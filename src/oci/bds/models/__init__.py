# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .activate_bds_metastore_configuration_details import ActivateBdsMetastoreConfigurationDetails
from .add_auto_scale_policy_details import AddAutoScalePolicyDetails
from .add_auto_scaling_configuration_details import AddAutoScalingConfigurationDetails
from .add_block_storage_details import AddBlockStorageDetails
from .add_cloud_sql_details import AddCloudSqlDetails
from .add_kafka_details import AddKafkaDetails
from .add_metric_based_horizontal_scaling_policy_details import AddMetricBasedHorizontalScalingPolicyDetails
from .add_metric_based_vertical_scaling_policy_details import AddMetricBasedVerticalScalingPolicyDetails
from .add_schedule_based_horizontal_scaling_policy_details import AddScheduleBasedHorizontalScalingPolicyDetails
from .add_schedule_based_vertical_scaling_policy_details import AddScheduleBasedVerticalScalingPolicyDetails
from .add_worker_nodes_details import AddWorkerNodesDetails
from .auto_scale_policy import AutoScalePolicy
from .auto_scale_policy_details import AutoScalePolicyDetails
from .auto_scale_policy_metric_rule import AutoScalePolicyMetricRule
from .auto_scale_policy_rule import AutoScalePolicyRule
from .auto_scaling_configuration import AutoScalingConfiguration
from .auto_scaling_configuration_summary import AutoScalingConfigurationSummary
from .bds_api_key import BdsApiKey
from .bds_api_key_summary import BdsApiKeySummary
from .bds_instance import BdsInstance
from .bds_instance_summary import BdsInstanceSummary
from .bds_metastore_configuration import BdsMetastoreConfiguration
from .bds_metastore_configuration_summary import BdsMetastoreConfigurationSummary
from .change_bds_instance_compartment_details import ChangeBdsInstanceCompartmentDetails
from .change_shape_details import ChangeShapeDetails
from .change_shape_nodes import ChangeShapeNodes
from .cloud_sql_details import CloudSqlDetails
from .cluster_details import ClusterDetails
from .create_bds_api_key_details import CreateBdsApiKeyDetails
from .create_bds_instance_details import CreateBdsInstanceDetails
from .create_bds_metastore_configuration_details import CreateBdsMetastoreConfigurationDetails
from .create_node_details import CreateNodeDetails
from .day_based_horizontal_scaling_schedule_details import DayBasedHorizontalScalingScheduleDetails
from .day_based_vertical_scaling_schedule_details import DayBasedVerticalScalingScheduleDetails
from .default_error import DefaultError
from .execute_bootstrap_script_details import ExecuteBootstrapScriptDetails
from .horizontal_scaling_schedule_details import HorizontalScalingScheduleDetails
from .install_patch_details import InstallPatchDetails
from .kerberos_details import KerberosDetails
from .metric_based_horizontal_scale_in_config import MetricBasedHorizontalScaleInConfig
from .metric_based_horizontal_scale_out_config import MetricBasedHorizontalScaleOutConfig
from .metric_based_horizontal_scaling_policy_details import MetricBasedHorizontalScalingPolicyDetails
from .metric_based_vertical_scale_down_config import MetricBasedVerticalScaleDownConfig
from .metric_based_vertical_scale_up_config import MetricBasedVerticalScaleUpConfig
from .metric_based_vertical_scaling_policy_details import MetricBasedVerticalScalingPolicyDetails
from .metric_threshold_rule import MetricThresholdRule
from .network_config import NetworkConfig
from .node import Node
from .patch_history_summary import PatchHistorySummary
from .patch_summary import PatchSummary
from .remove_auto_scaling_configuration_details import RemoveAutoScalingConfigurationDetails
from .remove_cloud_sql_details import RemoveCloudSqlDetails
from .remove_kafka_details import RemoveKafkaDetails
from .remove_node_details import RemoveNodeDetails
from .restart_node_details import RestartNodeDetails
from .schedule_based_horizontal_scaling_policy_details import ScheduleBasedHorizontalScalingPolicyDetails
from .schedule_based_vertical_scaling_policy_details import ScheduleBasedVerticalScalingPolicyDetails
from .shape_config_details import ShapeConfigDetails
from .start_bds_instance_details import StartBdsInstanceDetails
from .stop_bds_instance_details import StopBdsInstanceDetails
from .test_bds_metastore_configuration_details import TestBdsMetastoreConfigurationDetails
from .test_bds_object_storage_connection_details import TestBdsObjectStorageConnectionDetails
from .time_and_horizontal_scaling_config import TimeAndHorizontalScalingConfig
from .time_and_vertical_scaling_config import TimeAndVerticalScalingConfig
from .update_auto_scale_policy_details import UpdateAutoScalePolicyDetails
from .update_auto_scaling_configuration_details import UpdateAutoScalingConfigurationDetails
from .update_bds_instance_details import UpdateBdsInstanceDetails
from .update_bds_metastore_configuration_details import UpdateBdsMetastoreConfigurationDetails
from .update_metric_based_horizontal_scaling_policy_details import UpdateMetricBasedHorizontalScalingPolicyDetails
from .update_metric_based_vertical_scaling_policy_details import UpdateMetricBasedVerticalScalingPolicyDetails
from .update_schedule_based_horizontal_scaling_policy_details import UpdateScheduleBasedHorizontalScalingPolicyDetails
from .update_schedule_based_vertical_scaling_policy_details import UpdateScheduleBasedVerticalScalingPolicyDetails
from .vertical_scaling_schedule_details import VerticalScalingScheduleDetails
from .volume_attachment_detail import VolumeAttachmentDetail
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_resource import WorkRequestResource

