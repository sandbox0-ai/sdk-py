from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.function_invoke_request_headers import FunctionInvokeRequestHeaders
  from ..models.function_invoke_request_query import FunctionInvokeRequestQuery





T = TypeVar("T", bound="FunctionInvokeRequest")



@_attrs_define
class FunctionInvokeRequest:
    """ 
        Attributes:
            method (Union[Unset, str]): Logical request method passed to the function. Defaults to POST.
            path (Union[Unset, str]): Logical request path passed to the function. Defaults to /.
            query (Union[Unset, FunctionInvokeRequestQuery]):
            headers (Union[Unset, FunctionInvokeRequestHeaders]):
            body_base64 (Union[Unset, str]): Base64-encoded request body passed to the function.
            handler (Union[Unset, str]): Python handler name inside the function module. Defaults to handler.
            timeout_ms (Union[Unset, int]): Per-invocation timeout in milliseconds. Defaults to 30000 and must not exceed
                120000.
     """

    method: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    query: Union[Unset, 'FunctionInvokeRequestQuery'] = UNSET
    headers: Union[Unset, 'FunctionInvokeRequestHeaders'] = UNSET
    body_base64: Union[Unset, str] = UNSET
    handler: Union[Unset, str] = UNSET
    timeout_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_invoke_request_headers import FunctionInvokeRequestHeaders
        from ..models.function_invoke_request_query import FunctionInvokeRequestQuery
        method = self.method

        path = self.path

        query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        body_base64 = self.body_base64

        handler = self.handler

        timeout_ms = self.timeout_ms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if query is not UNSET:
            field_dict["query"] = query
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body_base64 is not UNSET:
            field_dict["body_base64"] = body_base64
        if handler is not UNSET:
            field_dict["handler"] = handler
        if timeout_ms is not UNSET:
            field_dict["timeout_ms"] = timeout_ms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_invoke_request_headers import FunctionInvokeRequestHeaders
        from ..models.function_invoke_request_query import FunctionInvokeRequestQuery
        d = dict(src_dict)
        method = d.pop("method", UNSET)

        path = d.pop("path", UNSET)

        _query = d.pop("query", UNSET)
        query: Union[Unset, FunctionInvokeRequestQuery]
        if isinstance(_query,  Unset):
            query = UNSET
        else:
            query = FunctionInvokeRequestQuery.from_dict(_query)




        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, FunctionInvokeRequestHeaders]
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = FunctionInvokeRequestHeaders.from_dict(_headers)




        body_base64 = d.pop("body_base64", UNSET)

        handler = d.pop("handler", UNSET)

        timeout_ms = d.pop("timeout_ms", UNSET)

        function_invoke_request = cls(
            method=method,
            path=path,
            query=query,
            headers=headers,
            body_base64=body_base64,
            handler=handler,
            timeout_ms=timeout_ms,
        )


        function_invoke_request.additional_properties = d
        return function_invoke_request

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
