from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateExecutionSessionAttemptRequest")


@_attrs_define
class CreateExecutionSessionAttemptRequest:
    """
    Attributes:
        replace_current (Union[Unset, bool]):  Default: False.
    """

    replace_current: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replace_current = self.replace_current

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replace_current is not UNSET:
            field_dict["replace_current"] = replace_current

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        replace_current = d.pop("replace_current", UNSET)

        create_execution_session_attempt_request = cls(
            replace_current=replace_current,
        )

        create_execution_session_attempt_request.additional_properties = d
        return create_execution_session_attempt_request

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
