from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.http_value_match import HTTPValueMatch





T = TypeVar("T", bound="HTTPMatch")



@_attrs_define
class HTTPMatch:
    """ Request-level matcher for HTTP-family egress credential rules.

        Attributes:
            methods (Union[Unset, list[str]]): HTTP methods matched case-insensitively after uppercasing.
            paths (Union[Unset, list[str]]): Exact URL path matches.
            path_prefixes (Union[Unset, list[str]]): URL path prefix matches.
            query (Union[Unset, list['HTTPValueMatch']]): Decoded query parameter matchers.
            headers (Union[Unset, list['HTTPValueMatch']]): HTTP request header matchers.
     """

    methods: Union[Unset, list[str]] = UNSET
    paths: Union[Unset, list[str]] = UNSET
    path_prefixes: Union[Unset, list[str]] = UNSET
    query: Union[Unset, list['HTTPValueMatch']] = UNSET
    headers: Union[Unset, list['HTTPValueMatch']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.http_value_match import HTTPValueMatch
        methods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = self.methods



        paths: Union[Unset, list[str]] = UNSET
        if not isinstance(self.paths, Unset):
            paths = self.paths



        path_prefixes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.path_prefixes, Unset):
            path_prefixes = self.path_prefixes



        query: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.query, Unset):
            query = []
            for query_item_data in self.query:
                query_item = query_item_data.to_dict()
                query.append(query_item)



        headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = []
            for headers_item_data in self.headers:
                headers_item = headers_item_data.to_dict()
                headers.append(headers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if methods is not UNSET:
            field_dict["methods"] = methods
        if paths is not UNSET:
            field_dict["paths"] = paths
        if path_prefixes is not UNSET:
            field_dict["pathPrefixes"] = path_prefixes
        if query is not UNSET:
            field_dict["query"] = query
        if headers is not UNSET:
            field_dict["headers"] = headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_value_match import HTTPValueMatch
        d = dict(src_dict)
        methods = cast(list[str], d.pop("methods", UNSET))


        paths = cast(list[str], d.pop("paths", UNSET))


        path_prefixes = cast(list[str], d.pop("pathPrefixes", UNSET))


        query = []
        _query = d.pop("query", UNSET)
        for query_item_data in (_query or []):
            query_item = HTTPValueMatch.from_dict(query_item_data)



            query.append(query_item)


        headers = []
        _headers = d.pop("headers", UNSET)
        for headers_item_data in (_headers or []):
            headers_item = HTTPValueMatch.from_dict(headers_item_data)



            headers.append(headers_item)


        http_match = cls(
            methods=methods,
            paths=paths,
            path_prefixes=path_prefixes,
            query=query,
            headers=headers,
        )


        http_match.additional_properties = d
        return http_match

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
