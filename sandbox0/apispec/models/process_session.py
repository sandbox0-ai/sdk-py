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

from ..models.process_session_state import ProcessSessionState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_channel_spec import ProcessChannelSpec
    from ..models.process_cleanup_spec import ProcessCleanupSpec
    from ..models.process_event_log_snapshot import ProcessEventLogSnapshot
    from ..models.process_restart_spec import ProcessRestartSpec
    from ..models.process_session_env_vars import ProcessSessionEnvVars


T = TypeVar("T", bound="ProcessSession")


@_attrs_define
class ProcessSession:
    """
    Attributes:
        id (str):
        command (list[str]):
        state (ProcessSessionState):
        created_at (datetime.datetime):
        channels (list['ProcessChannelSpec']):
        event_log (ProcessEventLogSnapshot):
        alias (Union[Unset, str]):
        cwd (Union[Unset, str]):
        env_vars (Union[Unset, ProcessSessionEnvVars]):
        pid (Union[Unset, int]):
        started_at (Union[Unset, datetime.datetime]):
        exited_at (Union[Unset, datetime.datetime]):
        exit_code (Union[Unset, int]):
        cleanup (Union[Unset, ProcessCleanupSpec]):
        restart (Union[Unset, ProcessRestartSpec]):
    """

    id: str
    command: list[str]
    state: ProcessSessionState
    created_at: datetime.datetime
    channels: list["ProcessChannelSpec"]
    event_log: "ProcessEventLogSnapshot"
    alias: Union[Unset, str] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "ProcessSessionEnvVars"] = UNSET
    pid: Union[Unset, int] = UNSET
    started_at: Union[Unset, datetime.datetime] = UNSET
    exited_at: Union[Unset, datetime.datetime] = UNSET
    exit_code: Union[Unset, int] = UNSET
    cleanup: Union[Unset, "ProcessCleanupSpec"] = UNSET
    restart: Union[Unset, "ProcessRestartSpec"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        command = self.command

        state = self.state.value

        created_at = self.created_at.isoformat()

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        event_log = self.event_log.to_dict()

        alias = self.alias

        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        pid = self.pid

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        exited_at: Union[Unset, str] = UNSET
        if not isinstance(self.exited_at, Unset):
            exited_at = self.exited_at.isoformat()

        exit_code = self.exit_code

        cleanup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cleanup, Unset):
            cleanup = self.cleanup.to_dict()

        restart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "command": command,
                "state": state,
                "created_at": created_at,
                "channels": channels,
                "event_log": event_log,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if pid is not UNSET:
            field_dict["pid"] = pid
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if exited_at is not UNSET:
            field_dict["exited_at"] = exited_at
        if exit_code is not UNSET:
            field_dict["exit_code"] = exit_code
        if cleanup is not UNSET:
            field_dict["cleanup"] = cleanup
        if restart is not UNSET:
            field_dict["restart"] = restart

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_channel_spec import ProcessChannelSpec
        from ..models.process_cleanup_spec import ProcessCleanupSpec
        from ..models.process_event_log_snapshot import ProcessEventLogSnapshot
        from ..models.process_restart_spec import ProcessRestartSpec
        from ..models.process_session_env_vars import ProcessSessionEnvVars

        d = dict(src_dict)
        id = d.pop("id")

        command = cast(list[str], d.pop("command"))

        state = ProcessSessionState(d.pop("state"))

        created_at = isoparse(d.pop("created_at"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = ProcessChannelSpec.from_dict(channels_item_data)

            channels.append(channels_item)

        event_log = ProcessEventLogSnapshot.from_dict(d.pop("event_log"))

        alias = d.pop("alias", UNSET)

        cwd = d.pop("cwd", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, ProcessSessionEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ProcessSessionEnvVars.from_dict(_env_vars)

        pid = d.pop("pid", UNSET)

        _started_at = d.pop("started_at", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _exited_at = d.pop("exited_at", UNSET)
        exited_at: Union[Unset, datetime.datetime]
        if isinstance(_exited_at, Unset):
            exited_at = UNSET
        else:
            exited_at = isoparse(_exited_at)

        exit_code = d.pop("exit_code", UNSET)

        _cleanup = d.pop("cleanup", UNSET)
        cleanup: Union[Unset, ProcessCleanupSpec]
        if isinstance(_cleanup, Unset):
            cleanup = UNSET
        else:
            cleanup = ProcessCleanupSpec.from_dict(_cleanup)

        _restart = d.pop("restart", UNSET)
        restart: Union[Unset, ProcessRestartSpec]
        if isinstance(_restart, Unset):
            restart = UNSET
        else:
            restart = ProcessRestartSpec.from_dict(_restart)

        process_session = cls(
            id=id,
            command=command,
            state=state,
            created_at=created_at,
            channels=channels,
            event_log=event_log,
            alias=alias,
            cwd=cwd,
            env_vars=env_vars,
            pid=pid,
            started_at=started_at,
            exited_at=exited_at,
            exit_code=exit_code,
            cleanup=cleanup,
            restart=restart,
        )

        process_session.additional_properties = d
        return process_session

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
