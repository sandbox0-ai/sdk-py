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
    from ..models.volume_sync_filesystem_capabilities import (
        VolumeSyncFilesystemCapabilities,
    )


T = TypeVar("T", bound="UpsertSyncReplicaRequest")


@_attrs_define
class UpsertSyncReplicaRequest:
    """
    Attributes:
        display_name (Union[Unset, str]):
        platform (Union[Unset, str]):
        root_path (Union[Unset, str]):
        case_sensitive (Union[Unset, bool]):
        capabilities (Union[Unset, VolumeSyncFilesystemCapabilities]):
    """

    display_name: Union[Unset, str] = UNSET
    platform: Union[Unset, str] = UNSET
    root_path: Union[Unset, str] = UNSET
    case_sensitive: Union[Unset, bool] = UNSET
    capabilities: Union[Unset, "VolumeSyncFilesystemCapabilities"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        platform = self.platform

        root_path = self.root_path

        case_sensitive = self.case_sensitive

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_sync_filesystem_capabilities import (
            VolumeSyncFilesystemCapabilities,
        )

        d = dict(src_dict)
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

        upsert_sync_replica_request = cls(
            display_name=display_name,
            platform=platform,
            root_path=root_path,
            case_sensitive=case_sensitive,
            capabilities=capabilities,
        )

        upsert_sync_replica_request.additional_properties = d
        return upsert_sync_replica_request

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
