from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.placeholder_replacement import PlaceholderReplacement





T = TypeVar("T", bound="PlaceholderSubstitutionProjection")



@_attrs_define
class PlaceholderSubstitutionProjection:
    """ 
        Attributes:
            replacements (Union[Unset, list['PlaceholderReplacement']]): Placeholder replacements applied to outbound HTTP
                requests at the egress boundary.
     """

    replacements: Union[Unset, list['PlaceholderReplacement']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.placeholder_replacement import PlaceholderReplacement
        replacements: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.replacements, Unset):
            replacements = []
            for replacements_item_data in self.replacements:
                replacements_item = replacements_item_data.to_dict()
                replacements.append(replacements_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if replacements is not UNSET:
            field_dict["replacements"] = replacements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.placeholder_replacement import PlaceholderReplacement
        d = dict(src_dict)
        replacements = []
        _replacements = d.pop("replacements", UNSET)
        for replacements_item_data in (_replacements or []):
            replacements_item = PlaceholderReplacement.from_dict(replacements_item_data)



            replacements.append(replacements_item)


        placeholder_substitution_projection = cls(
            replacements=replacements,
        )


        placeholder_substitution_projection.additional_properties = d
        return placeholder_substitution_projection

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
