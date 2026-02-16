import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sandbox_summary_status import SandboxSummaryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxSummary")


@_attrs_define
class SandboxSummary:
    """
    Attributes:
        id (str):
        template_id (str):
        status (SandboxSummaryStatus):
        paused (bool):
        created_at (datetime.datetime):
        expires_at (datetime.datetime):
        cluster_id (Union[None, Unset, str]): Cluster where sandbox runs (multi-cluster only)
    """

    id: str
    template_id: str
    status: SandboxSummaryStatus
    paused: bool
    created_at: datetime.datetime
    expires_at: datetime.datetime
    cluster_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        status = self.status.value

        paused = self.paused

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()

        cluster_id: Union[None, Unset, str]
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "template_id": template_id,
                "status": status,
                "paused": paused,
                "created_at": created_at,
                "expires_at": expires_at,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        status = SandboxSummaryStatus(d.pop("status"))

        paused = d.pop("paused")

        created_at = isoparse(d.pop("created_at"))

        expires_at = isoparse(d.pop("expires_at"))

        def _parse_cluster_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        sandbox_summary = cls(
            id=id,
            template_id=template_id,
            status=status,
            paused=paused,
            created_at=created_at,
            expires_at=expires_at,
            cluster_id=cluster_id,
        )

        sandbox_summary.additional_properties = d
        return sandbox_summary

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
