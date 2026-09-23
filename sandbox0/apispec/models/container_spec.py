from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.container_spec_security_class import ContainerSpecSecurityClass
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env_var import EnvVar
    from ..models.resource_quota import ResourceQuota


T = TypeVar("T", bound="ContainerSpec")


@_attrs_define
class ContainerSpec:
    """
    Attributes:
        image (str): Canonical normalized OCI reference pinned by a lowercase SHA-256 digest. Mutable tags are rejected.
        resources (ResourceQuota):
        env (Union[Unset, list['EnvVar']]):
        security_class (Union[Unset, ContainerSpecSecurityClass]): New templates and sandboxes use privileged. Standard
            remains valid for existing sandbox records and resume. Privileged capabilities remain confined by runsc and do
            not expose host devices. Default: ContainerSpecSecurityClass.PRIVILEGED.
    """

    image: str
    resources: "ResourceQuota"
    env: Union[Unset, list["EnvVar"]] = UNSET
    security_class: Union[Unset, ContainerSpecSecurityClass] = (
        ContainerSpecSecurityClass.PRIVILEGED
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        resources = self.resources.to_dict()

        env: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for env_item_data in self.env:
                env_item = env_item_data.to_dict()
                env.append(env_item)

        security_class: Union[Unset, str] = UNSET
        if not isinstance(self.security_class, Unset):
            security_class = self.security_class.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "resources": resources,
            }
        )
        if env is not UNSET:
            field_dict["env"] = env
        if security_class is not UNSET:
            field_dict["securityClass"] = security_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar
        from ..models.resource_quota import ResourceQuota

        d = dict(src_dict)
        image = d.pop("image")

        resources = ResourceQuota.from_dict(d.pop("resources"))

        env = []
        _env = d.pop("env", UNSET)
        for env_item_data in _env or []:
            env_item = EnvVar.from_dict(env_item_data)

            env.append(env_item)

        _security_class = d.pop("securityClass", UNSET)
        security_class: Union[Unset, ContainerSpecSecurityClass]
        if isinstance(_security_class, Unset):
            security_class = UNSET
        else:
            security_class = ContainerSpecSecurityClass(_security_class)

        container_spec = cls(
            image=image,
            resources=resources,
            env=env,
            security_class=security_class,
        )

        container_spec.additional_properties = d
        return container_spec

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
