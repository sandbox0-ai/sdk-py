from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.region import Region





T = TypeVar("T", bound="SuccessRegionListResponseData")



@_attrs_define
class SuccessRegionListResponseData:
    """ 
        Attributes:
            regions (Union[Unset, list['Region']]):
     """

    regions: Union[Unset, list['Region']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.region import Region
        regions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.regions, Unset):
            regions = []
            for regions_item_data in self.regions:
                regions_item = regions_item_data.to_dict()
                regions.append(regions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if regions is not UNSET:
            field_dict["regions"] = regions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.region import Region
        d = dict(src_dict)
        regions = []
        _regions = d.pop("regions", UNSET)
        for regions_item_data in (_regions or []):
            regions_item = Region.from_dict(regions_item_data)



            regions.append(regions_item)


        success_region_list_response_data = cls(
            regions=regions,
        )


        success_region_list_response_data.additional_properties = d
        return success_region_list_response_data

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
