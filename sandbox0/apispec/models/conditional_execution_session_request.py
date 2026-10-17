from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.execution_session_spec import ExecutionSessionSpec


T = TypeVar("T", bound="ConditionalExecutionSessionRequest")


@_attrs_define
class ConditionalExecutionSessionRequest:
    """
    Attributes:
        sandbox_id (str): Must equal the sandbox path identity and active supervisor owner.
        runtime_generation (int): Exact current runtime generation; never interpreted as a minimum.
        spec (ExecutionSessionSpec): Generic process-backed session specification. The supervisor does not interpret
            application protocols.
    """

    sandbox_id: str
    runtime_generation: int
    spec: "ExecutionSessionSpec"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        runtime_generation = self.runtime_generation

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "runtime_generation": runtime_generation,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_spec import ExecutionSessionSpec

        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        runtime_generation = d.pop("runtime_generation")

        spec = ExecutionSessionSpec.from_dict(d.pop("spec"))

        conditional_execution_session_request = cls(
            sandbox_id=sandbox_id,
            runtime_generation=runtime_generation,
            spec=spec,
        )

        conditional_execution_session_request.additional_properties = d
        return conditional_execution_session_request

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
