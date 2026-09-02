from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.claim_response import ClaimResponse


T = TypeVar("T", bound="SuccessClaimResponse")


@_attrs_define
class SuccessClaimResponse:
    """
    Attributes:
        success (bool):
        data (ClaimResponse):
    """

    success: bool
    data: "ClaimResponse"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_response import ClaimResponse

        d = dict(src_dict)
        success = d.pop("success")

        data = ClaimResponse.from_dict(d.pop("data"))

        success_claim_response = cls(
            success=success,
            data=data,
        )

        success_claim_response.additional_properties = d
        return success_claim_response

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
