from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.function_revision import FunctionRevision





T = TypeVar("T", bound="SuccessFunctionRevisionListResponseData")



@_attrs_define
class SuccessFunctionRevisionListResponseData:
    """ 
        Attributes:
            revisions (list['FunctionRevision']):
     """

    revisions: list['FunctionRevision']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_revision import FunctionRevision
        revisions = []
        for revisions_item_data in self.revisions:
            revisions_item = revisions_item_data.to_dict()
            revisions.append(revisions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "revisions": revisions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_revision import FunctionRevision
        d = dict(src_dict)
        revisions = []
        _revisions = d.pop("revisions")
        for revisions_item_data in (_revisions):
            revisions_item = FunctionRevision.from_dict(revisions_item_data)



            revisions.append(revisions_item)


        success_function_revision_list_response_data = cls(
            revisions=revisions,
        )


        success_function_revision_list_response_data.additional_properties = d
        return success_function_revision_list_response_data

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
