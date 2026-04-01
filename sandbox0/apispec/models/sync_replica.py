import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_sync_filesystem_capabilities import (
        VolumeSyncFilesystemCapabilities,
    )


T = TypeVar("T", bound="SyncReplica")


@_attrs_define
class SyncReplica:
    """
    Attributes:
        id (Union[Unset, str]):
        volume_id (Union[Unset, str]):
        team_id (Union[Unset, str]):
        display_name (Union[Unset, str]):
        platform (Union[Unset, str]):
        root_path (Union[Unset, str]):
        case_sensitive (Union[Unset, bool]):
        capabilities (Union[Unset, VolumeSyncFilesystemCapabilities]):
        last_seen_at (Union[Unset, datetime.datetime]):
        last_applied_seq (Union[Unset, int]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    volume_id: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    root_path: Union[Unset, str] = UNSET
    case_sensitive: Union[Unset, bool] = UNSET
    capabilities: Union[Unset, "VolumeSyncFilesystemCapabilities"] = UNSET
    last_seen_at: Union[Unset, datetime.datetime] = UNSET
    last_applied_seq: Union[Unset, int] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        volume_id = self.volume_id

        team_id = self.team_id

        display_name = self.display_name

        platform = self.platform

        root_path = self.root_path

        case_sensitive = self.case_sensitive

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        last_seen_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_seen_at, Unset):
            last_seen_at = self.last_seen_at.isoformat()

        last_applied_seq = self.last_applied_seq

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if root_path is not UNSET:
            field_dict["root_path"] = root_path
        if case_sensitive is not UNSET:
            field_dict["case_sensitive"] = case_sensitive
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if last_seen_at is not UNSET:
            field_dict["last_seen_at"] = last_seen_at
        if last_applied_seq is not UNSET:
            field_dict["last_applied_seq"] = last_applied_seq
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_sync_filesystem_capabilities import (
            VolumeSyncFilesystemCapabilities,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        volume_id = d.pop("volume_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        platform = d.pop("platform", UNSET)

        root_path = d.pop("root_path", UNSET)

        case_sensitive = d.pop("case_sensitive", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, VolumeSyncFilesystemCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = VolumeSyncFilesystemCapabilities.from_dict(_capabilities)

        _last_seen_at = d.pop("last_seen_at", UNSET)
        last_seen_at: Union[Unset, datetime.datetime]
        if isinstance(_last_seen_at, Unset):
            last_seen_at = UNSET
        else:
            last_seen_at = isoparse(_last_seen_at)

        last_applied_seq = d.pop("last_applied_seq", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        sync_replica = cls(
            id=id,
            volume_id=volume_id,
            team_id=team_id,
            display_name=display_name,
            platform=platform,
            root_path=root_path,
            case_sensitive=case_sensitive,
            capabilities=capabilities,
            last_seen_at=last_seen_at,
            last_applied_seq=last_applied_seq,
            created_at=created_at,
            updated_at=updated_at,
        )

        sync_replica.additional_properties = d
        return sync_replica

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
