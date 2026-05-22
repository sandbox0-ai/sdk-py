from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_revision_input_source_type import FunctionRevisionInputSourceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.function_revision_spec import FunctionRevisionSpec
    from ..models.function_sandbox_service_source import FunctionSandboxServiceSource
    from ..models.function_source_request_provenance import (
        FunctionSourceRequestProvenance,
    )


T = TypeVar("T", bound="FunctionSourceRequest")


@_attrs_define
class FunctionSourceRequest:
    """Source used to create a function revision. Omitting type with sandbox_id and service_id keeps the sandbox-service
    shortcut shape; internally it is compiled into an immutable FunctionRevisionSpec.

        Attributes:
            type_ (Union[Unset, FunctionRevisionInputSourceType]):
            sandbox_id (Union[Unset, str]): Compatibility shortcut for type=sandbox_service.
            service_id (Union[Unset, str]): Compatibility shortcut for type=sandbox_service.
            sandbox_service (Union[Unset, FunctionSandboxServiceSource]):
            revision_spec (Union[Unset, FunctionRevisionSpec]): Immutable execution contract used by Function Gateway to
                serve a revision.
            provenance (Union[Unset, FunctionSourceRequestProvenance]): Optional non-execution metadata describing how the
                revision spec was produced.
    """

    type_: Union[Unset, FunctionRevisionInputSourceType] = UNSET
    sandbox_id: Union[Unset, str] = UNSET
    service_id: Union[Unset, str] = UNSET
    sandbox_service: Union[Unset, "FunctionSandboxServiceSource"] = UNSET
    revision_spec: Union[Unset, "FunctionRevisionSpec"] = UNSET
    provenance: Union[Unset, "FunctionSourceRequestProvenance"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        sandbox_id = self.sandbox_id

        service_id = self.service_id

        sandbox_service: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sandbox_service, Unset):
            sandbox_service = self.sandbox_service.to_dict()

        revision_spec: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.revision_spec, Unset):
            revision_spec = self.revision_spec.to_dict()

        provenance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.provenance, Unset):
            provenance = self.provenance.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if service_id is not UNSET:
            field_dict["service_id"] = service_id
        if sandbox_service is not UNSET:
            field_dict["sandbox_service"] = sandbox_service
        if revision_spec is not UNSET:
            field_dict["revision_spec"] = revision_spec
        if provenance is not UNSET:
            field_dict["provenance"] = provenance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_revision_spec import FunctionRevisionSpec
        from ..models.function_sandbox_service_source import (
            FunctionSandboxServiceSource,
        )
        from ..models.function_source_request_provenance import (
            FunctionSourceRequestProvenance,
        )

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FunctionRevisionInputSourceType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = FunctionRevisionInputSourceType(_type_)

        sandbox_id = d.pop("sandbox_id", UNSET)

        service_id = d.pop("service_id", UNSET)

        _sandbox_service = d.pop("sandbox_service", UNSET)
        sandbox_service: Union[Unset, FunctionSandboxServiceSource]
        if isinstance(_sandbox_service, Unset):
            sandbox_service = UNSET
        else:
            sandbox_service = FunctionSandboxServiceSource.from_dict(_sandbox_service)

        _revision_spec = d.pop("revision_spec", UNSET)
        revision_spec: Union[Unset, FunctionRevisionSpec]
        if isinstance(_revision_spec, Unset):
            revision_spec = UNSET
        else:
            revision_spec = FunctionRevisionSpec.from_dict(_revision_spec)

        _provenance = d.pop("provenance", UNSET)
        provenance: Union[Unset, FunctionSourceRequestProvenance]
        if isinstance(_provenance, Unset):
            provenance = UNSET
        else:
            provenance = FunctionSourceRequestProvenance.from_dict(_provenance)

        function_source_request = cls(
            type_=type_,
            sandbox_id=sandbox_id,
            service_id=service_id,
            sandbox_service=sandbox_service,
            revision_spec=revision_spec,
            provenance=provenance,
        )

        function_source_request.additional_properties = d
        return function_source_request

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
