from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_channel_framing import ProcessChannelFraming
from ..models.process_channel_kind import ProcessChannelKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_channel_spec import HTTPChannelSpec
    from ..models.pty_size import PTYSize
    from ..models.web_socket_channel_spec import WebSocketChannelSpec


T = TypeVar("T", bound="ProcessChannelSpec")


@_attrs_define
class ProcessChannelSpec:
    """
    Attributes:
        name (str):
        kind (ProcessChannelKind):
        framing (Union[Unset, ProcessChannelFraming]):
        stdin (Union[Unset, bool]):
        stdout (Union[Unset, bool]):
        stderr (Union[Unset, bool]):
        pty_size (Union[Unset, PTYSize]):
        http (Union[Unset, HTTPChannelSpec]):
        websocket (Union[Unset, WebSocketChannelSpec]):
    """

    name: str
    kind: ProcessChannelKind
    framing: Union[Unset, ProcessChannelFraming] = UNSET
    stdin: Union[Unset, bool] = UNSET
    stdout: Union[Unset, bool] = UNSET
    stderr: Union[Unset, bool] = UNSET
    pty_size: Union[Unset, "PTYSize"] = UNSET
    http: Union[Unset, "HTTPChannelSpec"] = UNSET
    websocket: Union[Unset, "WebSocketChannelSpec"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        kind = self.kind.value

        framing: Union[Unset, str] = UNSET
        if not isinstance(self.framing, Unset):
            framing = self.framing.value

        stdin = self.stdin

        stdout = self.stdout

        stderr = self.stderr

        pty_size: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pty_size, Unset):
            pty_size = self.pty_size.to_dict()

        http: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.http, Unset):
            http = self.http.to_dict()

        websocket: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.websocket, Unset):
            websocket = self.websocket.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "kind": kind,
            }
        )
        if framing is not UNSET:
            field_dict["framing"] = framing
        if stdin is not UNSET:
            field_dict["stdin"] = stdin
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if pty_size is not UNSET:
            field_dict["pty_size"] = pty_size
        if http is not UNSET:
            field_dict["http"] = http
        if websocket is not UNSET:
            field_dict["websocket"] = websocket

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_channel_spec import HTTPChannelSpec
        from ..models.pty_size import PTYSize
        from ..models.web_socket_channel_spec import WebSocketChannelSpec

        d = dict(src_dict)
        name = d.pop("name")

        kind = ProcessChannelKind(d.pop("kind"))

        _framing = d.pop("framing", UNSET)
        framing: Union[Unset, ProcessChannelFraming]
        if isinstance(_framing, Unset):
            framing = UNSET
        else:
            framing = ProcessChannelFraming(_framing)

        stdin = d.pop("stdin", UNSET)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        _pty_size = d.pop("pty_size", UNSET)
        pty_size: Union[Unset, PTYSize]
        if isinstance(_pty_size, Unset):
            pty_size = UNSET
        else:
            pty_size = PTYSize.from_dict(_pty_size)

        _http = d.pop("http", UNSET)
        http: Union[Unset, HTTPChannelSpec]
        if isinstance(_http, Unset):
            http = UNSET
        else:
            http = HTTPChannelSpec.from_dict(_http)

        _websocket = d.pop("websocket", UNSET)
        websocket: Union[Unset, WebSocketChannelSpec]
        if isinstance(_websocket, Unset):
            websocket = UNSET
        else:
            websocket = WebSocketChannelSpec.from_dict(_websocket)

        process_channel_spec = cls(
            name=name,
            kind=kind,
            framing=framing,
            stdin=stdin,
            stdout=stdout,
            stderr=stderr,
            pty_size=pty_size,
            http=http,
            websocket=websocket,
        )

        process_channel_spec.additional_properties = d
        return process_channel_spec

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
