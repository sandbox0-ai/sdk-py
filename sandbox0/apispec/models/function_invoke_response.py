from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.function_invoke_response_headers import FunctionInvokeResponseHeaders





T = TypeVar("T", bound="FunctionInvokeResponse")



@_attrs_define
class FunctionInvokeResponse:
    """ 
        Attributes:
            status (int): Function-level HTTP-style status code.
            headers (Union[Unset, FunctionInvokeResponseHeaders]):
            body_base64 (Union[Unset, str]): Base64-encoded function response body.
     """

    status: int
    headers: Union[Unset, 'FunctionInvokeResponseHeaders'] = UNSET
    body_base64: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_invoke_response_headers import FunctionInvokeResponseHeaders
        status = self.status

        headers: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        body_base64 = self.body_base64


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })
        if headers is not UNSET:
            field_dict["headers"] = headers
        if body_base64 is not UNSET:
            field_dict["body_base64"] = body_base64

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_invoke_response_headers import FunctionInvokeResponseHeaders
        d = dict(src_dict)
        status = d.pop("status")

        _headers = d.pop("headers", UNSET)
        headers: Union[Unset, FunctionInvokeResponseHeaders]
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = FunctionInvokeResponseHeaders.from_dict(_headers)




        body_base64 = d.pop("body_base64", UNSET)

        function_invoke_response = cls(
            status=status,
            headers=headers,
            body_base64=body_base64,
        )


        function_invoke_response.additional_properties = d
        return function_invoke_response

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
