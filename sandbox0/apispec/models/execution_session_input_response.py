from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExecutionSessionInputResponse")


@_attrs_define
class ExecutionSessionInputResponse:
    """
    Attributes:
        input_id (str):
        attempt_id (str):
        accepted (bool):
        duplicate (bool):
    """

    input_id: str
    attempt_id: str
    accepted: bool
    duplicate: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_id = self.input_id

        attempt_id = self.attempt_id

        accepted = self.accepted

        duplicate = self.duplicate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input_id": input_id,
                "attempt_id": attempt_id,
                "accepted": accepted,
                "duplicate": duplicate,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_id = d.pop("input_id")

        attempt_id = d.pop("attempt_id")

        accepted = d.pop("accepted")

        duplicate = d.pop("duplicate")

        execution_session_input_response = cls(
            input_id=input_id,
            attempt_id=attempt_id,
            accepted=accepted,
            duplicate=duplicate,
        )

        execution_session_input_response.additional_properties = d
        return execution_session_input_response

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
