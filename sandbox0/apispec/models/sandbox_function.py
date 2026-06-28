from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sandbox_function_runtime import SandboxFunctionRuntime
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_function_source import SandboxFunctionSource


T = TypeVar("T", bound="SandboxFunction")


@_attrs_define
class SandboxFunction:
    """Function code executed by procd for a sandbox service request. cluster-gateway owns public ingress and carries this
    source to procd.

        Attributes:
            runtime (SandboxFunctionRuntime): Function runtime. Only python is supported in this version.
            source (SandboxFunctionSource): Function source code stored in sandbox service config.
            handler (Union[Unset, str]): Python callable name. Defaults to handler.
            max_concurrency (Union[Unset, int]): Maximum in-flight executions for this function service inside one sandbox
                runtime. Omit or set to 0 for unlimited.
    """

    runtime: SandboxFunctionRuntime
    source: "SandboxFunctionSource"
    handler: Union[Unset, str] = UNSET
    max_concurrency: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runtime = self.runtime.value

        source = self.source.to_dict()

        handler = self.handler

        max_concurrency = self.max_concurrency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runtime": runtime,
                "source": source,
            }
        )
        if handler is not UNSET:
            field_dict["handler"] = handler
        if max_concurrency is not UNSET:
            field_dict["max_concurrency"] = max_concurrency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_function_source import SandboxFunctionSource

        d = dict(src_dict)
        runtime = SandboxFunctionRuntime(d.pop("runtime"))

        source = SandboxFunctionSource.from_dict(d.pop("source"))

        handler = d.pop("handler", UNSET)

        max_concurrency = d.pop("max_concurrency", UNSET)

        sandbox_function = cls(
            runtime=runtime,
            source=source,
            handler=handler,
            max_concurrency=max_concurrency,
        )

        sandbox_function.additional_properties = d
        return sandbox_function

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
