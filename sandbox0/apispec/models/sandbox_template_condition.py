import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxTemplateCondition")


@_attrs_define
class SandboxTemplateCondition:
    """
    Attributes:
        type_ (Union[Unset, str]):
        status (Union[Unset, str]):
        last_transition_time (Union[Unset, datetime.datetime]):
        reason (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    type_: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    last_transition_time: Union[Unset, datetime.datetime] = UNSET
    reason: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        status = self.status

        last_transition_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_transition_time, Unset):
            last_transition_time = self.last_transition_time.isoformat()

        reason = self.reason

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if last_transition_time is not UNSET:
            field_dict["lastTransitionTime"] = last_transition_time
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        _last_transition_time = d.pop("lastTransitionTime", UNSET)
        last_transition_time: Union[Unset, datetime.datetime]
        if isinstance(_last_transition_time, Unset):
            last_transition_time = UNSET
        else:
            last_transition_time = isoparse(_last_transition_time)

        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        sandbox_template_condition = cls(
            type_=type_,
            status=status,
            last_transition_time=last_transition_time,
            reason=reason,
            message=message,
        )

        sandbox_template_condition.additional_properties = d
        return sandbox_template_condition

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
