from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.function_revision_mount import FunctionRevisionMount
  from ..models.function_env_ref import FunctionEnvRef
  from ..models.function_static_asset import FunctionStaticAsset
  from ..models.sandbox_app_service import SandboxAppService





T = TypeVar("T", bound="FunctionRevisionSpec")



@_attrs_define
class FunctionRevisionSpec:
    """ Immutable execution contract used by Function Gateway to serve a revision.

        Attributes:
            template_id (str): SandboxTemplate ID used to claim runtime sandboxes for this revision.
            runtime_service (SandboxAppService): Canonical service model for sandbox exposure and function publishing.
            mounts (Union[Unset, list['FunctionRevisionMount']]): Volume or artifact mounts attached when runtime sandboxes
                are claimed.
            static_assets (Union[Unset, list['FunctionStaticAsset']]): Static asset artifacts associated with the revision
                for future direct serving paths.
            env_refs (Union[Unset, list['FunctionEnvRef']]): Environment references resolved by future deployment flows.
     """

    template_id: str
    runtime_service: 'SandboxAppService'
    mounts: Union[Unset, list['FunctionRevisionMount']] = UNSET
    static_assets: Union[Unset, list['FunctionStaticAsset']] = UNSET
    env_refs: Union[Unset, list['FunctionEnvRef']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_revision_mount import FunctionRevisionMount
        from ..models.function_env_ref import FunctionEnvRef
        from ..models.function_static_asset import FunctionStaticAsset
        from ..models.sandbox_app_service import SandboxAppService
        template_id = self.template_id

        runtime_service = self.runtime_service.to_dict()

        mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)



        static_assets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.static_assets, Unset):
            static_assets = []
            for static_assets_item_data in self.static_assets:
                static_assets_item = static_assets_item_data.to_dict()
                static_assets.append(static_assets_item)



        env_refs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env_refs, Unset):
            env_refs = []
            for env_refs_item_data in self.env_refs:
                env_refs_item = env_refs_item_data.to_dict()
                env_refs.append(env_refs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "template_id": template_id,
            "runtime_service": runtime_service,
        })
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if static_assets is not UNSET:
            field_dict["static_assets"] = static_assets
        if env_refs is not UNSET:
            field_dict["env_refs"] = env_refs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_revision_mount import FunctionRevisionMount
        from ..models.function_env_ref import FunctionEnvRef
        from ..models.function_static_asset import FunctionStaticAsset
        from ..models.sandbox_app_service import SandboxAppService
        d = dict(src_dict)
        template_id = d.pop("template_id")

        runtime_service = SandboxAppService.from_dict(d.pop("runtime_service"))




        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in (_mounts or []):
            mounts_item = FunctionRevisionMount.from_dict(mounts_item_data)



            mounts.append(mounts_item)


        static_assets = []
        _static_assets = d.pop("static_assets", UNSET)
        for static_assets_item_data in (_static_assets or []):
            static_assets_item = FunctionStaticAsset.from_dict(static_assets_item_data)



            static_assets.append(static_assets_item)


        env_refs = []
        _env_refs = d.pop("env_refs", UNSET)
        for env_refs_item_data in (_env_refs or []):
            env_refs_item = FunctionEnvRef.from_dict(env_refs_item_data)



            env_refs.append(env_refs_item)


        function_revision_spec = cls(
            template_id=template_id,
            runtime_service=runtime_service,
            mounts=mounts,
            static_assets=static_assets,
            env_refs=env_refs,
        )


        function_revision_spec.additional_properties = d
        return function_revision_spec

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
