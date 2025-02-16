# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .analyze_document_result import AnalyzeDocumentResult
from .bounding_polygon import BoundingPolygon
from .cell import Cell
from .change_model_compartment_details import ChangeModelCompartmentDetails
from .change_project_compartment_details import ChangeProjectCompartmentDetails
from .create_model_details import CreateModelDetails
from .create_processor_job_details import CreateProcessorJobDetails
from .create_project_details import CreateProjectDetails
from .data_science_labeling_dataset import DataScienceLabelingDataset
from .dataset import Dataset
from .dataset_summary import DatasetSummary
from .detected_document_type import DetectedDocumentType
from .detected_language import DetectedLanguage
from .dimensions import Dimensions
from .document_classification_confidence_entry import DocumentClassificationConfidenceEntry
from .document_classification_feature import DocumentClassificationFeature
from .document_classification_label_metrics_report import DocumentClassificationLabelMetricsReport
from .document_classification_model_metrics import DocumentClassificationModelMetrics
from .document_classification_overall_metrics_report import DocumentClassificationOverallMetricsReport
from .document_feature import DocumentFeature
from .document_field import DocumentField
from .document_key_value_extraction_feature import DocumentKeyValueExtractionFeature
from .document_language_classification_feature import DocumentLanguageClassificationFeature
from .document_metadata import DocumentMetadata
from .document_table_extraction_feature import DocumentTableExtractionFeature
from .document_text_extraction_feature import DocumentTextExtractionFeature
from .field_label import FieldLabel
from .field_name import FieldName
from .field_value import FieldValue
from .general_processor_config import GeneralProcessorConfig
from .inline_document_content import InlineDocumentContent
from .input_location import InputLocation
from .key_value_detection_confidence_entry import KeyValueDetectionConfidenceEntry
from .key_value_detection_label_metrics_report import KeyValueDetectionLabelMetricsReport
from .key_value_detection_model_metrics import KeyValueDetectionModelMetrics
from .key_value_detection_overall_metrics_report import KeyValueDetectionOverallMetricsReport
from .line import Line
from .model import Model
from .model_collection import ModelCollection
from .model_metrics import ModelMetrics
from .model_summary import ModelSummary
from .normalized_vertex import NormalizedVertex
from .object_location import ObjectLocation
from .object_storage_dataset import ObjectStorageDataset
from .object_storage_locations import ObjectStorageLocations
from .output_location import OutputLocation
from .page import Page
from .processing_error import ProcessingError
from .processor_config import ProcessorConfig
from .processor_job import ProcessorJob
from .project import Project
from .project_collection import ProjectCollection
from .project_summary import ProjectSummary
from .table import Table
from .table_row import TableRow
from .update_model_details import UpdateModelDetails
from .update_project_details import UpdateProjectDetails
from .value_array import ValueArray
from .value_date import ValueDate
from .value_integer import ValueInteger
from .value_number import ValueNumber
from .value_phone_number import ValuePhoneNumber
from .value_string import ValueString
from .value_time import ValueTime
from .word import Word
from .work_request import WorkRequest
from .work_request_error import WorkRequestError
from .work_request_error_collection import WorkRequestErrorCollection
from .work_request_log_entry import WorkRequestLogEntry
from .work_request_log_entry_collection import WorkRequestLogEntryCollection
from .work_request_resource import WorkRequestResource
from .work_request_summary import WorkRequestSummary
from .work_request_summary_collection import WorkRequestSummaryCollection

# Maps type names to classes for ai_document services.
ai_document_type_mapping = {
    "AnalyzeDocumentResult": AnalyzeDocumentResult,
    "BoundingPolygon": BoundingPolygon,
    "Cell": Cell,
    "ChangeModelCompartmentDetails": ChangeModelCompartmentDetails,
    "ChangeProjectCompartmentDetails": ChangeProjectCompartmentDetails,
    "CreateModelDetails": CreateModelDetails,
    "CreateProcessorJobDetails": CreateProcessorJobDetails,
    "CreateProjectDetails": CreateProjectDetails,
    "DataScienceLabelingDataset": DataScienceLabelingDataset,
    "Dataset": Dataset,
    "DatasetSummary": DatasetSummary,
    "DetectedDocumentType": DetectedDocumentType,
    "DetectedLanguage": DetectedLanguage,
    "Dimensions": Dimensions,
    "DocumentClassificationConfidenceEntry": DocumentClassificationConfidenceEntry,
    "DocumentClassificationFeature": DocumentClassificationFeature,
    "DocumentClassificationLabelMetricsReport": DocumentClassificationLabelMetricsReport,
    "DocumentClassificationModelMetrics": DocumentClassificationModelMetrics,
    "DocumentClassificationOverallMetricsReport": DocumentClassificationOverallMetricsReport,
    "DocumentFeature": DocumentFeature,
    "DocumentField": DocumentField,
    "DocumentKeyValueExtractionFeature": DocumentKeyValueExtractionFeature,
    "DocumentLanguageClassificationFeature": DocumentLanguageClassificationFeature,
    "DocumentMetadata": DocumentMetadata,
    "DocumentTableExtractionFeature": DocumentTableExtractionFeature,
    "DocumentTextExtractionFeature": DocumentTextExtractionFeature,
    "FieldLabel": FieldLabel,
    "FieldName": FieldName,
    "FieldValue": FieldValue,
    "GeneralProcessorConfig": GeneralProcessorConfig,
    "InlineDocumentContent": InlineDocumentContent,
    "InputLocation": InputLocation,
    "KeyValueDetectionConfidenceEntry": KeyValueDetectionConfidenceEntry,
    "KeyValueDetectionLabelMetricsReport": KeyValueDetectionLabelMetricsReport,
    "KeyValueDetectionModelMetrics": KeyValueDetectionModelMetrics,
    "KeyValueDetectionOverallMetricsReport": KeyValueDetectionOverallMetricsReport,
    "Line": Line,
    "Model": Model,
    "ModelCollection": ModelCollection,
    "ModelMetrics": ModelMetrics,
    "ModelSummary": ModelSummary,
    "NormalizedVertex": NormalizedVertex,
    "ObjectLocation": ObjectLocation,
    "ObjectStorageDataset": ObjectStorageDataset,
    "ObjectStorageLocations": ObjectStorageLocations,
    "OutputLocation": OutputLocation,
    "Page": Page,
    "ProcessingError": ProcessingError,
    "ProcessorConfig": ProcessorConfig,
    "ProcessorJob": ProcessorJob,
    "Project": Project,
    "ProjectCollection": ProjectCollection,
    "ProjectSummary": ProjectSummary,
    "Table": Table,
    "TableRow": TableRow,
    "UpdateModelDetails": UpdateModelDetails,
    "UpdateProjectDetails": UpdateProjectDetails,
    "ValueArray": ValueArray,
    "ValueDate": ValueDate,
    "ValueInteger": ValueInteger,
    "ValueNumber": ValueNumber,
    "ValuePhoneNumber": ValuePhoneNumber,
    "ValueString": ValueString,
    "ValueTime": ValueTime,
    "Word": Word,
    "WorkRequest": WorkRequest,
    "WorkRequestError": WorkRequestError,
    "WorkRequestErrorCollection": WorkRequestErrorCollection,
    "WorkRequestLogEntry": WorkRequestLogEntry,
    "WorkRequestLogEntryCollection": WorkRequestLogEntryCollection,
    "WorkRequestResource": WorkRequestResource,
    "WorkRequestSummary": WorkRequestSummary,
    "WorkRequestSummaryCollection": WorkRequestSummaryCollection
}
