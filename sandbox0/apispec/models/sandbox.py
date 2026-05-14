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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.claim_mount_request import ClaimMountRequest
    from ..models.public_gateway_config import PublicGatewayConfig
    from ..models.sandbox_app_service import SandboxAppService
    from ..models.sandbox_power_state import SandboxPowerState
    from ..models.sandbox_ssh_connection import SandboxSSHConnection


T = TypeVar("T", bound="Sandbox")


@_attrs_define
class Sandbox:
    """
    Attributes:
        id (str):
        template_id (str):
        team_id (str):
        status (str):
        paused (bool):
        power_state (SandboxPowerState):
        auto_resume (bool):
        pod_name (str):
        expires_at (datetime.datetime): Soft expiration timestamp. Zero value means not set.
        hard_expires_at (datetime.datetime): Hard expiration timestamp. Zero value means not set.
        claimed_at (datetime.datetime):
        created_at (datetime.datetime):
        user_id (Union[Unset, str]):
        services (Union[Unset, list['SandboxAppService']]):
        public_gateway (Union[Unset, PublicGatewayConfig]):
        mounts (Union[Unset, list['ClaimMountRequest']]):
        ssh (Union[Unset, SandboxSSHConnection]):
    """

    id: str
    template_id: str
    team_id: str
    status: str
    paused: bool
    power_state: "SandboxPowerState"
    auto_resume: bool
    pod_name: str
    expires_at: datetime.datetime
    hard_expires_at: datetime.datetime
    claimed_at: datetime.datetime
    created_at: datetime.datetime
    user_id: Union[Unset, str] = UNSET
    services: Union[Unset, list["SandboxAppService"]] = UNSET
    public_gateway: Union[Unset, "PublicGatewayConfig"] = UNSET
    mounts: Union[Unset, list["ClaimMountRequest"]] = UNSET
    ssh: Union[Unset, "SandboxSSHConnection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        team_id = self.team_id

        status = self.status

        paused = self.paused

        power_state = self.power_state.to_dict()

        auto_resume = self.auto_resume

        pod_name = self.pod_name

        expires_at = self.expires_at.isoformat()

        hard_expires_at = self.hard_expires_at.isoformat()

        claimed_at = self.claimed_at.isoformat()

        created_at = self.created_at.isoformat()

        user_id = self.user_id

        services: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        public_gateway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.public_gateway, Unset):
            public_gateway = self.public_gateway.to_dict()

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
                "power_state": power_state,
                "auto_resume": auto_resume,
                "pod_name": pod_name,
                "expires_at": expires_at,
                "hard_expires_at": hard_expires_at,
                "claimed_at": claimed_at,
                "created_at": created_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if services is not UNSET:
            field_dict["services"] = services
        if public_gateway is not UNSET:
            field_dict["public_gateway"] = public_gateway
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if ssh is not UNSET:
            field_dict["ssh"] = ssh

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_mount_request import ClaimMountRequest
        from ..models.public_gateway_config import PublicGatewayConfig
        from ..models.sandbox_app_service import SandboxAppService
        from ..models.sandbox_power_state import SandboxPowerState
        from ..models.sandbox_ssh_connection import SandboxSSHConnection

        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        team_id = d.pop("team_id")

        status = d.pop("status")

        paused = d.pop("paused")

        power_state = SandboxPowerState.from_dict(d.pop("power_state"))

        auto_resume = d.pop("auto_resume")

        pod_name = d.pop("pod_name")

        expires_at = isoparse(d.pop("expires_at"))

        hard_expires_at = isoparse(d.pop("hard_expires_at"))

        claimed_at = isoparse(d.pop("claimed_at"))

        created_at = isoparse(d.pop("created_at"))

        user_id = d.pop("user_id", UNSET)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = SandboxAppService.from_dict(services_item_data)

            services.append(services_item)

        _public_gateway = d.pop("public_gateway", UNSET)
        public_gateway: Union[Unset, PublicGatewayConfig]
        if isinstance(_public_gateway, Unset):
            public_gateway = UNSET
        else:
            public_gateway = PublicGatewayConfig.from_dict(_public_gateway)

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
            power_state=power_state,
            auto_resume=auto_resume,
            pod_name=pod_name,
            expires_at=expires_at,
            hard_expires_at=hard_expires_at,
            claimed_at=claimed_at,
            created_at=created_at,
            user_id=user_id,
            services=services,
            public_gateway=public_gateway,
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
