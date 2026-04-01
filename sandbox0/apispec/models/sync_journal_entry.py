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

from ..models.sync_event_type import SyncEventType
from ..models.sync_journal_entry_entry_kind import SyncJournalEntryEntryKind
from ..models.sync_journal_entry_source import SyncJournalEntrySource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_journal_entry_metadata_type_0 import (
        SyncJournalEntryMetadataType0,
    )


T = TypeVar("T", bound="SyncJournalEntry")


@_attrs_define
class SyncJournalEntry:
    """
    Attributes:
        seq (Union[Unset, int]):
        volume_id (Union[Unset, str]):
        team_id (Union[Unset, str]):
        source (Union[Unset, SyncJournalEntrySource]):
        replica_id (Union[None, Unset, str]):
        event_type (Union[Unset, SyncEventType]):
        path (Union[Unset, str]):
        normalized_path (Union[Unset, str]):
        old_path (Union[None, Unset, str]):
        normalized_old_path (Union[None, Unset, str]):
        tombstone (Union[Unset, bool]):
        entry_kind (Union[Unset, SyncJournalEntryEntryKind]):
        mode (Union[None, Unset, int]):
        content_ref (Union[None, Unset, str]):
        content_sha256 (Union[None, Unset, str]):
        size_bytes (Union[None, Unset, int]):
        metadata (Union['SyncJournalEntryMetadataType0', None, Unset]):
        created_at (Union[Unset, datetime.datetime]):
    """

    seq: Union[Unset, int] = UNSET
    volume_id: Union[Unset, str] = UNSET
    team_id: Union[Unset, str] = UNSET
    source: Union[Unset, SyncJournalEntrySource] = UNSET
    replica_id: Union[None, Unset, str] = UNSET
    event_type: Union[Unset, SyncEventType] = UNSET
    path: Union[Unset, str] = UNSET
    normalized_path: Union[Unset, str] = UNSET
    old_path: Union[None, Unset, str] = UNSET
    normalized_old_path: Union[None, Unset, str] = UNSET
    tombstone: Union[Unset, bool] = UNSET
    entry_kind: Union[Unset, SyncJournalEntryEntryKind] = UNSET
    mode: Union[None, Unset, int] = UNSET
    content_ref: Union[None, Unset, str] = UNSET
    content_sha256: Union[None, Unset, str] = UNSET
    size_bytes: Union[None, Unset, int] = UNSET
    metadata: Union["SyncJournalEntryMetadataType0", None, Unset] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_journal_entry_metadata_type_0 import (
            SyncJournalEntryMetadataType0,
        )

        seq = self.seq

        volume_id = self.volume_id

        team_id = self.team_id

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        replica_id: Union[None, Unset, str]
        if isinstance(self.replica_id, Unset):
            replica_id = UNSET
        else:
            replica_id = self.replica_id

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        path = self.path

        normalized_path = self.normalized_path

        old_path: Union[None, Unset, str]
        if isinstance(self.old_path, Unset):
            old_path = UNSET
        else:
            old_path = self.old_path

        normalized_old_path: Union[None, Unset, str]
        if isinstance(self.normalized_old_path, Unset):
            normalized_old_path = UNSET
        else:
            normalized_old_path = self.normalized_old_path

        tombstone = self.tombstone

        entry_kind: Union[Unset, str] = UNSET
        if not isinstance(self.entry_kind, Unset):
            entry_kind = self.entry_kind.value

        mode: Union[None, Unset, int]
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        content_ref: Union[None, Unset, str]
        if isinstance(self.content_ref, Unset):
            content_ref = UNSET
        else:
            content_ref = self.content_ref

        content_sha256: Union[None, Unset, str]
        if isinstance(self.content_sha256, Unset):
            content_sha256 = UNSET
        else:
            content_sha256 = self.content_sha256

        size_bytes: Union[None, Unset, int]
        if isinstance(self.size_bytes, Unset):
            size_bytes = UNSET
        else:
            size_bytes = self.size_bytes

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, SyncJournalEntryMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if seq is not UNSET:
            field_dict["seq"] = seq
        if volume_id is not UNSET:
            field_dict["volume_id"] = volume_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if source is not UNSET:
            field_dict["source"] = source
        if replica_id is not UNSET:
            field_dict["replica_id"] = replica_id
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if path is not UNSET:
            field_dict["path"] = path
        if normalized_path is not UNSET:
            field_dict["normalized_path"] = normalized_path
        if old_path is not UNSET:
            field_dict["old_path"] = old_path
        if normalized_old_path is not UNSET:
            field_dict["normalized_old_path"] = normalized_old_path
        if tombstone is not UNSET:
            field_dict["tombstone"] = tombstone
        if entry_kind is not UNSET:
            field_dict["entry_kind"] = entry_kind
        if mode is not UNSET:
            field_dict["mode"] = mode
        if content_ref is not UNSET:
            field_dict["content_ref"] = content_ref
        if content_sha256 is not UNSET:
            field_dict["content_sha256"] = content_sha256
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_journal_entry_metadata_type_0 import (
            SyncJournalEntryMetadataType0,
        )

        d = dict(src_dict)
        seq = d.pop("seq", UNSET)

        volume_id = d.pop("volume_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, SyncJournalEntrySource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = SyncJournalEntrySource(_source)

        def _parse_replica_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        replica_id = _parse_replica_id(d.pop("replica_id", UNSET))

        _event_type = d.pop("event_type", UNSET)
        event_type: Union[Unset, SyncEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = SyncEventType(_event_type)

        path = d.pop("path", UNSET)

        normalized_path = d.pop("normalized_path", UNSET)

        def _parse_old_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        old_path = _parse_old_path(d.pop("old_path", UNSET))

        def _parse_normalized_old_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        normalized_old_path = _parse_normalized_old_path(
            d.pop("normalized_old_path", UNSET)
        )

        tombstone = d.pop("tombstone", UNSET)

        _entry_kind = d.pop("entry_kind", UNSET)
        entry_kind: Union[Unset, SyncJournalEntryEntryKind]
        if isinstance(_entry_kind, Unset):
            entry_kind = UNSET
        else:
            entry_kind = SyncJournalEntryEntryKind(_entry_kind)

        def _parse_mode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_content_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_ref = _parse_content_ref(d.pop("content_ref", UNSET))

        def _parse_content_sha256(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_sha256 = _parse_content_sha256(d.pop("content_sha256", UNSET))

        def _parse_size_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size_bytes = _parse_size_bytes(d.pop("size_bytes", UNSET))

        def _parse_metadata(
            data: object,
        ) -> Union["SyncJournalEntryMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = SyncJournalEntryMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SyncJournalEntryMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        sync_journal_entry = cls(
            seq=seq,
            volume_id=volume_id,
            team_id=team_id,
            source=source,
            replica_id=replica_id,
            event_type=event_type,
            path=path,
            normalized_path=normalized_path,
            old_path=old_path,
            normalized_old_path=normalized_old_path,
            tombstone=tombstone,
            entry_kind=entry_kind,
            mode=mode,
            content_ref=content_ref,
            content_sha256=content_sha256,
            size_bytes=size_bytes,
            metadata=metadata,
            created_at=created_at,
        )

        sync_journal_entry.additional_properties = d
        return sync_journal_entry

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
