from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.exec_action import ExecAction
  from ..models.http_get_action import HTTPGetAction
  from ..models.tcp_socket_action import TCPSocketAction
  from ..models.grpc_action import GRPCAction





T = TypeVar("T", bound="Probe")



@_attrs_define
class Probe:
    """ 
        Attributes:
            exec_ (Union[Unset, ExecAction]):
            http_get (Union[Unset, HTTPGetAction]):
            tcp_socket (Union[Unset, TCPSocketAction]):
            grpc (Union[Unset, GRPCAction]):
            initial_delay_seconds (Union[Unset, int]):
            timeout_seconds (Union[Unset, int]):
            period_seconds (Union[Unset, int]):
            success_threshold (Union[Unset, int]):
            failure_threshold (Union[Unset, int]):
            termination_grace_period_seconds (Union[Unset, int]):
     """

    exec_: Union[Unset, 'ExecAction'] = UNSET
    http_get: Union[Unset, 'HTTPGetAction'] = UNSET
    tcp_socket: Union[Unset, 'TCPSocketAction'] = UNSET
    grpc: Union[Unset, 'GRPCAction'] = UNSET
    initial_delay_seconds: Union[Unset, int] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    period_seconds: Union[Unset, int] = UNSET
    success_threshold: Union[Unset, int] = UNSET
    failure_threshold: Union[Unset, int] = UNSET
    termination_grace_period_seconds: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.exec_action import ExecAction
        from ..models.http_get_action import HTTPGetAction
        from ..models.tcp_socket_action import TCPSocketAction
        from ..models.grpc_action import GRPCAction
        exec_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.exec_, Unset):
            exec_ = self.exec_.to_dict()

        http_get: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http_get, Unset):
            http_get = self.http_get.to_dict()

        tcp_socket: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tcp_socket, Unset):
            tcp_socket = self.tcp_socket.to_dict()

        grpc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.grpc, Unset):
            grpc = self.grpc.to_dict()

        initial_delay_seconds = self.initial_delay_seconds

        timeout_seconds = self.timeout_seconds

        period_seconds = self.period_seconds

        success_threshold = self.success_threshold

        failure_threshold = self.failure_threshold

        termination_grace_period_seconds = self.termination_grace_period_seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if exec_ is not UNSET:
            field_dict["exec"] = exec_
        if http_get is not UNSET:
            field_dict["httpGet"] = http_get
        if tcp_socket is not UNSET:
            field_dict["tcpSocket"] = tcp_socket
        if grpc is not UNSET:
            field_dict["grpc"] = grpc
        if initial_delay_seconds is not UNSET:
            field_dict["initialDelaySeconds"] = initial_delay_seconds
        if timeout_seconds is not UNSET:
            field_dict["timeoutSeconds"] = timeout_seconds
        if period_seconds is not UNSET:
            field_dict["periodSeconds"] = period_seconds
        if success_threshold is not UNSET:
            field_dict["successThreshold"] = success_threshold
        if failure_threshold is not UNSET:
            field_dict["failureThreshold"] = failure_threshold
        if termination_grace_period_seconds is not UNSET:
            field_dict["terminationGracePeriodSeconds"] = termination_grace_period_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exec_action import ExecAction
        from ..models.http_get_action import HTTPGetAction
        from ..models.tcp_socket_action import TCPSocketAction
        from ..models.grpc_action import GRPCAction
        d = dict(src_dict)
        _exec_ = d.pop("exec", UNSET)
        exec_: Union[Unset, ExecAction]
        if isinstance(_exec_,  Unset):
            exec_ = UNSET
        else:
            exec_ = ExecAction.from_dict(_exec_)




        _http_get = d.pop("httpGet", UNSET)
        http_get: Union[Unset, HTTPGetAction]
        if isinstance(_http_get,  Unset):
            http_get = UNSET
        else:
            http_get = HTTPGetAction.from_dict(_http_get)




        _tcp_socket = d.pop("tcpSocket", UNSET)
        tcp_socket: Union[Unset, TCPSocketAction]
        if isinstance(_tcp_socket,  Unset):
            tcp_socket = UNSET
        else:
            tcp_socket = TCPSocketAction.from_dict(_tcp_socket)




        _grpc = d.pop("grpc", UNSET)
        grpc: Union[Unset, GRPCAction]
        if isinstance(_grpc,  Unset):
            grpc = UNSET
        else:
            grpc = GRPCAction.from_dict(_grpc)




        initial_delay_seconds = d.pop("initialDelaySeconds", UNSET)

        timeout_seconds = d.pop("timeoutSeconds", UNSET)

        period_seconds = d.pop("periodSeconds", UNSET)

        success_threshold = d.pop("successThreshold", UNSET)

        failure_threshold = d.pop("failureThreshold", UNSET)

        termination_grace_period_seconds = d.pop("terminationGracePeriodSeconds", UNSET)

        probe = cls(
            exec_=exec_,
            http_get=http_get,
            tcp_socket=tcp_socket,
            grpc=grpc,
            initial_delay_seconds=initial_delay_seconds,
            timeout_seconds=timeout_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            failure_threshold=failure_threshold,
            termination_grace_period_seconds=termination_grace_period_seconds,
        )


        probe.additional_properties = d
        return probe

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
