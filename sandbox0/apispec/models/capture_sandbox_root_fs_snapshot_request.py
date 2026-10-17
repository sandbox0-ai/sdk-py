import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaptureSandboxRootFSSnapshotRequest")


@_attrs_define
class CaptureSandboxRootFSSnapshotRequest:
    """
    Attributes:
        expected_runtime_generation (int): Exact source runtime generation; retries bind the originally admitted
            generation.
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        expires_at (Union[Unset, datetime.datetime]):
    """

    expected_runtime_generation: int
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        expected_runtime_generation = self.expected_runtime_generation

        name = self.name

        description = self.description

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expected_runtime_generation": expected_runtime_generation,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        expected_runtime_generation = d.pop("expected_runtime_generation")

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)

        capture_sandbox_root_fs_snapshot_request = cls(
            expected_runtime_generation=expected_runtime_generation,
            name=name,
            description=description,
            expires_at=expires_at,
        )

        return capture_sandbox_root_fs_snapshot_request
