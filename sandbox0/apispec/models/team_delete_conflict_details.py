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
    from ..models.team_delete_resource_count import TeamDeleteResourceCount


T = TypeVar("T", bound="TeamDeleteConflictDetails")


@_attrs_define
class TeamDeleteConflictDetails:
    """
    Attributes:
        team_id (str):
        blocking_resources (list['TeamDeleteResourceCount']): Resources that must be removed before the team can be
            deleted.
        retained_resources (Union[Unset, list['TeamDeleteResourceCount']]): Historical resources retained by policy.
            These do not block deletion.
        retention_policy (Union[Unset, str]): Summary of the historical metering retention policy for team deletion.
    """

    team_id: str
    blocking_resources: list["TeamDeleteResourceCount"]
    retained_resources: Union[Unset, list["TeamDeleteResourceCount"]] = UNSET
    retention_policy: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        blocking_resources = []
        for blocking_resources_item_data in self.blocking_resources:
            blocking_resources_item = blocking_resources_item_data.to_dict()
            blocking_resources.append(blocking_resources_item)

        retained_resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.retained_resources, Unset):
            retained_resources = []
            for retained_resources_item_data in self.retained_resources:
                retained_resources_item = retained_resources_item_data.to_dict()
                retained_resources.append(retained_resources_item)

        retention_policy = self.retention_policy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "blocking_resources": blocking_resources,
            }
        )
        if retained_resources is not UNSET:
            field_dict["retained_resources"] = retained_resources
        if retention_policy is not UNSET:
            field_dict["retention_policy"] = retention_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_delete_resource_count import TeamDeleteResourceCount

        d = dict(src_dict)
        team_id = d.pop("team_id")

        blocking_resources = []
        _blocking_resources = d.pop("blocking_resources")
        for blocking_resources_item_data in _blocking_resources:
            blocking_resources_item = TeamDeleteResourceCount.from_dict(
                blocking_resources_item_data
            )

            blocking_resources.append(blocking_resources_item)

        retained_resources = []
        _retained_resources = d.pop("retained_resources", UNSET)
        for retained_resources_item_data in _retained_resources or []:
            retained_resources_item = TeamDeleteResourceCount.from_dict(
                retained_resources_item_data
            )

            retained_resources.append(retained_resources_item)

        retention_policy = d.pop("retention_policy", UNSET)

        team_delete_conflict_details = cls(
            team_id=team_id,
            blocking_resources=blocking_resources,
            retained_resources=retained_resources,
            retention_policy=retention_policy,
        )

        team_delete_conflict_details.additional_properties = d
        return team_delete_conflict_details

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
