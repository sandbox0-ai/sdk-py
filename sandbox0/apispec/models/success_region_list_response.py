from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.success_region_list_response_data import SuccessRegionListResponseData





T = TypeVar("T", bound="SuccessRegionListResponse")



@_attrs_define
class SuccessRegionListResponse:
    """ 
        Attributes:
            success (bool):
            data (Union[Unset, SuccessRegionListResponseData]):
     """

    success: bool
    data: Union[Unset, 'SuccessRegionListResponseData'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.success_region_list_response_data import SuccessRegionListResponseData
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
        from ..models.success_region_list_response_data import SuccessRegionListResponseData
        d = dict(src_dict)
        success = d.pop("success")

        _data = d.pop("data", UNSET)
        data: Union[Unset, SuccessRegionListResponseData]
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = SuccessRegionListResponseData.from_dict(_data)




        success_region_list_response = cls(
            success=success,
            data=data,
        )


        success_region_list_response.additional_properties = d
        return success_region_list_response

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
