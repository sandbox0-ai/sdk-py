from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exec_action import ExecAction
    from ..models.http_get_action import HTTPGetAction
    from ..models.process_probe_action import ProcessProbeAction
    from ..models.tcp_socket_action import TCPSocketAction


T = TypeVar("T", bound="SandboxProbeSpec")


@_attrs_define
class SandboxProbeSpec:
    """
    Attributes:
        process (Union[Unset, ProcessProbeAction]):
        exec_ (Union[Unset, ExecAction]):
        http_get (Union[Unset, HTTPGetAction]):
        tcp_socket (Union[Unset, TCPSocketAction]):
        initial_delay_seconds (Union[Unset, int]):
        timeout_seconds (Union[Unset, int]):
    """

    process: Union[Unset, "ProcessProbeAction"] = UNSET
    exec_: Union[Unset, "ExecAction"] = UNSET
    http_get: Union[Unset, "HTTPGetAction"] = UNSET
    tcp_socket: Union[Unset, "TCPSocketAction"] = UNSET
    initial_delay_seconds: Union[Unset, int] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.process, Unset):
            process = self.process.to_dict()

        exec_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exec_, Unset):
            exec_ = self.exec_.to_dict()

        http_get: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_get, Unset):
            http_get = self.http_get.to_dict()

        tcp_socket: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tcp_socket, Unset):
            tcp_socket = self.tcp_socket.to_dict()

        initial_delay_seconds = self.initial_delay_seconds

        timeout_seconds = self.timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process is not UNSET:
            field_dict["process"] = process
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if http_get is not UNSET:
            field_dict["httpGet"] = http_get
        if tcp_socket is not UNSET:
            field_dict["tcpSocket"] = tcp_socket
        if initial_delay_seconds is not UNSET:
            field_dict["initialDelaySeconds"] = initial_delay_seconds
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exec_action import ExecAction
        from ..models.http_get_action import HTTPGetAction
        from ..models.process_probe_action import ProcessProbeAction
        from ..models.tcp_socket_action import TCPSocketAction

        d = dict(src_dict)
        _process = d.pop("process", UNSET)
        process: Union[Unset, ProcessProbeAction]
        if isinstance(_process, Unset):
            process = UNSET
        else:
            process = ProcessProbeAction.from_dict(_process)

        _exec_ = d.pop("exec", UNSET)
        exec_: Union[Unset, ExecAction]
        if isinstance(_exec_, Unset):
            exec_ = UNSET
        else:
            exec_ = ExecAction.from_dict(_exec_)

        _http_get = d.pop("httpGet", UNSET)
        http_get: Union[Unset, HTTPGetAction]
        if isinstance(_http_get, Unset):
            http_get = UNSET
        else:
            http_get = HTTPGetAction.from_dict(_http_get)

        _tcp_socket = d.pop("tcpSocket", UNSET)
        tcp_socket: Union[Unset, TCPSocketAction]
        if isinstance(_tcp_socket, Unset):
            tcp_socket = UNSET
        else:
            tcp_socket = TCPSocketAction.from_dict(_tcp_socket)

        initial_delay_seconds = d.pop("initialDelaySeconds", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        sandbox_probe_spec = cls(
            process=process,
            exec_=exec_,
            http_get=http_get,
            tcp_socket=tcp_socket,
            initial_delay_seconds=initial_delay_seconds,
            timeout_seconds=timeout_seconds,
        )

        sandbox_probe_spec.additional_properties = d
        return sandbox_probe_spec

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
