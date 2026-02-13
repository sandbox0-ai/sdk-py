import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_template_condition import SandboxTemplateCondition


T = TypeVar("T", bound="SandboxTemplateStatus")


@_attrs_define
class SandboxTemplateStatus:
    """
    Attributes:
        idle_count (Union[Unset, int]):
        active_count (Union[Unset, int]):
        conditions (Union[Unset, list['SandboxTemplateCondition']]):
        last_update_time (Union[Unset, datetime.datetime]):
    """

    idle_count: Union[Unset, int] = UNSET
    active_count: Union[Unset, int] = UNSET
    conditions: Union[Unset, list["SandboxTemplateCondition"]] = UNSET
    last_update_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idle_count = self.idle_count

        active_count = self.active_count

        conditions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        last_update_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_update_time, Unset):
            last_update_time = self.last_update_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idle_count is not UNSET:
            field_dict["idleCount"] = idle_count
        if active_count is not UNSET:
            field_dict["activeCount"] = active_count
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if last_update_time is not UNSET:
            field_dict["lastUpdateTime"] = last_update_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_template_condition import SandboxTemplateCondition

        d = dict(src_dict)
        idle_count = d.pop("idleCount", UNSET)

        active_count = d.pop("activeCount", UNSET)

        conditions = []
        _conditions = d.pop("conditions", UNSET)
        for conditions_item_data in _conditions or []:
            conditions_item = SandboxTemplateCondition.from_dict(conditions_item_data)

            conditions.append(conditions_item)

        _last_update_time = d.pop("lastUpdateTime", UNSET)
        last_update_time: Union[Unset, datetime.datetime]
        if isinstance(_last_update_time, Unset):
            last_update_time = UNSET
        else:
            last_update_time = isoparse(_last_update_time)

        sandbox_template_status = cls(
            idle_count=idle_count,
            active_count=active_count,
            conditions=conditions,
            last_update_time=last_update_time,
        )

        sandbox_template_status.additional_properties = d
        return sandbox_template_status

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
