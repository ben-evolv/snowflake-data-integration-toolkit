# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from connector_builder.generated.models.any_of_cartesian_product_stream_slicer_datetime_stream_slicer_list_stream_slicer_single_slice_substream_slicer import AnyOfCartesianProductStreamSlicerDatetimeStreamSlicerListStreamSlicerSingleSliceSubstreamSlicer
from connector_builder.generated.models.any_of_default_paginator_no_pagination import AnyOfDefaultPaginatorNoPagination
from connector_builder.generated.models.any_of_interpolated_stringstring import AnyOfInterpolatedStringstring
from connector_builder.generated.models.any_ofarrayarraystring import AnyOfarrayarraystring
from connector_builder.generated.models.http_requester import HttpRequester
from connector_builder.generated.models.record_selector import RecordSelector
from connector_builder.generated.models.simple_retriever_all_of import SimpleRetrieverAllOf


class SimpleRetriever(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SimpleRetriever - a model defined in OpenAPI

        requester: The requester of this SimpleRetriever.
        record_selector: The record_selector of this SimpleRetriever.
        config: The config of this SimpleRetriever.
        name: The name of this SimpleRetriever [Optional].
        name: The name of this SimpleRetriever [Optional].
        primary_key: The primary_key of this SimpleRetriever [Optional].
        primary_key: The primary_key of this SimpleRetriever [Optional].
        paginator: The paginator of this SimpleRetriever [Optional].
        stream_slicer: The stream_slicer of this SimpleRetriever [Optional].
    """

    requester: HttpRequester = Field(alias="requester")
    record_selector: RecordSelector = Field(alias="record_selector")
    config: Dict[str, Any] = Field(alias="config")
    name: Optional[str] = Field(alias="name", default=None)
    name: Optional[AnyOfInterpolatedStringstring] = Field(alias="_name", default=None)
    primary_key: Optional[AnyOfarrayarraystring] = Field(alias="primary_key", default=None)
    primary_key: Optional[str] = Field(alias="_primary_key", default=None)
    paginator: Optional[AnyOfDefaultPaginatorNoPagination] = Field(alias="paginator", default=None)
    stream_slicer: Optional[AnyOfCartesianProductStreamSlicerDatetimeStreamSlicerListStreamSlicerSingleSliceSubstreamSlicer] = Field(alias="stream_slicer", default=None)

SimpleRetriever.update_forward_refs()