from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.quota_dimension import QuotaDimension
from ..types import UNSET, Unset
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="TeamQuota")



@_attrs_define
class TeamQuota:
    """ 
        Attributes:
            team_id (str):
            dimension (QuotaDimension):
            limit_value (Union[None, Unset, int]):
     """

    team_id: str
    dimension: QuotaDimension
    limit_value: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        dimension = self.dimension.value

        limit_value: Union[None, Unset, int]
        if isinstance(self.limit_value, Unset):
            limit_value = UNSET
        else:
            limit_value = self.limit_value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "team_id": team_id,
            "dimension": dimension,
        })
        if limit_value is not UNSET:
            field_dict["limit_value"] = limit_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        dimension = QuotaDimension(d.pop("dimension"))




        def _parse_limit_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        limit_value = _parse_limit_value(d.pop("limit_value", UNSET))


        team_quota = cls(
            team_id=team_id,
            dimension=dimension,
            limit_value=limit_value,
        )


        team_quota.additional_properties = d
        return team_quota

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
