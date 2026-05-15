from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_content_response_encoding import FileContentResponseEncoding
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileContentResponse")


@_attrs_define
class FileContentResponse:
    """
    Attributes:
        content (Union[Unset, str]):
        encoding (Union[Unset, FileContentResponseEncoding]):
    """

    content: Union[Unset, str] = UNSET
    encoding: Union[Unset, FileContentResponseEncoding] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        encoding: Union[Unset, str] = UNSET
        if not isinstance(self.encoding, Unset):
            encoding = self.encoding.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if encoding is not UNSET:
            field_dict["encoding"] = encoding

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        _encoding = d.pop("encoding", UNSET)
        encoding: Union[Unset, FileContentResponseEncoding]
        if isinstance(_encoding, Unset):
            encoding = UNSET
        else:
            encoding = FileContentResponseEncoding(_encoding)

        file_content_response = cls(
            content=content,
            encoding=encoding,
        )

        file_content_response.additional_properties = d
        return file_content_response

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
