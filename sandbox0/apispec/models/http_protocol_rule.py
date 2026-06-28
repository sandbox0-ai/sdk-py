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
    from ..models.http_method_policy import HTTPMethodPolicy
    from ..models.http_path_policy import HTTPPathPolicy


T = TypeVar("T", bound="HTTPProtocolRule")


@_attrs_define
class HTTPProtocolRule:
    """HTTP request operation policy.

    Attributes:
        methods (Union[Unset, HTTPMethodPolicy]): HTTP method allow and deny lists.
        paths (Union[Unset, HTTPPathPolicy]): HTTP path allow and deny lists.
    """

    methods: Union[Unset, "HTTPMethodPolicy"] = UNSET
    paths: Union[Unset, "HTTPPathPolicy"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        methods: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = self.methods.to_dict()

        paths: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if methods is not UNSET:
            field_dict["methods"] = methods
        if paths is not UNSET:
            field_dict["paths"] = paths

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_method_policy import HTTPMethodPolicy
        from ..models.http_path_policy import HTTPPathPolicy

        d = dict(src_dict)
        _methods = d.pop("methods", UNSET)
        methods: Union[Unset, HTTPMethodPolicy]
        if isinstance(_methods, Unset):
            methods = UNSET
        else:
            methods = HTTPMethodPolicy.from_dict(_methods)

        _paths = d.pop("paths", UNSET)
        paths: Union[Unset, HTTPPathPolicy]
        if isinstance(_paths, Unset):
            paths = UNSET
        else:
            paths = HTTPPathPolicy.from_dict(_paths)

        http_protocol_rule = cls(
            methods=methods,
            paths=paths,
        )

        http_protocol_rule.additional_properties = d
        return http_protocol_rule

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
