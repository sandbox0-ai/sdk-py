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
    from ..models.capabilities import Capabilities


T = TypeVar("T", bound="SecurityContext")


@_attrs_define
class SecurityContext:
    """
    Attributes:
        capabilities (Union[Unset, Capabilities]):
        run_as_user (Union[Unset, int]):
        run_as_group (Union[Unset, int]):
    """

    capabilities: Union[Unset, "Capabilities"] = UNSET
    run_as_user: Union[Unset, int] = UNSET
    run_as_group: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        run_as_user = self.run_as_user

        run_as_group = self.run_as_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if run_as_user is not UNSET:
            field_dict["runAsUser"] = run_as_user
        if run_as_group is not UNSET:
            field_dict["runAsGroup"] = run_as_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capabilities import Capabilities

        d = dict(src_dict)
        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, Capabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = Capabilities.from_dict(_capabilities)

        run_as_user = d.pop("runAsUser", UNSET)

        run_as_group = d.pop("runAsGroup", UNSET)

        security_context = cls(
            capabilities=capabilities,
            run_as_user=run_as_user,
            run_as_group=run_as_group,
        )

        security_context.additional_properties = d
        return security_context

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
