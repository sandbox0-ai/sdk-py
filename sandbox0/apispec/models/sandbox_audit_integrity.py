from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_audit_integrity_algorithm import SandboxAuditIntegrityAlgorithm
from ..models.sandbox_audit_integrity_signature_status import (
    SandboxAuditIntegritySignatureStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxAuditIntegrity")


@_attrs_define
class SandboxAuditIntegrity:
    """
    Attributes:
        algorithm (SandboxAuditIntegrityAlgorithm):
        payload_hash (str):
        signature (str):
        signing_key_id (str):
        signature_status (SandboxAuditIntegritySignatureStatus):
        event_id_conflict (Union[Unset, bool]): True when the query observed the same event ID with a different
            canonical payload hash.
    """

    algorithm: SandboxAuditIntegrityAlgorithm
    payload_hash: str
    signature: str
    signing_key_id: str
    signature_status: SandboxAuditIntegritySignatureStatus
    event_id_conflict: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        algorithm = self.algorithm.value

        payload_hash = self.payload_hash

        signature = self.signature

        signing_key_id = self.signing_key_id

        signature_status = self.signature_status.value

        event_id_conflict = self.event_id_conflict

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "algorithm": algorithm,
                "payload_hash": payload_hash,
                "signature": signature,
                "signing_key_id": signing_key_id,
                "signature_status": signature_status,
            }
        )
        if event_id_conflict is not UNSET:
            field_dict["event_id_conflict"] = event_id_conflict

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        algorithm = SandboxAuditIntegrityAlgorithm(d.pop("algorithm"))

        payload_hash = d.pop("payload_hash")

        signature = d.pop("signature")

        signing_key_id = d.pop("signing_key_id")

        signature_status = SandboxAuditIntegritySignatureStatus(
            d.pop("signature_status")
        )

        event_id_conflict = d.pop("event_id_conflict", UNSET)

        sandbox_audit_integrity = cls(
            algorithm=algorithm,
            payload_hash=payload_hash,
            signature=signature,
            signing_key_id=signing_key_id,
            signature_status=signature_status,
            event_id_conflict=event_id_conflict,
        )

        sandbox_audit_integrity.additional_properties = d
        return sandbox_audit_integrity

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
