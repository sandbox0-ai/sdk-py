from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sandbox import Sandbox


T = TypeVar("T", bound="ForkSandboxResponse")


@_attrs_define
class ForkSandboxResponse:
    """
    Attributes:
        source_sandbox_id (str):
        sandbox (Sandbox):
    """

    source_sandbox_id: str
    sandbox: "Sandbox"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_sandbox_id = self.source_sandbox_id

        sandbox = self.sandbox.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_sandbox_id": source_sandbox_id,
                "sandbox": sandbox,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox import Sandbox

        d = dict(src_dict)
        source_sandbox_id = d.pop("source_sandbox_id")

        sandbox = Sandbox.from_dict(d.pop("sandbox"))

        fork_sandbox_response = cls(
            source_sandbox_id=source_sandbox_id,
            sandbox=sandbox,
        )

        fork_sandbox_response.additional_properties = d
        return fork_sandbox_response

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
