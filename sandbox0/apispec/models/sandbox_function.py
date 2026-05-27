from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.sandbox_function_runtime import SandboxFunctionRuntime
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sandbox_function_source import SandboxFunctionSource





T = TypeVar("T", bound="SandboxFunction")



@_attrs_define
class SandboxFunction:
    """ Function code executed by procd for a sandbox service request. cluster-gateway owns public ingress and carries this
    source to procd.

        Attributes:
            runtime (SandboxFunctionRuntime): Function runtime. Only python is supported in this version.
            source (SandboxFunctionSource): Function source code stored in sandbox service config.
            handler (Union[Unset, str]): Python callable name. Defaults to handler.
     """

    runtime: SandboxFunctionRuntime
    source: 'SandboxFunctionSource'
    handler: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_function_source import SandboxFunctionSource
        runtime = self.runtime.value

        source = self.source.to_dict()

        handler = self.handler


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runtime": runtime,
            "source": source,
        })
        if handler is not UNSET:
            field_dict["handler"] = handler

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_function_source import SandboxFunctionSource
        d = dict(src_dict)
        runtime = SandboxFunctionRuntime(d.pop("runtime"))




        source = SandboxFunctionSource.from_dict(d.pop("source"))




        handler = d.pop("handler", UNSET)

        sandbox_function = cls(
            runtime=runtime,
            source=source,
            handler=handler,
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
