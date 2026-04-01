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

from ..models.change_request_entry_kind import ChangeRequestEntryKind
from ..models.sync_event_type import SyncEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.change_request_metadata import ChangeRequestMetadata


T = TypeVar("T", bound="ChangeRequest")


@_attrs_define
class ChangeRequest:
    """
    Attributes:
        event_type (SyncEventType):
        path (Union[Unset, str]):
        old_path (Union[Unset, str]):
        entry_kind (Union[Unset, ChangeRequestEntryKind]):
        content_base64 (Union[None, Unset, str]):
        mode (Union[None, Unset, int]):
        content_sha256 (Union[Unset, str]):
        size_bytes (Union[Unset, int]):
        metadata (Union[Unset, ChangeRequestMetadata]):
    """

    event_type: SyncEventType
    path: Union[Unset, str] = UNSET
    old_path: Union[Unset, str] = UNSET
    entry_kind: Union[Unset, ChangeRequestEntryKind] = UNSET
    content_base64: Union[None, Unset, str] = UNSET
    mode: Union[None, Unset, int] = UNSET
    content_sha256: Union[Unset, str] = UNSET
    size_bytes: Union[Unset, int] = UNSET
    metadata: Union[Unset, "ChangeRequestMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type.value

        path = self.path

        old_path = self.old_path

        entry_kind: Union[Unset, str] = UNSET
        if not isinstance(self.entry_kind, Unset):
            entry_kind = self.entry_kind.value

        content_base64: Union[None, Unset, str]
        if isinstance(self.content_base64, Unset):
            content_base64 = UNSET
        else:
            content_base64 = self.content_base64

        mode: Union[None, Unset, int]
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        content_sha256 = self.content_sha256

        size_bytes = self.size_bytes

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
            }
        )
        if path is not UNSET:
            field_dict["path"] = path
        if old_path is not UNSET:
            field_dict["old_path"] = old_path
        if entry_kind is not UNSET:
            field_dict["entry_kind"] = entry_kind
        if content_base64 is not UNSET:
            field_dict["content_base64"] = content_base64
        if mode is not UNSET:
            field_dict["mode"] = mode
        if content_sha256 is not UNSET:
            field_dict["content_sha256"] = content_sha256
        if size_bytes is not UNSET:
            field_dict["size_bytes"] = size_bytes
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_request_metadata import ChangeRequestMetadata

        d = dict(src_dict)
        event_type = SyncEventType(d.pop("event_type"))

        path = d.pop("path", UNSET)

        old_path = d.pop("old_path", UNSET)

        _entry_kind = d.pop("entry_kind", UNSET)
        entry_kind: Union[Unset, ChangeRequestEntryKind]
        if isinstance(_entry_kind, Unset):
            entry_kind = UNSET
        else:
            entry_kind = ChangeRequestEntryKind(_entry_kind)

        def _parse_content_base64(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content_base64 = _parse_content_base64(d.pop("content_base64", UNSET))

        def _parse_mode(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        mode = _parse_mode(d.pop("mode", UNSET))

        content_sha256 = d.pop("content_sha256", UNSET)

        size_bytes = d.pop("size_bytes", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ChangeRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ChangeRequestMetadata.from_dict(_metadata)

        change_request = cls(
            event_type=event_type,
            path=path,
            old_path=old_path,
            entry_kind=entry_kind,
            content_base64=content_base64,
            mode=mode,
            content_sha256=content_sha256,
            size_bytes=size_bytes,
            metadata=metadata,
        )

        change_request.additional_properties = d
        return change_request

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