# Maps type names to classes for bds services.
bds_type_mapping = {
    "ActivateBdsMetastoreConfigurationDetails": ActivateBdsMetastoreConfigurationDetails,
    "AddAutoScalePolicyDetails": AddAutoScalePolicyDetails,
    "AddAutoScalingConfigurationDetails": AddAutoScalingConfigurationDetails,
    "AddBlockStorageDetails": AddBlockStorageDetails,
    "AddCloudSqlDetails": AddCloudSqlDetails,
    "AddKafkaDetails": AddKafkaDetails,
    "AddMetricBasedHorizontalScalingPolicyDetails": AddMetricBasedHorizontalScalingPolicyDetails,
    "AddMetricBasedVerticalScalingPolicyDetails": AddMetricBasedVerticalScalingPolicyDetails,
    "AddScheduleBasedHorizontalScalingPolicyDetails": AddScheduleBasedHorizontalScalingPolicyDetails,
    "AddScheduleBasedVerticalScalingPolicyDetails": AddScheduleBasedVerticalScalingPolicyDetails,
    "AddWorkerNodesDetails": AddWorkerNodesDetails,
    "AutoScalePolicy": AutoScalePolicy,
    "AutoScalePolicyDetails": AutoScalePolicyDetails,
    "AutoScalePolicyMetricRule": AutoScalePolicyMetricRule,
    "AutoScalePolicyRule": AutoScalePolicyRule,
    "AutoScalingConfiguration": AutoScalingConfiguration,
    "AutoScalingConfigurationSummary": AutoScalingConfigurationSummary,
    "BdsApiKey": BdsApiKey,
    "BdsApiKeySummary": BdsApiKeySummary,
    "BdsInstance": BdsInstance,
    "BdsInstanceSummary": BdsInstanceSummary,
    "BdsMetastoreConfiguration": BdsMetastoreConfiguration,
    "BdsMetastoreConfigurationSummary": BdsMetastoreConfigurationSummary,
    "ChangeBdsInstanceCompartmentDetails": ChangeBdsInstanceCompartmentDetails,
    "ChangeShapeDetails": ChangeShapeDetails,
    "ChangeShapeNodes": ChangeShapeNodes,
    "CloudSqlDetails": CloudSqlDetails,
    "ClusterDetails": ClusterDetails,
    "CreateBdsApiKeyDetails": CreateBdsApiKeyDetails,
    "CreateBdsInstanceDetails": CreateBdsInstanceDetails,
    "CreateBdsMetastoreConfigurationDetails": CreateBdsMetastoreConfigurationDetails,
    "CreateNodeDetails": CreateNodeDetails,
    "DayBasedHorizontalScalingScheduleDetails": DayBasedHorizontalScalingScheduleDetails,
    "DayBasedVerticalScalingScheduleDetails": DayBasedVerticalScalingScheduleDetails,
    "DefaultError": DefaultError,
    "ExecuteBootstrapScriptDetails": ExecuteBootstrapScriptDetails,
    "HorizontalScalingScheduleDetails": HorizontalScalingScheduleDetails,
    "InstallPatchDetails": InstallPatchDetails,
    "KerberosDetails": KerberosDetails,
    "MetricBasedHorizontalScaleInConfig": MetricBasedHorizontalScaleInConfig,
    "MetricBasedHorizontalScaleOutConfig": MetricBasedHorizontalScaleOutConfig,
    "MetricBasedHorizontalScalingPolicyDetails": MetricBasedHorizontalScalingPolicyDetails,
    "MetricBasedVerticalScaleDownConfig": MetricBasedVerticalScaleDownConfig,
    "MetricBasedVerticalScaleUpConfig": MetricBasedVerticalScaleUpConfig,
    "MetricBasedVerticalScalingPolicyDetails": MetricBasedVerticalScalingPolicyDetails,
    "MetricThresholdRule": MetricThresholdRule,
    "NetworkConfig": NetworkConfig,
    "Node": Node,
    "PatchHistorySummary": PatchHistorySummary,
    "PatchSummary": PatchSummary,
    "RemoveAutoScalingConfigurationDetails": RemoveAutoScalingConfigurationDetails,
    "RemoveCloudSqlDetails": RemoveCloudSqlDetails,
    "RemoveKafkaDetails": RemoveKafkaDetails,
    "RemoveNodeDetails": RemoveNodeDetails,
    "RestartNodeDetails": RestartNodeDetails,
    "ScheduleBasedHorizontalScalingPolicyDetails": ScheduleBasedHorizontalScalingPolicyDetails,
    "ScheduleBasedVerticalScalingPolicyDetails": ScheduleBasedVerticalScalingPolicyDetails,
    "ShapeConfigDetails": ShapeConfigDetails,
    "StartBdsInstanceDetails": StartBdsInstanceDetails,
    "StopBdsInstanceDetails": StopBdsInstanceDetails,
    "TestBdsMetastoreConfigurationDetails": TestBdsMetastoreConfigurationDetails,
    "TestBdsObjectStorageConnectionDetails": TestBdsObjectStorageConnectionDetails,
    "TimeAndHorizontalScalingConfig": TimeAndHorizontalScalingConfig,
    "TimeAndVerticalScalingConfig": TimeAndVerticalScalingConfig,
    "UpdateAutoScalePolicyDetails": UpdateAutoScalePolicyDetails,
    "UpdateAutoScalingConfigurationDetails": UpdateAutoScalingConfigurationDetails,
    "UpdateBdsInstanceDetails": UpdateBdsInstanceDetails,
    "UpdateBdsMetastoreConfigurationDetails": UpdateBdsMetastoreConfigurationDetails,
    "UpdateMetricBasedHorizontalScalingPolicyDetails": UpdateMetricBasedHorizontalScalingPolicyDetails,
    "UpdateMetricBasedVerticalScalingPolicyDetails": UpdateMetricBasedVerticalScalingPolicyDetails,
    "UpdateScheduleBasedHorizontalScalingPolicyDetails": UpdateScheduleBasedHorizontalScalingPolicyDetails,
    "UpdateScheduleBasedVerticalScalingPolicyDetails": UpdateScheduleBasedVerticalScalingPolicyDetails,
    "VerticalScalingScheduleDetails": VerticalScalingScheduleDetails,
    "VolumeAttachmentDetail": VolumeAttachmentDetail,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestResource": WorkRequestResource
}
