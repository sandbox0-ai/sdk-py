from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.http_header import HTTPHeader





T = TypeVar("T", bound="HTTPGetAction")



@_attrs_define
class HTTPGetAction:
    """ 
        Attributes:
            port (int):
            path (Union[Unset, str]):
            host (Union[Unset, str]):
            scheme (Union[Unset, str]):
            http_headers (Union[Unset, list['HTTPHeader']]):
     """

    port: int
    path: Union[Unset, str] = UNSET
    host: Union[Unset, str] = UNSET
    scheme: Union[Unset, str] = UNSET
    http_headers: Union[Unset, list['HTTPHeader']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.http_header import HTTPHeader
        port = self.port

        path = self.path

        host = self.host

        scheme = self.scheme

        http_headers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.http_headers, Unset):
            http_headers = []
            for http_headers_item_data in self.http_headers:
                http_headers_item = http_headers_item_data.to_dict()
                http_headers.append(http_headers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "port": port,
        })
        if path is not UNSET:
            field_dict["path"] = path
        if host is not UNSET:
            field_dict["host"] = host
        if scheme is not UNSET:
            field_dict["scheme"] = scheme
        if http_headers is not UNSET:
            field_dict["httpHeaders"] = http_headers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_header import HTTPHeader
        d = dict(src_dict)
        port = d.pop("port")

        path = d.pop("path", UNSET)

        host = d.pop("host", UNSET)

        scheme = d.pop("scheme", UNSET)

        http_headers = []
        _http_headers = d.pop("httpHeaders", UNSET)
        for http_headers_item_data in (_http_headers or []):
            http_headers_item = HTTPHeader.from_dict(http_headers_item_data)



            http_headers.append(http_headers_item)


        http_get_action = cls(
            port=port,
            path=path,
            host=host,
            scheme=scheme,
            http_headers=http_headers,
        )


        http_get_action.additional_properties = d
        return http_get_action

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
