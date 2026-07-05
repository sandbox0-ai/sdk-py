from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volume_access_mode import VolumeAccessMode
from ..models.volume_backend import VolumeBackend
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_sandbox_volume_s3_config import CreateSandboxVolumeS3Config


T = TypeVar("T", bound="CreateSandboxVolumeRequest")


@_attrs_define
class CreateSandboxVolumeRequest:
    """
    Attributes:
        snapshot_id (Union[Unset, str]): Optional snapshot ID used to initialize the new volume from immutable snapshot
            state.
        backend (Union[Unset, VolumeBackend]): Storage backend for a SandboxVolume. s0fs is the default durable Sandbox0
            volume backend. s3 mounts an existing S3-compatible prefix through the volume portal and supports mount-s3-like
            object projection.
        s3 (Union[Unset, CreateSandboxVolumeS3Config]):
        default_posix_uid (Union[Unset, int]): Default POSIX UID used by external volume access paths that do not carry
            caller identity. Defaults to 0 when omitted on create. Default: 0.
        default_posix_gid (Union[Unset, int]): Default POSIX GID used by external volume access paths that do not carry
            caller identity. Defaults to 0 when omitted on create. Default: 0.
        access_mode (Union[Unset, VolumeAccessMode]): Access mode for sandbox volumes. Enforcement is scoped to storage-
            proxy instances. RWO allows read-write mounts on a single instance; ROX allows read-only mounts across
            instances; RWX allows read-write mounts across instances.
    """

    snapshot_id: Union[Unset, str] = UNSET
    backend: Union[Unset, VolumeBackend] = UNSET
    s3: Union[Unset, "CreateSandboxVolumeS3Config"] = UNSET
    default_posix_uid: Union[Unset, int] = 0
    default_posix_gid: Union[Unset, int] = 0
    access_mode: Union[Unset, VolumeAccessMode] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot_id = self.snapshot_id

        backend: Union[Unset, str] = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.value

        s3: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        default_posix_uid = self.default_posix_uid

        default_posix_gid = self.default_posix_gid

        access_mode: Union[Unset, str] = UNSET
        if not isinstance(self.access_mode, Unset):
            access_mode = self.access_mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if backend is not UNSET:
            field_dict["backend"] = backend
        if s3 is not UNSET:
            field_dict["s3"] = s3
        if default_posix_uid is not UNSET:
            field_dict["default_posix_uid"] = default_posix_uid
        if default_posix_gid is not UNSET:
            field_dict["default_posix_gid"] = default_posix_gid
        if access_mode is not UNSET:
            field_dict["access_mode"] = access_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_sandbox_volume_s3_config import CreateSandboxVolumeS3Config

        d = dict(src_dict)
        snapshot_id = d.pop("snapshot_id", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: Union[Unset, VolumeBackend]
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = VolumeBackend(_backend)

        _s3 = d.pop("s3", UNSET)
        s3: Union[Unset, CreateSandboxVolumeS3Config]
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = CreateSandboxVolumeS3Config.from_dict(_s3)

        default_posix_uid = d.pop("default_posix_uid", UNSET)

        default_posix_gid = d.pop("default_posix_gid", UNSET)

        _access_mode = d.pop("access_mode", UNSET)
        access_mode: Union[Unset, VolumeAccessMode]
        if isinstance(_access_mode, Unset):
            access_mode = UNSET
        else:
            access_mode = VolumeAccessMode(_access_mode)

        create_sandbox_volume_request = cls(
            snapshot_id=snapshot_id,
            backend=backend,
            s3=s3,
            default_posix_uid=default_posix_uid,
            default_posix_gid=default_posix_gid,
            access_mode=access_mode,
        )

        create_sandbox_volume_request.additional_properties = d
        return create_sandbox_volume_request

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
