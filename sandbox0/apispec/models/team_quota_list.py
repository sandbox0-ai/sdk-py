from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.team_quota_status import TeamQuotaStatus


T = TypeVar("T", bound="TeamQuotaList")


@_attrs_define
class TeamQuotaList:
    """
    Attributes:
        team_id (str):
        quotas (list['TeamQuotaStatus']):
    """

    team_id: str
    quotas: list["TeamQuotaStatus"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        quotas = []
        for quotas_item_data in self.quotas:
            quotas_item = quotas_item_data.to_dict()
            quotas.append(quotas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "quotas": quotas,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_quota_status import TeamQuotaStatus

        d = dict(src_dict)
        team_id = d.pop("team_id")

        quotas = []
        _quotas = d.pop("quotas")
        for quotas_item_data in _quotas:
            quotas_item = TeamQuotaStatus.from_dict(quotas_item_data)

            quotas.append(quotas_item)

        team_quota_list = cls(
            team_id=team_id,
            quotas=quotas,
        )

        team_quota_list.additional_properties = d
        return team_quota_list

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
