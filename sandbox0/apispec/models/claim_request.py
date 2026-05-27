from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.sandbox_config import SandboxConfig
  from ..models.claim_mount_request import ClaimMountRequest





T = TypeVar("T", bound="ClaimRequest")



@_attrs_define
class ClaimRequest:
    """ 
        Attributes:
            template (Union[Unset, str]):
            config (Union[Unset, SandboxConfig]):
            mounts (Union[Unset, list['ClaimMountRequest']]):
     """

    template: Union[Unset, str] = UNSET
    config: Union[Unset, 'SandboxConfig'] = UNSET
    mounts: Union[Unset, list['ClaimMountRequest']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_config import SandboxConfig
        from ..models.claim_mount_request import ClaimMountRequest
        template = self.template

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if template is not UNSET:
            field_dict["template"] = template
        if config is not UNSET:
            field_dict["config"] = config
        if mounts is not UNSET:
            field_dict["mounts"] = mounts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_config import SandboxConfig
        from ..models.claim_mount_request import ClaimMountRequest
        d = dict(src_dict)
        template = d.pop("template", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, SandboxConfig]
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = SandboxConfig.from_dict(_config)




        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in (_mounts or []):
            mounts_item = ClaimMountRequest.from_dict(mounts_item_data)



            mounts.append(mounts_item)


        claim_request = cls(
            template=template,
            config=config,
            mounts=mounts,
        )


        claim_request.additional_properties = d
        return claim_request

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
