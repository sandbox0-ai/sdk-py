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

from ..models.sandbox_observability_watch_line_type import (
    SandboxObservabilityWatchLineType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_observability_event import SandboxObservabilityEvent
    from ..models.sandbox_observability_log_entry import SandboxObservabilityLogEntry


T = TypeVar("T", bound="SandboxObservabilityWatchLine")


@_attrs_define
class SandboxObservabilityWatchLine:
    """
    Attributes:
        type_ (SandboxObservabilityWatchLineType):
        data (Union['SandboxObservabilityEvent', 'SandboxObservabilityLogEntry', Unset]):
        cursor (Union[Unset, str]): Watch resume cursor. Present on watermark lines.
        watermark (Union[Unset, str]): Backend watermark for the emitted batch.
        time (Union[Unset, datetime.datetime]): Heartbeat timestamp.
        error (Union[Unset, str]): Stream error message.
    """

    type_: SandboxObservabilityWatchLineType
    data: Union["SandboxObservabilityEvent", "SandboxObservabilityLogEntry", Unset] = (
        UNSET
    )
    cursor: Union[Unset, str] = UNSET
    watermark: Union[Unset, str] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    error: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_observability_event import SandboxObservabilityEvent

        type_ = self.type_.value

        data: Union[Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, SandboxObservabilityEvent):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        cursor = self.cursor

        watermark = self.watermark

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if cursor is not UNSET:
            field_dict["cursor"] = cursor
        if watermark is not UNSET:
            field_dict["watermark"] = watermark
        if time is not UNSET:
            field_dict["time"] = time
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_observability_event import SandboxObservabilityEvent
        from ..models.sandbox_observability_log_entry import (
            SandboxObservabilityLogEntry,
        )

        d = dict(src_dict)
        type_ = SandboxObservabilityWatchLineType(d.pop("type"))

        def _parse_data(
            data: object,
        ) -> Union["SandboxObservabilityEvent", "SandboxObservabilityLogEntry", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = SandboxObservabilityEvent.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = SandboxObservabilityLogEntry.from_dict(data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        cursor = d.pop("cursor", UNSET)

        watermark = d.pop("watermark", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        error = d.pop("error", UNSET)

        sandbox_observability_watch_line = cls(
            type_=type_,
            data=data,
            cursor=cursor,
            watermark=watermark,
            time=time,
            error=error,
        )

        sandbox_observability_watch_line.additional_properties = d
        return sandbox_observability_watch_line

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
