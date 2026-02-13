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
    from ..models.exposed_port_config import ExposedPortConfig


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
        auto_resume (bool):
        pod_name (str):
        expires_at (datetime.datetime):
        claimed_at (datetime.datetime):
        created_at (datetime.datetime):
        user_id (Union[Unset, str]):
        exposed_ports (Union[Unset, list['ExposedPortConfig']]):
    """

    id: str
    template_id: str
    team_id: str
    status: str
    paused: bool
    auto_resume: bool
    pod_name: str
    expires_at: datetime.datetime
    claimed_at: datetime.datetime
    created_at: datetime.datetime
    user_id: Union[Unset, str] = UNSET
    exposed_ports: Union[Unset, list["ExposedPortConfig"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        team_id = self.team_id

        status = self.status

        paused = self.paused

        auto_resume = self.auto_resume

        pod_name = self.pod_name

        expires_at = self.expires_at.isoformat()

        claimed_at = self.claimed_at.isoformat()

        created_at = self.created_at.isoformat()

        user_id = self.user_id

        exposed_ports: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.exposed_ports, Unset):
            exposed_ports = []
            for exposed_ports_item_data in self.exposed_ports:
                exposed_ports_item = exposed_ports_item_data.to_dict()
                exposed_ports.append(exposed_ports_item)

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
                "expires_at": expires_at,
                "claimed_at": claimed_at,
                "created_at": created_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if exposed_ports is not UNSET:
            field_dict["exposed_ports"] = exposed_ports

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exposed_port_config import ExposedPortConfig

        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        team_id = d.pop("team_id")

        status = d.pop("status")

        paused = d.pop("paused")

        auto_resume = d.pop("auto_resume")

        pod_name = d.pop("pod_name")

        expires_at = isoparse(d.pop("expires_at"))

        claimed_at = isoparse(d.pop("claimed_at"))

        created_at = isoparse(d.pop("created_at"))

        user_id = d.pop("user_id", UNSET)

        exposed_ports = []
        _exposed_ports = d.pop("exposed_ports", UNSET)
        for exposed_ports_item_data in _exposed_ports or []:
            exposed_ports_item = ExposedPortConfig.from_dict(exposed_ports_item_data)

            exposed_ports.append(exposed_ports_item)

        sandbox = cls(
            id=id,
            template_id=template_id,
            team_id=team_id,
            status=status,
            paused=paused,
            auto_resume=auto_resume,
            pod_name=pod_name,
            expires_at=expires_at,
            claimed_at=claimed_at,
            created_at=created_at,
            user_id=user_id,
            exposed_ports=exposed_ports,
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
