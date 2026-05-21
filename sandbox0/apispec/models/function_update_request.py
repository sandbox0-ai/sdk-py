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
    from ..models.function_autoscaling import FunctionAutoscaling


T = TypeVar("T", bound="FunctionUpdateRequest")


@_attrs_define
class FunctionUpdateRequest:
    """
    Attributes:
        name (Union[Unset, str]): Mutable function display name. Slug and domain label stay stable.
        enabled (Union[Unset, bool]): Whether the function host should serve traffic. Disabled functions do not restore
            runtime sandboxes.
        autoscaling (Union[Unset, FunctionAutoscaling]): Function runtime pool autoscaling settings. target_concurrency
            is a soft routing and scale-out signal; it is not a strong distributed per-instance concurrency semaphore.
    """

    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    autoscaling: Union[Unset, "FunctionAutoscaling"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        enabled = self.enabled

        autoscaling: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.autoscaling, Unset):
            autoscaling = self.autoscaling.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if autoscaling is not UNSET:
            field_dict["autoscaling"] = autoscaling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_autoscaling import FunctionAutoscaling

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _autoscaling = d.pop("autoscaling", UNSET)
        autoscaling: Union[Unset, FunctionAutoscaling]
        if isinstance(_autoscaling, Unset):
            autoscaling = UNSET
        else:
            autoscaling = FunctionAutoscaling.from_dict(_autoscaling)

        function_update_request = cls(
            name=name,
            enabled=enabled,
            autoscaling=autoscaling,
        )

        function_update_request.additional_properties = d
        return function_update_request

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
