from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sandbox_app_service_ingress import SandboxAppServiceIngress
  from ..models.sandbox_app_service_runtime import SandboxAppServiceRuntime
  from ..models.sandbox_app_service_health import SandboxAppServiceHealth





T = TypeVar("T", bound="SandboxAppService")



@_attrs_define
class SandboxAppService:
    """ Canonical service model for sandbox exposure and function publishing.

        Attributes:
            id (str): Stable service ID. Must be a DNS label.
            port (int):
            ingress (SandboxAppServiceIngress):
            display_name (Union[Unset, str]):
            runtime (Union[Unset, SandboxAppServiceRuntime]):
            health_check (Union[Unset, SandboxAppServiceHealth]):
     """

    id: str
    port: int
    ingress: 'SandboxAppServiceIngress'
    display_name: Union[Unset, str] = UNSET
    runtime: Union[Unset, 'SandboxAppServiceRuntime'] = UNSET
    health_check: Union[Unset, 'SandboxAppServiceHealth'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_app_service_ingress import SandboxAppServiceIngress
        from ..models.sandbox_app_service_runtime import SandboxAppServiceRuntime
        from ..models.sandbox_app_service_health import SandboxAppServiceHealth
        id = self.id

        port = self.port

        ingress = self.ingress.to_dict()

        display_name = self.display_name

        runtime: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.runtime, Unset):
            runtime = self.runtime.to_dict()

        health_check: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.health_check, Unset):
            health_check = self.health_check.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "port": port,
            "ingress": ingress,
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if runtime is not UNSET:
            field_dict["runtime"] = runtime
        if health_check is not UNSET:
            field_dict["health_check"] = health_check

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service_ingress import SandboxAppServiceIngress
        from ..models.sandbox_app_service_runtime import SandboxAppServiceRuntime
        from ..models.sandbox_app_service_health import SandboxAppServiceHealth
        d = dict(src_dict)
        id = d.pop("id")

        port = d.pop("port")

        ingress = SandboxAppServiceIngress.from_dict(d.pop("ingress"))




        display_name = d.pop("display_name", UNSET)

        _runtime = d.pop("runtime", UNSET)
        runtime: Union[Unset, SandboxAppServiceRuntime]
        if isinstance(_runtime,  Unset):
            runtime = UNSET
        else:
            runtime = SandboxAppServiceRuntime.from_dict(_runtime)




        _health_check = d.pop("health_check", UNSET)
        health_check: Union[Unset, SandboxAppServiceHealth]
        if isinstance(_health_check,  Unset):
            health_check = UNSET
        else:
            health_check = SandboxAppServiceHealth.from_dict(_health_check)




        sandbox_app_service = cls(
            id=id,
            port=port,
            ingress=ingress,
            display_name=display_name,
            runtime=runtime,
            health_check=health_check,
        )


        sandbox_app_service.additional_properties = d
        return sandbox_app_service

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
