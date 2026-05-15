from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.function_record import FunctionRecord





T = TypeVar("T", bound="SuccessFunctionListResponseData")



@_attrs_define
class SuccessFunctionListResponseData:
    """ 
        Attributes:
            functions (list['FunctionRecord']):
     """

    functions: list['FunctionRecord']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_record import FunctionRecord
        functions = []
        for functions_item_data in self.functions:
            functions_item = functions_item_data.to_dict()
            functions.append(functions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "functions": functions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_record import FunctionRecord
        d = dict(src_dict)
        functions = []
        _functions = d.pop("functions")
        for functions_item_data in (_functions):
            functions_item = FunctionRecord.from_dict(functions_item_data)



            functions.append(functions_item)


        success_function_list_response_data = cls(
            functions=functions,
        )


        success_function_list_response_data.additional_properties = d
        return success_function_list_response_data

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
