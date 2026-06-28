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
    from ..models.identity import Identity


T = TypeVar("T", bound="SuccessIdentityListResponseData")


@_attrs_define
class SuccessIdentityListResponseData:
    """
    Attributes:
        identities (Union[Unset, list['Identity']]):
    """

    identities: Union[Unset, list["Identity"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identities: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.identities, Unset):
            identities = []
            for identities_item_data in self.identities:
                identities_item = identities_item_data.to_dict()
                identities.append(identities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identities is not UNSET:
            field_dict["identities"] = identities

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.identity import Identity

        d = dict(src_dict)
        identities = []
        _identities = d.pop("identities", UNSET)
        for identities_item_data in _identities or []:
            identities_item = Identity.from_dict(identities_item_data)

            identities.append(identities_item)

        success_identity_list_response_data = cls(
            identities=identities,
        )

        success_identity_list_response_data.additional_properties = d
        return success_identity_list_response_data

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
