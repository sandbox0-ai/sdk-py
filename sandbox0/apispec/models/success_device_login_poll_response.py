from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.device_login_poll_response import DeviceLoginPollResponse





T = TypeVar("T", bound="SuccessDeviceLoginPollResponse")



@_attrs_define
class SuccessDeviceLoginPollResponse:
    """ 
        Attributes:
            success (bool):
            data (Union[Unset, DeviceLoginPollResponse]):
     """

    success: bool
    data: Union[Unset, 'DeviceLoginPollResponse'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.device_login_poll_response import DeviceLoginPollResponse
        success = self.success

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
        })
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_login_poll_response import DeviceLoginPollResponse
        d = dict(src_dict)
        success = d.pop("success")

        _data = d.pop("data", UNSET)
        data: Union[Unset, DeviceLoginPollResponse]
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = DeviceLoginPollResponse.from_dict(_data)




        success_device_login_poll_response = cls(
            success=success,
            data=data,
        )


        success_device_login_poll_response.additional_properties = d
        return success_device_login_poll_response

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
