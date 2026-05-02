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
    from ..models.public_gateway_config import PublicGatewayConfig


T = TypeVar("T", bound="SuccessPublicGatewayResponseData")


@_attrs_define
class SuccessPublicGatewayResponseData:
    """
    Attributes:
        sandbox_id (str):
        public_gateway (PublicGatewayConfig):
        exposure_domain (Union[Unset, str]):
    """

    sandbox_id: str
    public_gateway: "PublicGatewayConfig"
    exposure_domain: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        public_gateway = self.public_gateway.to_dict()

        exposure_domain = self.exposure_domain

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "public_gateway": public_gateway,
            }
        )
        if exposure_domain is not UNSET:
            field_dict["exposure_domain"] = exposure_domain

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_gateway_config import PublicGatewayConfig

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        public_gateway = PublicGatewayConfig.from_dict(d.pop("public_gateway"))

        exposure_domain = d.pop("exposure_domain", UNSET)

        success_public_gateway_response_data = cls(
            sandbox_id=sandbox_id,
            public_gateway=public_gateway,
            exposure_domain=exposure_domain,
        )

        success_public_gateway_response_data.additional_properties = d
        return success_public_gateway_response_data

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
