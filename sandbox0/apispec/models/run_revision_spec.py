from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.run_revision_spec_env_vars import RunRevisionSpecEnvVars
  from ..models.sandbox_app_service import SandboxAppService
  from ..models.run_revision_mount import RunRevisionMount





T = TypeVar("T", bound="RunRevisionSpec")



@_attrs_define
class RunRevisionSpec:
    """ Canonical runtime contract compiled from every run deploy mode.

        Attributes:
            template (str):
            service (SandboxAppService): Canonical service model for sandbox exposure.
            mounts (Union[Unset, list['RunRevisionMount']]):
            env_vars (Union[Unset, RunRevisionSpecEnvVars]):
     """

    template: str
    service: 'SandboxAppService'
    mounts: Union[Unset, list['RunRevisionMount']] = UNSET
    env_vars: Union[Unset, 'RunRevisionSpecEnvVars'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_revision_spec_env_vars import RunRevisionSpecEnvVars
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.run_revision_mount import RunRevisionMount
        template = self.template

        service = self.service.to_dict()

        mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)



        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "template": template,
            "service": service,
        })
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_revision_spec_env_vars import RunRevisionSpecEnvVars
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.run_revision_mount import RunRevisionMount
        d = dict(src_dict)
        template = d.pop("template")

        service = SandboxAppService.from_dict(d.pop("service"))




        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in (_mounts or []):
            mounts_item = RunRevisionMount.from_dict(mounts_item_data)



            mounts.append(mounts_item)


        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, RunRevisionSpecEnvVars]
        if isinstance(_env_vars,  Unset):
            env_vars = UNSET
        else:
            env_vars = RunRevisionSpecEnvVars.from_dict(_env_vars)




        run_revision_spec = cls(
            template=template,
            service=service,
            mounts=mounts,
            env_vars=env_vars,
        )


        run_revision_spec.additional_properties = d
        return run_revision_spec

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
