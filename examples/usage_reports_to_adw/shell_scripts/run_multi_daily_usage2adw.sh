#!/bin/bash
#############################################################################################################################
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.
#
# Author - Adi Zohar, Feb 28th 2020, Amended Oct 18th 2022
#
# Run Multi daily usage load for crontab use
#
# Amend variables below and database connectivity
# Use .oci/config profiles with user authentications
#
# Crontab set:
# 0 0 * * * timeout 6h /home/opc/usage_reports_to_adw/shell_scripts/run_multi_daily_usage2adw.sh > /home/opc/usage_reports_to_adw/cron_run_multi_tenants_crontab_run.txt 2>&1
#############################################################################################################################

# Env Variables based on yum instant client
export CLIENT_HOME=/usr/lib/oracle/current/client64
export PATH=$PATH:$CLIENT_HOME/bin:$CLIENT_HOME

# App dir
export TNS_ADMIN=$HOME/ADWCUSG
export APPDIR=$HOME/usage_reports_to_adw
export CREDFILE=$APPDIR/config.user
cd $APPDIR

# database info
export DATABASE_USER=`grep "^DATABASE_USER" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_PASS=`grep "^DATABASE_PASS" $CREDFILE | awk -F= '{ print $2 }'`
export DATABASE_NAME=`grep "^DATABASE_NAME" $CREDFILE | awk -F= '{ print $2 }'`
export TAG1_SPECIAL=`grep "^TAG_SPECIAL" $CREDFILE | awk -F= '{ print $2 }'`
export TAG2_SPECIAL=`grep "^TAG2_SPECIAL" $CREDFILE | awk -F= '{ print $2 }'`
export MIN_DATE=`grep "^EXTRACT_DATE" $CREDFILE | awk -F= '{ print $2 }'`

# Fixed variables
export DATE=`date '+%Y%m%d_%H%M'`
export REPORT_DIR=${APPDIR}/report
mkdir -p ${REPORT_DIR}

# Check if usage2adw.py already running
if (( `ps -ef |grep python |grep usage2adw.py |wc -l` > 0 ))
then
    echo "usage2adw.py is already running, abort.."
    ps -ef |grep python |grep usage2adw.py
    exit 1
fi

##################################
# Report Function
##################################
run_report()
{
    NAME=$1
    export tenant="-t $NAME"
    if [ -z "$NAME" ]
    then
        exit 1
    fi

    if [ "${1}" = "local" ]; then
        export tenant="-ip"
    fi

    if [ -z "${2}" ]
    then
        TAG1=$TAG1_SPECIAL
    else
        TAG1=$2
    fi

    if [ -z "${3}" ]
    then
        TAG2=$TAG2_SPECIAL
    else
        TAG2=$3
    fi

    DIR=${REPORT_DIR}/$NAME
    OUTPUT_FILE=${DIR}/${DATE}_${NAME}.txt
    mkdir -p $DIR
    echo "Running $NAME... to $OUTPUT_FILE "
    python3 $APPDIR/usage2adw.py $tenant -du $DATABASE_USER -dp $DATABASE_PASS -dn $DATABASE_NAME -d $MIN_DATE -ts "${TAG1}" -ts2 "${TAG2}" $4 |tee -a $OUTPUT_FILE
    grep -i "Error" $OUTPUT_FILE

    ERROR=""

    if (( `grep -i Error $OUTPUT_FILE | wc -l` > 0 ))
    then
        ERROR=" with **** Errors ****"
    fi

    echo "Finish `date` - $NAME $ERROR "
}

###########################################################
# Main
###########################################################
# local - authentication by instant principle
# add oci config tenant profile to add more tenants to load
##################################
echo "Start running at `date`..."

run_report local
#run_report tenant2 tagspecial1 tagspecial2
#run_report tenant3 tagspecial1 tagspecial2

echo "Completed at `date`.."
