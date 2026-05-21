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
    from ..models.mcp_tool_policy import MCPToolPolicy


T = TypeVar("T", bound="MCPProtocolRule")


@_attrs_define
class MCPProtocolRule:
    """Model Context Protocol operation policy.

    Attributes:
        tools (Union[Unset, MCPToolPolicy]): Tool-name allow and deny lists for MCP tools/call requests.
    """

    tools: Union[Unset, "MCPToolPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tools: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = self.tools.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_tool_policy import MCPToolPolicy

        d = dict(src_dict)
        _tools = d.pop("tools", UNSET)
        tools: Union[Unset, MCPToolPolicy]
        if isinstance(_tools, Unset):
            tools = UNSET
        else:
            tools = MCPToolPolicy.from_dict(_tools)

        mcp_protocol_rule = cls(
            tools=tools,
        )

        mcp_protocol_rule.additional_properties = d
        return mcp_protocol_rule

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
