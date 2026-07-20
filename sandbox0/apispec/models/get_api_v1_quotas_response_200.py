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
    from ..models.team_quota import TeamQuota


T = TypeVar("T", bound="GetApiV1QuotasResponse200")


@_attrs_define
class GetApiV1QuotasResponse200:
    """
    Attributes:
        success (bool):
        data (Union[Unset, list['TeamQuota']]):
    """

    success: bool
    data: Union[Unset, list["TeamQuota"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_quota import TeamQuota

        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = TeamQuota.from_dict(data_item_data)

            data.append(data_item)

        get_api_v1_quotas_response_200 = cls(
            success=success,
            data=data,
        )

        get_api_v1_quotas_response_200.additional_properties = d
        return get_api_v1_quotas_response_200

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
