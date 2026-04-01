from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.snapshot import Snapshot


T = TypeVar("T", bound="VolumeSyncBootstrap")


@_attrs_define
class VolumeSyncBootstrap:
    """
    Attributes:
        snapshot (Snapshot):
        replay_after_seq (int):
        archive_download_path (str):
    """

    snapshot: "Snapshot"
    replay_after_seq: int
    archive_download_path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snapshot = self.snapshot.to_dict()

        replay_after_seq = self.replay_after_seq

        archive_download_path = self.archive_download_path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snapshot": snapshot,
                "replay_after_seq": replay_after_seq,
                "archive_download_path": archive_download_path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snapshot import Snapshot

        d = dict(src_dict)
        snapshot = Snapshot.from_dict(d.pop("snapshot"))

        replay_after_seq = d.pop("replay_after_seq")

        archive_download_path = d.pop("archive_download_path")

        volume_sync_bootstrap = cls(
            snapshot=snapshot,
            replay_after_seq=replay_after_seq,
            archive_download_path=archive_download_path,
        )

        volume_sync_bootstrap.additional_properties = d
        return volume_sync_bootstrap

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
