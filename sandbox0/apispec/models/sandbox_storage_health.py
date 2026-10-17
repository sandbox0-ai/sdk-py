from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.sandbox_health_observation import SandboxHealthObservation


T = TypeVar("T", bound="SandboxStorageHealth")


@_attrs_define
class SandboxStorageHealth:
    """
    Attributes:
        identity (SandboxHealthObservation):
        writer_authority (SandboxHealthObservation):
        io (SandboxHealthObservation):
    """

    identity: "SandboxHealthObservation"
    writer_authority: "SandboxHealthObservation"
    io: "SandboxHealthObservation"

    def to_dict(self) -> dict[str, Any]:
        identity = self.identity.to_dict()

        writer_authority = self.writer_authority.to_dict()

        io = self.io.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "identity": identity,
                "writer_authority": writer_authority,
                "io": io,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_health_observation import SandboxHealthObservation

        d = dict(src_dict)
        identity = SandboxHealthObservation.from_dict(d.pop("identity"))

        writer_authority = SandboxHealthObservation.from_dict(d.pop("writer_authority"))

        io = SandboxHealthObservation.from_dict(d.pop("io"))

        sandbox_storage_health = cls(
            identity=identity,
            writer_authority=writer_authority,
            io=io,
        )

        return sandbox_storage_health
