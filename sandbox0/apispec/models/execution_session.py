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

from ..models.execution_session_phase import ExecutionSessionPhase
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_session_attempt import ExecutionSessionAttempt
    from ..models.execution_session_event_cursor import ExecutionSessionEventCursor
    from ..models.execution_session_spec import ExecutionSessionSpec


T = TypeVar("T", bound="ExecutionSession")


@_attrs_define
class ExecutionSession:
    """
    Attributes:
        id (str):
        spec (ExecutionSessionSpec): Generic process-backed session specification. The supervisor does not interpret
            application protocols.
        spec_version (int):
        phase (ExecutionSessionPhase):
        runtime_generation (int):
        restart_count (int):
        cursor (ExecutionSessionEventCursor):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        last_activity_at (datetime.datetime):
        attempt (Union[Unset, ExecutionSessionAttempt]):
    """

    id: str
    spec: "ExecutionSessionSpec"
    spec_version: int
    phase: ExecutionSessionPhase
    runtime_generation: int
    restart_count: int
    cursor: "ExecutionSessionEventCursor"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_activity_at: datetime.datetime
    attempt: Union[Unset, "ExecutionSessionAttempt"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        spec = self.spec.to_dict()

        spec_version = self.spec_version

        phase = self.phase.value

        runtime_generation = self.runtime_generation

        restart_count = self.restart_count

        cursor = self.cursor.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        last_activity_at = self.last_activity_at.isoformat()

        attempt: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.attempt, Unset):
            attempt = self.attempt.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "spec": spec,
                "spec_version": spec_version,
                "phase": phase,
                "runtime_generation": runtime_generation,
                "restart_count": restart_count,
                "cursor": cursor,
                "created_at": created_at,
                "updated_at": updated_at,
                "last_activity_at": last_activity_at,
            }
        )
        if attempt is not UNSET:
            field_dict["attempt"] = attempt

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_session_attempt import ExecutionSessionAttempt
        from ..models.execution_session_event_cursor import ExecutionSessionEventCursor
        from ..models.execution_session_spec import ExecutionSessionSpec

        d = dict(src_dict)
        id = d.pop("id")

        spec = ExecutionSessionSpec.from_dict(d.pop("spec"))

        spec_version = d.pop("spec_version")

        phase = ExecutionSessionPhase(d.pop("phase"))

        runtime_generation = d.pop("runtime_generation")

        restart_count = d.pop("restart_count")

        cursor = ExecutionSessionEventCursor.from_dict(d.pop("cursor"))

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        last_activity_at = isoparse(d.pop("last_activity_at"))

        _attempt = d.pop("attempt", UNSET)
        attempt: Union[Unset, ExecutionSessionAttempt]
        if isinstance(_attempt, Unset):
            attempt = UNSET
        else:
            attempt = ExecutionSessionAttempt.from_dict(_attempt)

        execution_session = cls(
            id=id,
            spec=spec,
            spec_version=spec_version,
            phase=phase,
            runtime_generation=runtime_generation,
            restart_count=restart_count,
            cursor=cursor,
            created_at=created_at,
            updated_at=updated_at,
            last_activity_at=last_activity_at,
            attempt=attempt,
        )

        execution_session.additional_properties = d
        return execution_session

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
