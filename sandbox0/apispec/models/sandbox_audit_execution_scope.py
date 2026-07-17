from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_audit_execution_scope_attribution import (
    SandboxAuditExecutionScopeAttribution,
)

T = TypeVar("T", bound="SandboxAuditExecutionScope")


@_attrs_define
class SandboxAuditExecutionScope:
    """Attributes sandbox workload activity to one native harness execution
    scope. The sandbox workload remains the audit actor.

        Attributes:
            namespace (str):
            kind (str):
            id (str):
            attribution (SandboxAuditExecutionScopeAttribution):
    """

    namespace: str
    kind: str
    id: str
    attribution: SandboxAuditExecutionScopeAttribution
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        namespace = self.namespace

        kind = self.kind

        id = self.id

        attribution = self.attribution.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespace": namespace,
                "kind": kind,
                "id": id,
                "attribution": attribution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        namespace = d.pop("namespace")

        kind = d.pop("kind")

        id = d.pop("id")

        attribution = SandboxAuditExecutionScopeAttribution(d.pop("attribution"))

        sandbox_audit_execution_scope = cls(
            namespace=namespace,
            kind=kind,
            id=id,
            attribution=attribution,
        )

        sandbox_audit_execution_scope.additional_properties = d
        return sandbox_audit_execution_scope

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
