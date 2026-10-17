from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResumeSandboxResponse")


@_attrs_define
class ResumeSandboxResponse:
    """
    Attributes:
        sandbox_id (str):
        resumed (bool): True after the requested runtime has committed. Memory restoration never implicitly starts
            filesystem-only replacement processes.
        operation_id (Union[Unset, str]): Authenticated caller request for this conditional memory restore, distinct
            from the capture operation and internal worker lifecycle.
        checkpoint_id (Union[Unset, str]): Exact retained capture restored by this conditional request.
        from_runtime_generation (Union[Unset, int]): Source generation bound by this conditional request.
        runtime_generation (Union[Unset, int]): Committed restored runtime generation, exactly one greater than
            from_runtime_generation. These conditional result coordinates are not a current process or storage health
            attestation.
        restored_memory (Union[Unset, str]):
    """

    sandbox_id: str
    resumed: bool
    operation_id: Union[Unset, str] = UNSET
    checkpoint_id: Union[Unset, str] = UNSET
    from_runtime_generation: Union[Unset, int] = UNSET
    runtime_generation: Union[Unset, int] = UNSET
    restored_memory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        resumed = self.resumed

        operation_id = self.operation_id

        checkpoint_id = self.checkpoint_id

        from_runtime_generation = self.from_runtime_generation

        runtime_generation = self.runtime_generation

        restored_memory = self.restored_memory

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "resumed": resumed,
            }
        )
        if operation_id is not UNSET:
            field_dict["operation_id"] = operation_id
        if checkpoint_id is not UNSET:
            field_dict["checkpoint_id"] = checkpoint_id
        if from_runtime_generation is not UNSET:
            field_dict["from_runtime_generation"] = from_runtime_generation
        if runtime_generation is not UNSET:
            field_dict["runtime_generation"] = runtime_generation
        if restored_memory is not UNSET:
            field_dict["restored_memory"] = restored_memory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        resumed = d.pop("resumed")

        operation_id = d.pop("operation_id", UNSET)

        checkpoint_id = d.pop("checkpoint_id", UNSET)

        from_runtime_generation = d.pop("from_runtime_generation", UNSET)

        runtime_generation = d.pop("runtime_generation", UNSET)

        restored_memory = d.pop("restored_memory", UNSET)

        resume_sandbox_response = cls(
            sandbox_id=sandbox_id,
            resumed=resumed,
            operation_id=operation_id,
            checkpoint_id=checkpoint_id,
            from_runtime_generation=from_runtime_generation,
            runtime_generation=runtime_generation,
            restored_memory=restored_memory,
        )

        resume_sandbox_response.additional_properties = d
        return resume_sandbox_response

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
