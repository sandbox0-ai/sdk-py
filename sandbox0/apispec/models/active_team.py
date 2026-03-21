from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveTeam")


@_attrs_define
class ActiveTeam:
    """
    Attributes:
        user_id (str):
        team_id (str):
        home_region_id (str):
        team_role (Union[Unset, str]):
        default_team (Union[Unset, bool]):
        edge_gateway_url (Union[None, Unset, str]):
    """

    user_id: str
    team_id: str
    home_region_id: str
    team_role: Union[Unset, str] = UNSET
    default_team: Union[Unset, bool] = UNSET
    edge_gateway_url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        team_id = self.team_id

        home_region_id = self.home_region_id

        team_role = self.team_role

        default_team = self.default_team

        edge_gateway_url: Union[None, Unset, str]
        if isinstance(self.edge_gateway_url, Unset):
            edge_gateway_url = UNSET
        else:
            edge_gateway_url = self.edge_gateway_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "team_id": team_id,
                "home_region_id": home_region_id,
            }
        )
        if team_role is not UNSET:
            field_dict["team_role"] = team_role
        if default_team is not UNSET:
            field_dict["default_team"] = default_team
        if edge_gateway_url is not UNSET:
            field_dict["edge_gateway_url"] = edge_gateway_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        team_id = d.pop("team_id")

        home_region_id = d.pop("home_region_id")

        team_role = d.pop("team_role", UNSET)

        default_team = d.pop("default_team", UNSET)

        def _parse_edge_gateway_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        edge_gateway_url = _parse_edge_gateway_url(d.pop("edge_gateway_url", UNSET))

        active_team = cls(
            user_id=user_id,
            team_id=team_id,
            home_region_id=home_region_id,
            team_role=team_role,
            default_team=default_team,
            edge_gateway_url=edge_gateway_url,
        )

        active_team.additional_properties = d
        return active_team

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
