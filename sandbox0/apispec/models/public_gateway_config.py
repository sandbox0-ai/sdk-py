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
    from ..models.public_gateway_route import PublicGatewayRoute


T = TypeVar("T", bound="PublicGatewayConfig")


@_attrs_define
class PublicGatewayConfig:
    """
    Attributes:
        enabled (bool): Enables request-level public gateway enforcement for sandbox public traffic.
        routes (Union[Unset, list['PublicGatewayRoute']]):
    """

    enabled: bool
    routes: Union[Unset, list["PublicGatewayRoute"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        routes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.routes, Unset):
            routes = []
            for routes_item_data in self.routes:
                routes_item = routes_item_data.to_dict()
                routes.append(routes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
            }
        )
        if routes is not UNSET:
            field_dict["routes"] = routes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_gateway_route import PublicGatewayRoute

        d = dict(src_dict)
        enabled = d.pop("enabled")

        routes = []
        _routes = d.pop("routes", UNSET)
        for routes_item_data in _routes or []:
            routes_item = PublicGatewayRoute.from_dict(routes_item_data)

            routes.append(routes_item)

        public_gateway_config = cls(
            enabled=enabled,
            routes=routes,
        )

        public_gateway_config.additional_properties = d
        return public_gateway_config

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
