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
    from ..models.list_volume_sync_conflicts_response import (
        ListVolumeSyncConflictsResponse,
    )


T = TypeVar("T", bound="SuccessVolumeSyncConflictListResponse")


@_attrs_define
class SuccessVolumeSyncConflictListResponse:
    """
    Attributes:
        success (bool):
        data (Union[Unset, ListVolumeSyncConflictsResponse]):
    """

    success: bool
    data: Union[Unset, "ListVolumeSyncConflictsResponse"] = UNSET
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
        from ..models.list_volume_sync_conflicts_response import (
            ListVolumeSyncConflictsResponse,
        )

        d = dict(src_dict)
        success = d.pop("success")

        _data = d.pop("data", UNSET)
        data: Union[Unset, ListVolumeSyncConflictsResponse]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ListVolumeSyncConflictsResponse.from_dict(_data)

        success_volume_sync_conflict_list_response = cls(
            success=success,
            data=data,
        )

        success_volume_sync_conflict_list_response.additional_properties = d
        return success_volume_sync_conflict_list_response

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
