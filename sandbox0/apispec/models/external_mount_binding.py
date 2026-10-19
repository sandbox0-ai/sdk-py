from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define

from ..models.external_mount_binding_access import ExternalMountBindingAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalMountBinding")


@_attrs_define
class ExternalMountBinding:
    """Credential-free binding to a team-owned S3 source. Bucket, endpoint and credentials come from the source and are
    never supplied here or exposed to the guest. At attachment the mount target must be an empty directory without
    symlink aliases.

        Attributes:
            source_ref (str): Name of an enabled static_s3 source owned by the authenticated team. No whitespace at either
                end, slash, backslash, NUL or line breaks.
            mount_path (str): Canonical absolute guest directory, at most 4096 UTF-8 bytes. No root, dot components,
                duplicate slashes, backslash, NUL or line breaks. Must not overlap other mounts, template tmpfs mounts or
                platform-owned paths such as /tmp, /proc, /sys, /dev, /config and /run/sandbox0.
            prefix (Union[Unset, str]): Optional canonical relative directory prefix ending in a slash, appended to the
                source prefix to narrow its scope. The combined S3 key must fit 1024 UTF-8 bytes.
            access (Union[Unset, ExternalMountBindingAccess]): read_write additionally requires allowWrite on the source.
                Omission never grants write access. Default: ExternalMountBindingAccess.READ_ONLY.
    """

    source_ref: str
    mount_path: str
    prefix: Union[Unset, str] = UNSET
    access: Union[Unset, ExternalMountBindingAccess] = (
        ExternalMountBindingAccess.READ_ONLY
    )

    def to_dict(self) -> dict[str, Any]:
        source_ref = self.source_ref

        mount_path = self.mount_path

        prefix = self.prefix

        access: Union[Unset, str] = UNSET
        if not isinstance(self.access, Unset):
            access = self.access.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source_ref": source_ref,
                "mount_path": mount_path,
            }
        )
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if access is not UNSET:
            field_dict["access"] = access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_ref = d.pop("source_ref")

        mount_path = d.pop("mount_path")

        prefix = d.pop("prefix", UNSET)

        _access = d.pop("access", UNSET)
        access: Union[Unset, ExternalMountBindingAccess]
        if isinstance(_access, Unset):
            access = UNSET
        else:
            access = ExternalMountBindingAccess(_access)

        external_mount_binding = cls(
            source_ref=source_ref,
            mount_path=mount_path,
            prefix=prefix,
            access=access,
        )

        return external_mount_binding
