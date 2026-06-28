import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sandbox_lifecycle_status import SandboxLifecycleStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_mount_request import ClaimMountRequest
    from ..models.sandbox_app_service import SandboxAppService
    from ..models.sandbox_resource_config import SandboxResourceConfig
    from ..models.sandbox_ssh_connection import SandboxSSHConnection


T = TypeVar("T", bound="Sandbox")


@_attrs_define
class Sandbox:
    """
    Attributes:
        id (str):
        template_id (str):
        team_id (str):
        status (SandboxLifecycleStatus):
        paused (bool): True when status is paused.
        auto_resume (bool):
        pod_name (str):
        runtime_generation (int): Monotonically increasing runtime generation. Resume starts a new generation.
        expires_at (datetime.datetime): Soft expiration timestamp. Zero value means not set.
        hard_expires_at (datetime.datetime): Hard expiration timestamp. Zero value means not set.
        claimed_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        user_id (Union[Unset, str]):
        services (Union[Unset, list['SandboxAppService']]):
        resources (Union[Unset, SandboxResourceConfig]): Instance-level sandbox resource override. Sandbox0 exposes
            memory only and derives CPU from the platform memory-per-CPU ratio.
        mounts (Union[Unset, list['ClaimMountRequest']]):
        ssh (Union[Unset, SandboxSSHConnection]):
    """

    id: str
    template_id: str
    team_id: str
    status: SandboxLifecycleStatus
    paused: bool
    auto_resume: bool
    pod_name: str
    runtime_generation: int
    expires_at: datetime.datetime
    hard_expires_at: datetime.datetime
    claimed_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: Union[Unset, str] = UNSET
    services: Union[Unset, list["SandboxAppService"]] = UNSET
    resources: Union[Unset, "SandboxResourceConfig"] = UNSET
    mounts: Union[Unset, list["ClaimMountRequest"]] = UNSET
    ssh: Union[Unset, "SandboxSSHConnection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        team_id = self.team_id

        status = self.status.value

        paused = self.paused

        auto_resume = self.auto_resume

        pod_name = self.pod_name

        runtime_generation = self.runtime_generation

        expires_at = self.expires_at.isoformat()

        hard_expires_at = self.hard_expires_at.isoformat()

        claimed_at = self.claimed_at.isoformat()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        user_id = self.user_id

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)

        ssh: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "template_id": template_id,
                "team_id": team_id,
                "status": status,
                "paused": paused,
                "auto_resume": auto_resume,
                "pod_name": pod_name,
                "runtime_generation": runtime_generation,
                "expires_at": expires_at,
                "hard_expires_at": hard_expires_at,
                "claimed_at": claimed_at,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if services is not UNSET:
            field_dict["services"] = services
        if resources is not UNSET:
            field_dict["resources"] = resources
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if ssh is not UNSET:
            field_dict["ssh"] = ssh

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_mount_request import ClaimMountRequest
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.sandbox_resource_config import SandboxResourceConfig
        from ..models.sandbox_ssh_connection import SandboxSSHConnection

        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        team_id = d.pop("team_id")

        status = SandboxLifecycleStatus(d.pop("status"))

        paused = d.pop("paused")

        auto_resume = d.pop("auto_resume")

        pod_name = d.pop("pod_name")

        runtime_generation = d.pop("runtime_generation")

        expires_at = isoparse(d.pop("expires_at"))

        hard_expires_at = isoparse(d.pop("hard_expires_at"))

        claimed_at = isoparse(d.pop("claimed_at"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        user_id = d.pop("user_id", UNSET)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = SandboxAppService.from_dict(services_item_data)

            services.append(services_item)

        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, SandboxResourceConfig]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = SandboxResourceConfig.from_dict(_resources)

        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in _mounts or []:
            mounts_item = ClaimMountRequest.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        _ssh = d.pop("ssh", UNSET)
        ssh: Union[Unset, SandboxSSHConnection]
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = SandboxSSHConnection.from_dict(_ssh)

        sandbox = cls(
            id=id,
            template_id=template_id,
            team_id=team_id,
            status=status,
            paused=paused,
            auto_resume=auto_resume,
            pod_name=pod_name,
            runtime_generation=runtime_generation,
            expires_at=expires_at,
            hard_expires_at=hard_expires_at,
            claimed_at=claimed_at,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            services=services,
            resources=resources,
            mounts=mounts,
            ssh=ssh,
        )

        sandbox.additional_properties = d
        return sandbox

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
