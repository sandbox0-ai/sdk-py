from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.env_var import EnvVar
    from ..models.resource_quota import ResourceQuota
    from ..models.security_context import SecurityContext


T = TypeVar("T", bound="ContainerSpec")


@_attrs_define
class ContainerSpec:
    """
    Attributes:
        image (str):
        resources (ResourceQuota):
        image_pull_policy (Union[Unset, str]):
        env (Union[Unset, list['EnvVar']]):
        security_context (Union[Unset, SecurityContext]):
    """

    image: str
    resources: "ResourceQuota"
    image_pull_policy: Union[Unset, str] = UNSET
    env: Union[Unset, list["EnvVar"]] = UNSET
    security_context: Union[Unset, "SecurityContext"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image = self.image

        resources = self.resources.to_dict()

        image_pull_policy = self.image_pull_policy

        env: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for env_item_data in self.env:
                env_item = env_item_data.to_dict()
                env.append(env_item)

        security_context: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.security_context, Unset):
            security_context = self.security_context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image": image,
                "resources": resources,
            }
        )
        if image_pull_policy is not UNSET:
            field_dict["imagePullPolicy"] = image_pull_policy
        if env is not UNSET:
            field_dict["env"] = env
        if security_context is not UNSET:
            field_dict["securityContext"] = security_context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.env_var import EnvVar
        from ..models.resource_quota import ResourceQuota
        from ..models.security_context import SecurityContext

        d = dict(src_dict)
        image = d.pop("image")

        resources = ResourceQuota.from_dict(d.pop("resources"))

        image_pull_policy = d.pop("imagePullPolicy", UNSET)

        env = []
        _env = d.pop("env", UNSET)
        for env_item_data in _env or []:
            env_item = EnvVar.from_dict(env_item_data)

            env.append(env_item)

        _security_context = d.pop("securityContext", UNSET)
        security_context: Union[Unset, SecurityContext]
        if isinstance(_security_context, Unset):
            security_context = UNSET
        else:
            security_context = SecurityContext.from_dict(_security_context)

        container_spec = cls(
            image=image,
            resources=resources,
            image_pull_policy=image_pull_policy,
            env=env,
            security_context=security_context,
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
