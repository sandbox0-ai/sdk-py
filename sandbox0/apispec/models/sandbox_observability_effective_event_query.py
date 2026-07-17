from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_audit_execution_scope_attribution import (
    SandboxAuditExecutionScopeAttribution,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxObservabilityEffectiveEventQuery")


@_attrs_define
class SandboxObservabilityEffectiveEventQuery:
    """Normalized schema ceiling and execution-scope filters applied by the
    server. This metadata is returned even when no events match.

        Attributes:
            max_schema_version (int):
            execution_scope_namespace (Union[Unset, str]):
            execution_scope_kind (Union[Unset, str]):
            execution_scope_id (Union[Unset, str]):
            execution_scope_attribution (Union[Unset, SandboxAuditExecutionScopeAttribution]):
    """

    max_schema_version: int
    execution_scope_namespace: Union[Unset, str] = UNSET
    execution_scope_kind: Union[Unset, str] = UNSET
    execution_scope_id: Union[Unset, str] = UNSET
    execution_scope_attribution: Union[Unset, SandboxAuditExecutionScopeAttribution] = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_schema_version = self.max_schema_version

        execution_scope_namespace = self.execution_scope_namespace

        execution_scope_kind = self.execution_scope_kind

        execution_scope_id = self.execution_scope_id

        execution_scope_attribution: Union[Unset, str] = UNSET
        if not isinstance(self.execution_scope_attribution, Unset):
            execution_scope_attribution = self.execution_scope_attribution.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_schema_version": max_schema_version,
            }
        )
        if execution_scope_namespace is not UNSET:
            field_dict["execution_scope_namespace"] = execution_scope_namespace
        if execution_scope_kind is not UNSET:
            field_dict["execution_scope_kind"] = execution_scope_kind
        if execution_scope_id is not UNSET:
            field_dict["execution_scope_id"] = execution_scope_id
        if execution_scope_attribution is not UNSET:
            field_dict["execution_scope_attribution"] = execution_scope_attribution

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_schema_version = d.pop("max_schema_version")

        execution_scope_namespace = d.pop("execution_scope_namespace", UNSET)

        execution_scope_kind = d.pop("execution_scope_kind", UNSET)

        execution_scope_id = d.pop("execution_scope_id", UNSET)

        _execution_scope_attribution = d.pop("execution_scope_attribution", UNSET)
        execution_scope_attribution: Union[Unset, SandboxAuditExecutionScopeAttribution]
        if isinstance(_execution_scope_attribution, Unset):
            execution_scope_attribution = UNSET
        else:
            execution_scope_attribution = SandboxAuditExecutionScopeAttribution(
                _execution_scope_attribution
            )

        sandbox_observability_effective_event_query = cls(
            max_schema_version=max_schema_version,
            execution_scope_namespace=execution_scope_namespace,
            execution_scope_kind=execution_scope_kind,
            execution_scope_id=execution_scope_id,
            execution_scope_attribution=execution_scope_attribution,
        )

        sandbox_observability_effective_event_query.additional_properties = d
        return sandbox_observability_effective_event_query

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
