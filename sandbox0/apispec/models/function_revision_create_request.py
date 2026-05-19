from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.function_source_request import FunctionSourceRequest





T = TypeVar("T", bound="FunctionRevisionCreateRequest")



@_attrs_define
class FunctionRevisionCreateRequest:
    """ 
        Attributes:
            source (FunctionSourceRequest):
            promote (Union[Unset, bool]): Whether to move the production alias to the new revision. Default: True.
     """

    source: 'FunctionSourceRequest'
    promote: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_source_request import FunctionSourceRequest
        source = self.source.to_dict()

        promote = self.promote


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "source": source,
        })
        if promote is not UNSET:
            field_dict["promote"] = promote

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_source_request import FunctionSourceRequest
        d = dict(src_dict)
        source = FunctionSourceRequest.from_dict(d.pop("source"))




        promote = d.pop("promote", UNSET)

        function_revision_create_request = cls(
            source=source,
            promote=promote,
        )


        function_revision_create_request.additional_properties = d
        return function_revision_create_request

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
