from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxAuditRequest")


@_attrs_define
class SandboxAuditRequest:
    """
    Attributes:
        request_id (Union[Unset, str]):
        trace_id (Union[Unset, str]):
        source_ip (Union[Unset, str]):
        user_agent (Union[Unset, str]):
        http_method (Union[Unset, str]):
        route (Union[Unset, str]):
        status_code (Union[Unset, int]):
    """

    request_id: Union[Unset, str] = UNSET
    trace_id: Union[Unset, str] = UNSET
    source_ip: Union[Unset, str] = UNSET
    user_agent: Union[Unset, str] = UNSET
    http_method: Union[Unset, str] = UNSET
    route: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request_id = self.request_id

        trace_id = self.trace_id

        source_ip = self.source_ip

        user_agent = self.user_agent

        http_method = self.http_method

        route = self.route

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if source_ip is not UNSET:
            field_dict["source_ip"] = source_ip
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if http_method is not UNSET:
            field_dict["http_method"] = http_method
        if route is not UNSET:
            field_dict["route"] = route
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        request_id = d.pop("request_id", UNSET)

        trace_id = d.pop("trace_id", UNSET)

        source_ip = d.pop("source_ip", UNSET)

        user_agent = d.pop("user_agent", UNSET)

        http_method = d.pop("http_method", UNSET)

        route = d.pop("route", UNSET)

        status_code = d.pop("status_code", UNSET)

        sandbox_audit_request = cls(
            request_id=request_id,
            trace_id=trace_id,
            source_ip=source_ip,
            user_agent=user_agent,
            http_method=http_method,
            route=route,
            status_code=status_code,
        )

        sandbox_audit_request.additional_properties = d
        return sandbox_audit_request

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
