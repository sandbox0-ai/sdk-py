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

from ..models.sandbox_lifecycle_status import SandboxLifecycleStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxSummary")


@_attrs_define
class SandboxSummary:
    """
    Attributes:
        id (str):
        template_id (str):
        status (SandboxLifecycleStatus):
        paused (bool): True when status is paused.
        runtime_generation (int): Monotonically increasing runtime generation. Resume starts a new generation.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        cluster_id (Union[None, Unset, str]): Cluster where sandbox runs (multi-cluster only)
        expires_at (Union[None, Unset, datetime.datetime]): Soft expiration timestamp. Omitted or null means disabled or
            not set.
        hard_expires_at (Union[None, Unset, datetime.datetime]): Hard expiration timestamp. Omitted or null means
            disabled or not set.
    """

    id: str
    template_id: str
    status: SandboxLifecycleStatus
    paused: bool
    runtime_generation: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    cluster_id: Union[None, Unset, str] = UNSET
    expires_at: Union[None, Unset, datetime.datetime] = UNSET
    hard_expires_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        template_id = self.template_id

        status = self.status.value

        paused = self.paused

        runtime_generation = self.runtime_generation

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cluster_id: Union[None, Unset, str]
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

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
                "status": status,
                "paused": paused,
                "runtime_generation": runtime_generation,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if hard_expires_at is not UNSET:
            field_dict["hard_expires_at"] = hard_expires_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        template_id = d.pop("template_id")

        status = SandboxLifecycleStatus(d.pop("status"))

        paused = d.pop("paused")

        runtime_generation = d.pop("runtime_generation")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_cluster_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

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

        sandbox_summary = cls(
            id=id,
            template_id=template_id,
            status=status,
            paused=paused,
            runtime_generation=runtime_generation,
            created_at=created_at,
            updated_at=updated_at,
            cluster_id=cluster_id,
            expires_at=expires_at,
            hard_expires_at=hard_expires_at,
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
