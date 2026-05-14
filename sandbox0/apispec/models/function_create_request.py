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
    from ..models.function_source_request import FunctionSourceRequest


T = TypeVar("T", bound="FunctionCreateRequest")


@_attrs_define
class FunctionCreateRequest:
    """
    Attributes:
        source (FunctionSourceRequest):
        name (Union[Unset, str]): Function display name. Defaults to the source service name or ID when omitted.
    """

    source: "FunctionSourceRequest"
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_source_request import FunctionSourceRequest

        d = dict(src_dict)
        source = FunctionSourceRequest.from_dict(d.pop("source"))

        name = d.pop("name", UNSET)

        function_create_request = cls(
            source=source,
            name=name,
        )

        function_create_request.additional_properties = d
        return function_create_request

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
