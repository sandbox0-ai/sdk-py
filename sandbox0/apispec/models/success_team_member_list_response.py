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
    from ..models.success_team_member_list_response_data import (
        SuccessTeamMemberListResponseData,
    )


T = TypeVar("T", bound="SuccessTeamMemberListResponse")


@_attrs_define
class SuccessTeamMemberListResponse:
    """
    Attributes:
        success (bool):
        data (Union[Unset, SuccessTeamMemberListResponseData]):
    """

    success: bool
    data: Union[Unset, "SuccessTeamMemberListResponseData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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
        from ..models.success_team_member_list_response_data import (
            SuccessTeamMemberListResponseData,
        )

        d = dict(src_dict)
        success = d.pop("success")

        _data = d.pop("data", UNSET)
        data: Union[Unset, SuccessTeamMemberListResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = SuccessTeamMemberListResponseData.from_dict(_data)

        success_team_member_list_response = cls(
            success=success,
            data=data,
        )

        success_team_member_list_response.additional_properties = d
        return success_team_member_list_response

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
