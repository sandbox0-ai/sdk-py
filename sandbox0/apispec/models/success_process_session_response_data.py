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
    from ..models.process_session import ProcessSession


T = TypeVar("T", bound="SuccessProcessSessionResponseData")


@_attrs_define
class SuccessProcessSessionResponseData:
    """
    Attributes:
        process (Union[Unset, ProcessSession]):
    """

    process: Union[Unset, "ProcessSession"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.process, Unset):
            process = self.process.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process is not UNSET:
            field_dict["process"] = process

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_session import ProcessSession

        d = dict(src_dict)
        _process = d.pop("process", UNSET)
        process: Union[Unset, ProcessSession]
        if isinstance(_process, Unset):
            process = UNSET
        else:
            process = ProcessSession.from_dict(_process)

        success_process_session_response_data = cls(
            process=process,
        )

        success_process_session_response_data.additional_properties = d
        return success_process_session_response_data

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
