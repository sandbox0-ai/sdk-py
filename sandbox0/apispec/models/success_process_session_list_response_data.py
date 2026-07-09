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


T = TypeVar("T", bound="SuccessProcessSessionListResponseData")


@_attrs_define
class SuccessProcessSessionListResponseData:
    """
    Attributes:
        processes (Union[Unset, list['ProcessSession']]):
    """

    processes: Union[Unset, list["ProcessSession"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.processes, Unset):
            processes = []
            for processes_item_data in self.processes:
                processes_item = processes_item_data.to_dict()
                processes.append(processes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processes is not UNSET:
            field_dict["processes"] = processes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_session import ProcessSession

        d = dict(src_dict)
        processes = []
        _processes = d.pop("processes", UNSET)
        for processes_item_data in _processes or []:
            processes_item = ProcessSession.from_dict(processes_item_data)

            processes.append(processes_item)

        success_process_session_list_response_data = cls(
            processes=processes,
        )

        success_process_session_list_response_data.additional_properties = d
        return success_process_session_list_response_data

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
