from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="CreateRegionRequest")



@_attrs_define
class CreateRegionRequest:
    """ 
        Attributes:
            id (str):
            regional_gateway_url (str):
            display_name (Union[Unset, str]):
            metering_export_url (Union[None, Unset, str]):
            enabled (Union[Unset, bool]):
     """

    id: str
    regional_gateway_url: str
    display_name: Union[Unset, str] = UNSET
    metering_export_url: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        regional_gateway_url = self.regional_gateway_url

        display_name = self.display_name

        metering_export_url: Union[None, Unset, str]
        if isinstance(self.metering_export_url, Unset):
            metering_export_url = UNSET
        else:
            metering_export_url = self.metering_export_url

        enabled = self.enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "regional_gateway_url": regional_gateway_url,
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if metering_export_url is not UNSET:
            field_dict["metering_export_url"] = metering_export_url
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        regional_gateway_url = d.pop("regional_gateway_url")

        display_name = d.pop("display_name", UNSET)

        def _parse_metering_export_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        metering_export_url = _parse_metering_export_url(d.pop("metering_export_url", UNSET))


        enabled = d.pop("enabled", UNSET)

        create_region_request = cls(
            id=id,
            regional_gateway_url=regional_gateway_url,
            display_name=display_name,
            metering_export_url=metering_export_url,
            enabled=enabled,
        )


        create_region_request.additional_properties = d
        return create_region_request

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
