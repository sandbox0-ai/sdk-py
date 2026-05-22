from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.function_runtime_status import FunctionRuntimeStatus


T = TypeVar("T", bound="SuccessFunctionRuntimeResponseData")


@_attrs_define
class SuccessFunctionRuntimeResponseData:
    """
    Attributes:
        runtime (FunctionRuntimeStatus):
    """

    runtime: "FunctionRuntimeStatus"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime = self.runtime.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runtime": runtime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_runtime_status import FunctionRuntimeStatus

        d = dict(src_dict)
        runtime = FunctionRuntimeStatus.from_dict(d.pop("runtime"))

        success_function_runtime_response_data = cls(
            runtime=runtime,
        )

        success_function_runtime_response_data.additional_properties = d
        return success_function_runtime_response_data

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
