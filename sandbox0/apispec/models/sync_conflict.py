import datetime
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
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_conflict_metadata_type_0 import SyncConflictMetadataType0


T = TypeVar("T", bound="SyncConflict")


@_attrs_define
class SyncConflict:
    """
    Attributes:
        id (Union[Unset, str]):
        volume_id (Union[Unset, str]):
        team_id (Union[Unset, str]):
        replica_id (Union[None, Unset, str]):
        path (Union[Unset, str]):
        normalized_path (Union[Unset, str]):
        artifact_path (Union[Unset, str]):
        incoming_path (Union[None, Unset, str]):
        incoming_old_path (Union[None, Unset, str]):
        existing_seq (Union[None, Unset, int]):
        reason (Union[Unset, str]):
        status (Union[Unset, str]):
        metadata (Union['SyncConflictMetadataType0', None, Unset]):
        created_at (Union[Unset, datetime.datetime]):
        updated_at (Union[Unset, datetime.datetime]):
    """

    id: Union[Unset, str] = UNSET
    volume_id: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    replica_id: Union[None, Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    normalized_path: Union[Unset, str] = UNSET
    artifact_path: Union[Unset, str] = UNSET
    incoming_path: Union[None, Unset, str] = UNSET
    incoming_old_path: Union[None, Unset, str] = UNSET
    existing_seq: Union[None, Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    metadata: Union["SyncConflictMetadataType0", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_conflict_metadata_type_0 import SyncConflictMetadataType0

        id = self.id

        volume_id = self.volume_id

        team_id = self.team_id

        replica_id: Union[None, Unset, str]
        if isinstance(self.replica_id, Unset):
            replica_id = UNSET
        else:
            replica_id = self.replica_id

        path = self.path

        normalized_path = self.normalized_path

        artifact_path = self.artifact_path

        incoming_path: Union[None, Unset, str]
        if isinstance(self.incoming_path, Unset):
            incoming_path = UNSET
        else:
            incoming_path = self.incoming_path

        incoming_old_path: Union[None, Unset, str]
        if isinstance(self.incoming_old_path, Unset):
            incoming_old_path = UNSET
        else:
            incoming_old_path = self.incoming_old_path

        existing_seq: Union[None, Unset, int]
        if isinstance(self.existing_seq, Unset):
            existing_seq = UNSET
        else:
            existing_seq = self.existing_seq

        reason = self.reason

        status = self.status

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SyncConflictMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

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
        if replica_id is not UNSET:
            field_dict["replica_id"] = replica_id
        if path is not UNSET:
            field_dict["path"] = path
        if normalized_path is not UNSET:
            field_dict["normalized_path"] = normalized_path
        if artifact_path is not UNSET:
            field_dict["artifact_path"] = artifact_path
        if incoming_path is not UNSET:
            field_dict["incoming_path"] = incoming_path
        if incoming_old_path is not UNSET:
            field_dict["incoming_old_path"] = incoming_old_path
        if existing_seq is not UNSET:
            field_dict["existing_seq"] = existing_seq
        if reason is not UNSET:
            field_dict["reason"] = reason
        if status is not UNSET:
            field_dict["status"] = status
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_conflict_metadata_type_0 import SyncConflictMetadataType0

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        volume_id = d.pop("volume_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        def _parse_replica_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        replica_id = _parse_replica_id(d.pop("replica_id", UNSET))

        path = d.pop("path", UNSET)

        normalized_path = d.pop("normalized_path", UNSET)

        artifact_path = d.pop("artifact_path", UNSET)

        def _parse_incoming_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        incoming_path = _parse_incoming_path(d.pop("incoming_path", UNSET))

        def _parse_incoming_old_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        incoming_old_path = _parse_incoming_old_path(d.pop("incoming_old_path", UNSET))

        def _parse_existing_seq(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        existing_seq = _parse_existing_seq(d.pop("existing_seq", UNSET))

        reason = d.pop("reason", UNSET)

        status = d.pop("status", UNSET)

        def _parse_metadata(
            data: object,
        ) -> Union["SyncConflictMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SyncConflictMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SyncConflictMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

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

        sync_conflict = cls(
            id=id,
            volume_id=volume_id,
            team_id=team_id,
            replica_id=replica_id,
            path=path,
            normalized_path=normalized_path,
            artifact_path=artifact_path,
            incoming_path=incoming_path,
            incoming_old_path=incoming_old_path,
            existing_seq=existing_seq,
            reason=reason,
            status=status,
            metadata=metadata,
            created_at=created_at,
            updated_at=updated_at,
        )

        sync_conflict.additional_properties = d
        return sync_conflict

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
