# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from connector_builder.generated.models.any_of_interpolated_stringstring import AnyOfInterpolatedStringstring
from connector_builder.generated.models.any_of_min_max_datetimestring import AnyOfMinMaxDatetimestring
from connector_builder.generated.models.datetime_stream_slicer_all_of import DatetimeStreamSlicerAllOf
from connector_builder.generated.models.request_option import RequestOption
from connector_builder.generated.models.stream_slicer import StreamSlicer


class DatetimeStreamSlicer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    DatetimeStreamSlicer - a model defined in OpenAPI

        start_datetime: The start_datetime of this DatetimeStreamSlicer.
        end_datetime: The end_datetime of this DatetimeStreamSlicer.
        step: The step of this DatetimeStreamSlicer.
        cursor_field: The cursor_field of this DatetimeStreamSlicer.
        datetime_format: The datetime_format of this DatetimeStreamSlicer.
        config: The config of this DatetimeStreamSlicer.
        cursor: The cursor of this DatetimeStreamSlicer [Optional].
        cursor_end: The cursor_end of this DatetimeStreamSlicer [Optional].
        start_time_option: The start_time_option of this DatetimeStreamSlicer [Optional].
        end_time_option: The end_time_option of this DatetimeStreamSlicer [Optional].
        stream_state_field_start: The stream_state_field_start of this DatetimeStreamSlicer [Optional].
        stream_state_field_end: The stream_state_field_end of this DatetimeStreamSlicer [Optional].
        lookback_window: The lookback_window of this DatetimeStreamSlicer [Optional].
    """

    start_datetime: AnyOfMinMaxDatetimestring = Field(alias="start_datetime")
    end_datetime: AnyOfMinMaxDatetimestring = Field(alias="end_datetime")
    step: str = Field(alias="step")
    cursor_field: AnyOfInterpolatedStringstring = Field(alias="cursor_field")
    datetime_format: str = Field(alias="datetime_format")
    config: Dict[str, Any] = Field(alias="config")
    cursor: Optional[Dict[str, Any]] = Field(alias="_cursor", default=None)
    cursor_end: Optional[Dict[str, Any]] = Field(alias="_cursor_end", default=None)
    start_time_option: Optional[RequestOption] = Field(alias="start_time_option", default=None)
    end_time_option: Optional[RequestOption] = Field(alias="end_time_option", default=None)
    stream_state_field_start: Optional[str] = Field(alias="stream_state_field_start", default=None)
    stream_state_field_end: Optional[str] = Field(alias="stream_state_field_end", default=None)
    lookback_window: Optional[AnyOfInterpolatedStringstring] = Field(alias="lookback_window", default=None)

DatetimeStreamSlicer.update_forward_refs()