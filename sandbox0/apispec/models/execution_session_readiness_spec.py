from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_session_readiness_type import ExecutionSessionReadinessType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionReadinessSpec")


@_attrs_define
class ExecutionSessionReadinessSpec:
    """
    Attributes:
        type_ (Union[Unset, ExecutionSessionReadinessType]):
        delay_ms (Union[Unset, int]):
        output (Union[Unset, str]): Byte sequence whose appearance in process output marks the attempt ready when type
            is output.
        timeout_ms (Union[Unset, int]):  Default: 30000.
    """

    type_: Union[Unset, ExecutionSessionReadinessType] = UNSET
    delay_ms: Union[Unset, int] = UNSET
    output: Union[Unset, str] = UNSET
    timeout_ms: Union[Unset, int] = 30000
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        delay_ms = self.delay_ms

        output = self.output

        timeout_ms = self.timeout_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if delay_ms is not UNSET:
            field_dict["delay_ms"] = delay_ms
        if output is not UNSET:
            field_dict["output"] = output
        if timeout_ms is not UNSET:
            field_dict["timeout_ms"] = timeout_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ExecutionSessionReadinessType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ExecutionSessionReadinessType(_type_)

        delay_ms = d.pop("delay_ms", UNSET)

        output = d.pop("output", UNSET)

        timeout_ms = d.pop("timeout_ms", UNSET)

        execution_session_readiness_spec = cls(
            type_=type_,
            delay_ms=delay_ms,
            output=output,
            timeout_ms=timeout_ms,
        )

        execution_session_readiness_spec.additional_properties = d
        return execution_session_readiness_spec

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
