from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.function_revision import FunctionRevision


T = TypeVar("T", bound="SuccessFunctionRevisionCreateResponseData")


@_attrs_define
class SuccessFunctionRevisionCreateResponseData:
    """
    Attributes:
        revision (FunctionRevision):
        promoted (bool):
    """

    revision: "FunctionRevision"
    promoted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revision = self.revision.to_dict()

        promoted = self.promoted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "revision": revision,
                "promoted": promoted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_revision import FunctionRevision

        d = dict(src_dict)
        revision = FunctionRevision.from_dict(d.pop("revision"))

        promoted = d.pop("promoted")

        success_function_revision_create_response_data = cls(
            revision=revision,
            promoted=promoted,
        )

        success_function_revision_create_response_data.additional_properties = d
        return success_function_revision_create_response_data

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
