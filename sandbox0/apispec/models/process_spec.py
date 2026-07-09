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

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_channel_spec import ProcessChannelSpec
    from ..models.process_cleanup_spec import ProcessCleanupSpec
    from ..models.process_restart_spec import ProcessRestartSpec
    from ..models.process_spec_env_vars import ProcessSpecEnvVars


T = TypeVar("T", bound="ProcessSpec")


@_attrs_define
class ProcessSpec:
    """
    Attributes:
        command (list[str]): argv array. procd does not shell-expand command strings.
        channels (list['ProcessChannelSpec']):
        alias (Union[Unset, str]):
        cwd (Union[Unset, str]):
        env_vars (Union[Unset, ProcessSpecEnvVars]):
        cleanup (Union[Unset, ProcessCleanupSpec]):
        restart (Union[Unset, ProcessRestartSpec]):
        event_buffer_size (Union[Unset, int]):
        input_buffer_size (Union[Unset, int]):
    """

    command: list[str]
    channels: list["ProcessChannelSpec"]
    alias: Union[Unset, str] = UNSET
    cwd: Union[Unset, str] = UNSET
    env_vars: Union[Unset, "ProcessSpecEnvVars"] = UNSET
    cleanup: Union[Unset, "ProcessCleanupSpec"] = UNSET
    restart: Union[Unset, "ProcessRestartSpec"] = UNSET
    event_buffer_size: Union[Unset, int] = UNSET
    input_buffer_size: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        alias = self.alias

        cwd = self.cwd

        env_vars: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.env_vars, Unset):
            env_vars = self.env_vars.to_dict()

        cleanup: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cleanup, Unset):
            cleanup = self.cleanup.to_dict()

        restart: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.restart, Unset):
            restart = self.restart.to_dict()

        event_buffer_size = self.event_buffer_size

        input_buffer_size = self.input_buffer_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "command": command,
                "channels": channels,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if cwd is not UNSET:
            field_dict["cwd"] = cwd
        if env_vars is not UNSET:
            field_dict["env_vars"] = env_vars
        if cleanup is not UNSET:
            field_dict["cleanup"] = cleanup
        if restart is not UNSET:
            field_dict["restart"] = restart
        if event_buffer_size is not UNSET:
            field_dict["event_buffer_size"] = event_buffer_size
        if input_buffer_size is not UNSET:
            field_dict["input_buffer_size"] = input_buffer_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.process_channel_spec import ProcessChannelSpec
        from ..models.process_cleanup_spec import ProcessCleanupSpec
        from ..models.process_restart_spec import ProcessRestartSpec
        from ..models.process_spec_env_vars import ProcessSpecEnvVars

        d = dict(src_dict)
        command = cast(list[str], d.pop("command"))

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = ProcessChannelSpec.from_dict(channels_item_data)

            channels.append(channels_item)

        alias = d.pop("alias", UNSET)

        cwd = d.pop("cwd", UNSET)

        _env_vars = d.pop("env_vars", UNSET)
        env_vars: Union[Unset, ProcessSpecEnvVars]
        if isinstance(_env_vars, Unset):
            env_vars = UNSET
        else:
            env_vars = ProcessSpecEnvVars.from_dict(_env_vars)

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

        event_buffer_size = d.pop("event_buffer_size", UNSET)

        input_buffer_size = d.pop("input_buffer_size", UNSET)

        process_spec = cls(
            command=command,
            channels=channels,
            alias=alias,
            cwd=cwd,
            env_vars=env_vars,
            cleanup=cleanup,
            restart=restart,
            event_buffer_size=event_buffer_size,
            input_buffer_size=input_buffer_size,
        )

        process_spec.additional_properties = d
        return process_spec

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
