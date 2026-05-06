from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.observability_log_record import ObservabilityLogRecord


T = TypeVar("T", bound="SuccessObservabilityLogRecordListResponseData")


@_attrs_define
class SuccessObservabilityLogRecordListResponseData:
    """
    Attributes:
        logs (Union[Unset, list['ObservabilityLogRecord']]):
    """

    logs: Union[Unset, list["ObservabilityLogRecord"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        logs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.logs, Unset):
            logs = []
            for logs_item_data in self.logs:
                logs_item = logs_item_data.to_dict()
                logs.append(logs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logs is not UNSET:
            field_dict["logs"] = logs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.observability_log_record import ObservabilityLogRecord

        d = dict(src_dict)
        logs = []
        _logs = d.pop("logs", UNSET)
        for logs_item_data in _logs or []:
            logs_item = ObservabilityLogRecord.from_dict(logs_item_data)

            logs.append(logs_item)

        success_observability_log_record_list_response_data = cls(
            logs=logs,
        )

        success_observability_log_record_list_response_data.additional_properties = d
        return success_observability_log_record_list_response_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
