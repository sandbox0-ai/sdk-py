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
    from ..models.function_source_request import FunctionSourceRequest


T = TypeVar("T", bound="FunctionCreateRequest")


@_attrs_define
class FunctionCreateRequest:
    """
    Attributes:
        source (FunctionSourceRequest): Source used to create a function revision. Omitting type with sandbox_id and
            service_id keeps the sandbox-service shortcut shape; internally it is compiled into an immutable
            FunctionRevisionSpec.
        name (Union[Unset, str]): Function display name. Defaults to the source service name or ID when omitted.
        autoscaling (Union[Unset, FunctionAutoscaling]): Function runtime pool autoscaling settings. target_concurrency
            is a soft routing and scale-out signal; it is not a strong distributed per-instance concurrency semaphore.
    """

    source: "FunctionSourceRequest"
    name: Union[Unset, str] = UNSET
    autoscaling: Union[Unset, "FunctionAutoscaling"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source.to_dict()

        name = self.name

        autoscaling: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.autoscaling, Unset):
            autoscaling = self.autoscaling.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if autoscaling is not UNSET:
            field_dict["autoscaling"] = autoscaling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_autoscaling import FunctionAutoscaling
        from ..models.function_source_request import FunctionSourceRequest

        d = dict(src_dict)
        source = FunctionSourceRequest.from_dict(d.pop("source"))

        name = d.pop("name", UNSET)

        _autoscaling = d.pop("autoscaling", UNSET)
        autoscaling: Union[Unset, FunctionAutoscaling]
        if isinstance(_autoscaling, Unset):
            autoscaling = UNSET
        else:
            autoscaling = FunctionAutoscaling.from_dict(_autoscaling)

        function_create_request = cls(
            source=source,
            name=name,
            autoscaling=autoscaling,
        )

        function_create_request.additional_properties = d
        return function_create_request

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
