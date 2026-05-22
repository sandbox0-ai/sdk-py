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
    from ..models.node_selector_requirement import NodeSelectorRequirement


T = TypeVar("T", bound="NodeSelectorTerm")


@_attrs_define
class NodeSelectorTerm:
    """
    Attributes:
        match_expressions (Union[Unset, list['NodeSelectorRequirement']]):
        match_fields (Union[Unset, list['NodeSelectorRequirement']]):
    """

    match_expressions: Union[Unset, list["NodeSelectorRequirement"]] = UNSET
    match_fields: Union[Unset, list["NodeSelectorRequirement"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_expressions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.match_expressions, Unset):
            match_expressions = []
            for match_expressions_item_data in self.match_expressions:
                match_expressions_item = match_expressions_item_data.to_dict()
                match_expressions.append(match_expressions_item)

        match_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.match_fields, Unset):
            match_fields = []
            for match_fields_item_data in self.match_fields:
                match_fields_item = match_fields_item_data.to_dict()
                match_fields.append(match_fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_expressions is not UNSET:
            field_dict["matchExpressions"] = match_expressions
        if match_fields is not UNSET:
            field_dict["matchFields"] = match_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_selector_requirement import NodeSelectorRequirement

        d = dict(src_dict)
        match_expressions = []
        _match_expressions = d.pop("matchExpressions", UNSET)
        for match_expressions_item_data in _match_expressions or []:
            match_expressions_item = NodeSelectorRequirement.from_dict(
                match_expressions_item_data
            )

            match_expressions.append(match_expressions_item)

        match_fields = []
        _match_fields = d.pop("matchFields", UNSET)
        for match_fields_item_data in _match_fields or []:
            match_fields_item = NodeSelectorRequirement.from_dict(
                match_fields_item_data
            )

            match_fields.append(match_fields_item)

        node_selector_term = cls(
            match_expressions=match_expressions,
            match_fields=match_fields,
        )

        node_selector_term.additional_properties = d
        return node_selector_term

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
