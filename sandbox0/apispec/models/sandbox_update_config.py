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
    from ..models.sandbox_app_service import SandboxAppService
    from ..models.sandbox_resource_config import SandboxResourceConfig


T = TypeVar("T", bound="SandboxUpdateConfig")


@_attrs_define
class SandboxUpdateConfig:
    """Durable lifecycle and service fields, or a standalone resources.memory change.
    Resource changes preserve the sandbox ID and durable files but restart processes
    through filesystem pause and a fresh CPU/memory lease. Paused sandboxes stay
    paused with the new next-start configuration; retained memory is discarded.
    Submit resources separately from lifecycle and service fields. The operation
    survives request timeout and manager restart. Retry the same limit after 503;
    an already-applied limit is a no-op. Network policy uses its dedicated endpoint.
    Environment and webhook changes require a new runtime.

        Attributes:
            resources (Union[Unset, SandboxResourceConfig]): Instance-level sandbox resource override. Sandbox0 exposes
                memory only and derives CPU from the platform memory-per-CPU ratio.
            ttl (Union[Unset, int]): Runtime soft time-to-live in seconds. When it expires, Sandbox0 checkpoints the
                writable rootfs, pauses the sandbox, and releases runtime compute while preserving durable sandbox state.
            hard_ttl (Union[Unset, int]): Sandbox hard time-to-live in seconds. When it expires, Sandbox0 deletes the
                sandbox identity and durable state, including paused rootfs checkpoints.
            auto_resume (Union[Unset, bool]): Controls whether supported inbound API or public exposure requests may
                automatically
                make an inactive sandbox available. This setting does not control platform-initiated
                runtime fault recovery. A supported access request returns `503 unavailable` with
                `sandbox is waking up` when an accepted resume has not committed yet. It returns
                `503 sandbox_resume_failed` when that resume attempt has ended unsuccessfully.
                 Default: True.
            services (Union[Unset, list['SandboxAppService']]):
    """

    resources: Union[Unset, "SandboxResourceConfig"] = UNSET
    ttl: Union[Unset, int] = UNSET
    hard_ttl: Union[Unset, int] = UNSET
    auto_resume: Union[Unset, bool] = True
    services: Union[Unset, list["SandboxAppService"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        ttl = self.ttl

        hard_ttl = self.hard_ttl

        auto_resume = self.auto_resume

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resources is not UNSET:
            field_dict["resources"] = resources
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if hard_ttl is not UNSET:
            field_dict["hard_ttl"] = hard_ttl
        if auto_resume is not UNSET:
            field_dict["auto_resume"] = auto_resume
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.sandbox_resource_config import SandboxResourceConfig

        d = dict(src_dict)
        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, SandboxResourceConfig]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = SandboxResourceConfig.from_dict(_resources)

        ttl = d.pop("ttl", UNSET)

        hard_ttl = d.pop("hard_ttl", UNSET)

        auto_resume = d.pop("auto_resume", UNSET)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = SandboxAppService.from_dict(services_item_data)

            services.append(services_item)

        sandbox_update_config = cls(
            resources=resources,
            ttl=ttl,
            hard_ttl=hard_ttl,
            auto_resume=auto_resume,
            services=services,
        )

        sandbox_update_config.additional_properties = d
        return sandbox_update_config

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
