from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.function_alias import FunctionAlias
    from ..models.function_record import FunctionRecord
    from ..models.function_revision import FunctionRevision


T = TypeVar("T", bound="SuccessFunctionCreateResponseData")


@_attrs_define
class SuccessFunctionCreateResponseData:
    """
    Attributes:
        function (FunctionRecord):
        revision (FunctionRevision):
        alias (FunctionAlias):
    """

    function: "FunctionRecord"
    revision: "FunctionRevision"
    alias: "FunctionAlias"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function = self.function.to_dict()

        revision = self.revision.to_dict()

        alias = self.alias.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "function": function,
                "revision": revision,
                "alias": alias,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_alias import FunctionAlias
        from ..models.function_record import FunctionRecord
        from ..models.function_revision import FunctionRevision

        d = dict(src_dict)
        function = FunctionRecord.from_dict(d.pop("function"))

        revision = FunctionRevision.from_dict(d.pop("revision"))

        alias = FunctionAlias.from_dict(d.pop("alias"))

        success_function_create_response_data = cls(
            function=function,
            revision=revision,
            alias=alias,
        )

        success_function_create_response_data.additional_properties = d
        return success_function_create_response_data

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
