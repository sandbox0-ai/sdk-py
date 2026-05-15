from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sandbox_probe_spec import SandboxProbeSpec





T = TypeVar("T", bound="SandboxProbeSet")



@_attrs_define
class SandboxProbeSet:
    """ 
        Attributes:
            startup (Union[Unset, SandboxProbeSpec]):
            readiness (Union[Unset, SandboxProbeSpec]):
            liveness (Union[Unset, SandboxProbeSpec]):
     """

    startup: Union[Unset, 'SandboxProbeSpec'] = UNSET
    readiness: Union[Unset, 'SandboxProbeSpec'] = UNSET
    liveness: Union[Unset, 'SandboxProbeSpec'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_probe_spec import SandboxProbeSpec
        startup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.startup, Unset):
            startup = self.startup.to_dict()

        readiness: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.readiness, Unset):
            readiness = self.readiness.to_dict()

        liveness: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.liveness, Unset):
            liveness = self.liveness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if startup is not UNSET:
            field_dict["startup"] = startup
        if readiness is not UNSET:
            field_dict["readiness"] = readiness
        if liveness is not UNSET:
            field_dict["liveness"] = liveness

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_probe_spec import SandboxProbeSpec
        d = dict(src_dict)
        _startup = d.pop("startup", UNSET)
        startup: Union[Unset, SandboxProbeSpec]
        if isinstance(_startup,  Unset):
            startup = UNSET
        else:
            startup = SandboxProbeSpec.from_dict(_startup)




        _readiness = d.pop("readiness", UNSET)
        readiness: Union[Unset, SandboxProbeSpec]
        if isinstance(_readiness,  Unset):
            readiness = UNSET
        else:
            readiness = SandboxProbeSpec.from_dict(_readiness)




        _liveness = d.pop("liveness", UNSET)
        liveness: Union[Unset, SandboxProbeSpec]
        if isinstance(_liveness,  Unset):
            liveness = UNSET
        else:
            liveness = SandboxProbeSpec.from_dict(_liveness)




        sandbox_probe_set = cls(
            startup=startup,
            readiness=readiness,
            liveness=liveness,
        )


        sandbox_probe_set.additional_properties = d
        return sandbox_probe_set

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
