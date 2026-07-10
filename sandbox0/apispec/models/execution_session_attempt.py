import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExecutionSessionAttempt")


@_attrs_define
class ExecutionSessionAttempt:
    """
    Attributes:
        id (str):
        number (int):
        runtime_generation (int):
        pid (Union[Unset, int]):
        started_at (Union[Unset, datetime.datetime]):
        finished_at (Union[Unset, datetime.datetime]):
        exit_code (Union[Unset, int]):
        reason (Union[Unset, str]):
    """

    id: str
    number: int
    runtime_generation: int
    pid: Union[Unset, int] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    finished_at: Union[Unset, datetime.datetime] = UNSET
    exit_code: Union[Unset, int] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        number = self.number

        runtime_generation = self.runtime_generation

        pid = self.pid

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        finished_at: Union[Unset, str] = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        exit_code = self.exit_code

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "number": number,
                "runtime_generation": runtime_generation,
            }
        )
        if pid is not UNSET:
            field_dict["pid"] = pid
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        number = d.pop("number")

        runtime_generation = d.pop("runtime_generation")

        pid = d.pop("pid", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _finished_at = d.pop("finished_at", UNSET)
        finished_at: Union[Unset, datetime.datetime]
        if isinstance(_finished_at, Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)

        exit_code = d.pop("exit_code", UNSET)

        reason = d.pop("reason", UNSET)

        execution_session_attempt = cls(
            id=id,
            number=number,
            runtime_generation=runtime_generation,
            pid=pid,
            started_at=started_at,
            finished_at=finished_at,
            exit_code=exit_code,
            reason=reason,
        )

        execution_session_attempt.additional_properties = d
        return execution_session_attempt

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
