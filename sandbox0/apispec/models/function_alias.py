import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FunctionAlias")


@_attrs_define
class FunctionAlias:
    """
    Attributes:
        function_id (str):
        alias (str):
        revision_id (str):
        revision_number (int):
        updated_at (datetime.datetime):
        updated_by (Union[Unset, str]):
    """

    function_id: str
    alias: str
    revision_id: str
    revision_number: int
    updated_at: datetime.datetime
    updated_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_id = self.function_id

        alias = self.alias

        revision_id = self.revision_id

        revision_number = self.revision_number

        updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function_id": function_id,
                "alias": alias,
                "revision_id": revision_id,
                "revision_number": revision_number,
                "updated_at": updated_at,
            }
        )
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        function_id = d.pop("function_id")

        alias = d.pop("alias")

        revision_id = d.pop("revision_id")

        revision_number = d.pop("revision_number")

        updated_at = isoparse(d.pop("updated_at"))

        updated_by = d.pop("updated_by", UNSET)

        function_alias = cls(
            function_id=function_id,
            alias=alias,
            revision_id=revision_id,
            revision_number=revision_number,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        function_alias.additional_properties = d
        return function_alias

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
