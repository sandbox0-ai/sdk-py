import datetime
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sandbox_lifecycle_status import SandboxLifecycleStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
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
        runtime_id (str): Opaque identifier of the current physical runtime allocation. Empty while paused.
        runtime_generation (int): Monotonically increasing runtime generation. Resume starts a new generation.
        claimed_at (datetime.datetime):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        user_id (Union[Unset, str]):
        services (Union[Unset, list['SandboxAppService']]):
        resources (Union[Unset, SandboxResourceConfig]): Instance-level sandbox resource override. Sandbox0 exposes
            memory only and derives CPU from the platform memory-per-CPU ratio.
        ssh (Union[Unset, SandboxSSHConnection]):
        expires_at (Union[None, Unset, datetime.datetime]): Soft expiration timestamp. Omitted or null means disabled or
            not set.
        hard_expires_at (Union[None, Unset, datetime.datetime]): Hard expiration timestamp. Omitted or null means
            disabled or not set.
    """

    id: str
    template_id: str
    team_id: str
    status: SandboxLifecycleStatus
    paused: bool
    auto_resume: bool
    runtime_id: str
    runtime_generation: int
    claimed_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    user_id: Union[Unset, str] = UNSET
    services: Union[Unset, list["SandboxAppService"]] = UNSET
    resources: Union[Unset, "SandboxResourceConfig"] = UNSET
    ssh: Union[Unset, "SandboxSSHConnection"] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    hard_expires_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        team_id = self.team_id

        status = self.status.value

        paused = self.paused

        auto_resume = self.auto_resume

        runtime_id = self.runtime_id

        runtime_generation = self.runtime_generation

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

        ssh: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        expires_at: Union[None, Unset, str]
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        hard_expires_at: Union[None, Unset, str]
        if isinstance(self.hard_expires_at, Unset):
            hard_expires_at = UNSET
        elif isinstance(self.hard_expires_at, datetime.datetime):
            hard_expires_at = self.hard_expires_at.isoformat()
        else:
            hard_expires_at = self.hard_expires_at

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
                "runtime_id": runtime_id,
                "runtime_generation": runtime_generation,
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
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if hard_expires_at is not UNSET:
            field_dict["hard_expires_at"] = hard_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
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

        runtime_id = d.pop("runtime_id")

        runtime_generation = d.pop("runtime_generation")

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

        _ssh = d.pop("ssh", UNSET)
        ssh: Union[Unset, SandboxSSHConnection]
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = SandboxSSHConnection.from_dict(_ssh)

        def _parse_expires_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_hard_expires_at(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hard_expires_at_type_0 = isoparse(data)

                return hard_expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        hard_expires_at = _parse_hard_expires_at(d.pop("hard_expires_at", UNSET))

        sandbox = cls(
            id=id,
            template_id=template_id,
            team_id=team_id,
            status=status,
            paused=paused,
            auto_resume=auto_resume,
            runtime_id=runtime_id,
            runtime_generation=runtime_generation,
            claimed_at=claimed_at,
            created_at=created_at,
            updated_at=updated_at,
            user_id=user_id,
            services=services,
            resources=resources,
            ssh=ssh,
            expires_at=expires_at,
            hard_expires_at=hard_expires_at,
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
