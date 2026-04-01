from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.volume_sync_filesystem_capabilities import (
        VolumeSyncFilesystemCapabilities,
    )


T = TypeVar("T", bound="CreateVolumeSyncBootstrapRequest")


@_attrs_define
class CreateVolumeSyncBootstrapRequest:
    """
    Attributes:
        snapshot_name (Union[Unset, str]):
        snapshot_description (Union[Unset, str]):
        case_sensitive (Union[None, Unset, bool]):
        capabilities (Union[Unset, VolumeSyncFilesystemCapabilities]):
    """

    snapshot_name: Union[Unset, str] = UNSET
    snapshot_description: Union[Unset, str] = UNSET
    case_sensitive: Union[None, Unset, bool] = UNSET
    capabilities: Union[Unset, "VolumeSyncFilesystemCapabilities"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_name = self.snapshot_name

        snapshot_description = self.snapshot_description

        case_sensitive: Union[None, Unset, bool]
        if isinstance(self.case_sensitive, Unset):
            case_sensitive = UNSET
        else:
            case_sensitive = self.case_sensitive

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot_name is not UNSET:
            field_dict["snapshot_name"] = snapshot_name
        if snapshot_description is not UNSET:
            field_dict["snapshot_description"] = snapshot_description
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
        snapshot_name = d.pop("snapshot_name", UNSET)

        snapshot_description = d.pop("snapshot_description", UNSET)

        def _parse_case_sensitive(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        case_sensitive = _parse_case_sensitive(d.pop("case_sensitive", UNSET))

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, VolumeSyncFilesystemCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = VolumeSyncFilesystemCapabilities.from_dict(_capabilities)

        create_volume_sync_bootstrap_request = cls(
            snapshot_name=snapshot_name,
            snapshot_description=snapshot_description,
            case_sensitive=case_sensitive,
            capabilities=capabilities,
        )

        create_volume_sync_bootstrap_request.additional_properties = d
        return create_volume_sync_bootstrap_request

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
