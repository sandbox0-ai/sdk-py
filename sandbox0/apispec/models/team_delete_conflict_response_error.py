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
    from ..models.team_delete_conflict_details import TeamDeleteConflictDetails


T = TypeVar("T", bound="TeamDeleteConflictResponseError")


@_attrs_define
class TeamDeleteConflictResponseError:
    """
    Attributes:
        code (str):
        message (str):
        details (Union[Unset, TeamDeleteConflictDetails]):
    """

    code: str
    message: str
    details: Union[Unset, "TeamDeleteConflictDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "message": message,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_delete_conflict_details import TeamDeleteConflictDetails

        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        _details = d.pop("details", UNSET)
        details: Union[Unset, TeamDeleteConflictDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = TeamDeleteConflictDetails.from_dict(_details)

        team_delete_conflict_response_error = cls(
            code=code,
            message=message,
            details=details,
        )

        team_delete_conflict_response_error.additional_properties = d
        return team_delete_conflict_response_error

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
