from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sync_replica import SyncReplica


T = TypeVar("T", bound="VolumeSyncReplicaEnvelope")


@_attrs_define
class VolumeSyncReplicaEnvelope:
    """
    Attributes:
        replica (SyncReplica):
        head_seq (int):
    """

    replica: "SyncReplica"
    head_seq: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replica = self.replica.to_dict()

        head_seq = self.head_seq

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "replica": replica,
                "head_seq": head_seq,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_replica import SyncReplica

        d = dict(src_dict)
        replica = SyncReplica.from_dict(d.pop("replica"))

        head_seq = d.pop("head_seq")

        volume_sync_replica_envelope = cls(
            replica=replica,
            head_seq=head_seq,
        )

        volume_sync_replica_envelope.additional_properties = d
        return volume_sync_replica_envelope

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
