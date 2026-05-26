from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="SnapshotFunctionSource")



@_attrs_define
class SnapshotFunctionSource:
    """ 
        Attributes:
            snapshot_ids (Union[Unset, list[str]]):
     """

    snapshot_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        snapshot_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.snapshot_ids, Unset):
            snapshot_ids = self.snapshot_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if snapshot_ids is not UNSET:
            field_dict["snapshot_ids"] = snapshot_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        snapshot_ids = cast(list[str], d.pop("snapshot_ids", UNSET))


        snapshot_function_source = cls(
            snapshot_ids=snapshot_ids,
        )


        snapshot_function_source.additional_properties = d
        return snapshot_function_source

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
