from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_revision_mount_source_type import FunctionRevisionMountSourceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionRevisionMountSource")


@_attrs_define
class FunctionRevisionMountSource:
    """
    Attributes:
        type_ (FunctionRevisionMountSourceType):
        sandboxvolume_id (Union[Unset, str]): Prepared SandboxVolume ID available to the runtime claim path.
        source_sandboxvolume_id (Union[Unset, str]): Source SandboxVolume captured by a sandbox-service publish.
        snapshot_id (Union[Unset, str]): Immutable snapshot used to materialize this mount.
        artifact_id (Union[Unset, str]): Future first-class Function artifact ID.
        digest (Union[Unset, str]): Content digest for artifact-backed sources.
    """

    type_: FunctionRevisionMountSourceType
    sandboxvolume_id: Union[Unset, str] = UNSET
    source_sandboxvolume_id: Union[Unset, str] = UNSET
    snapshot_id: Union[Unset, str] = UNSET
    artifact_id: Union[Unset, str] = UNSET
    digest: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        sandboxvolume_id = self.sandboxvolume_id

        source_sandboxvolume_id = self.source_sandboxvolume_id

        snapshot_id = self.snapshot_id

        artifact_id = self.artifact_id

        digest = self.digest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if sandboxvolume_id is not UNSET:
            field_dict["sandboxvolume_id"] = sandboxvolume_id
        if source_sandboxvolume_id is not UNSET:
            field_dict["source_sandboxvolume_id"] = source_sandboxvolume_id
        if snapshot_id is not UNSET:
            field_dict["snapshot_id"] = snapshot_id
        if artifact_id is not UNSET:
            field_dict["artifact_id"] = artifact_id
        if digest is not UNSET:
            field_dict["digest"] = digest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = FunctionRevisionMountSourceType(d.pop("type"))

        sandboxvolume_id = d.pop("sandboxvolume_id", UNSET)

        source_sandboxvolume_id = d.pop("source_sandboxvolume_id", UNSET)

        snapshot_id = d.pop("snapshot_id", UNSET)

        artifact_id = d.pop("artifact_id", UNSET)

        digest = d.pop("digest", UNSET)

        function_revision_mount_source = cls(
            type_=type_,
            sandboxvolume_id=sandboxvolume_id,
            source_sandboxvolume_id=source_sandboxvolume_id,
            snapshot_id=snapshot_id,
            artifact_id=artifact_id,
            digest=digest,
        )

        function_revision_mount_source.additional_properties = d
        return function_revision_mount_source

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
