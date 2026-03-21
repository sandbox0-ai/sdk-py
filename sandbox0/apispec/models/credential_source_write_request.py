from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.credential_source_resolver_kind import CredentialSourceResolverKind

if TYPE_CHECKING:
    from ..models.credential_source_write_spec import CredentialSourceWriteSpec


T = TypeVar("T", bound="CredentialSourceWriteRequest")


@_attrs_define
class CredentialSourceWriteRequest:
    """
    Attributes:
        name (str):
        resolver_kind (CredentialSourceResolverKind):
        spec (CredentialSourceWriteSpec):
    """

    name: str
    resolver_kind: CredentialSourceResolverKind
    spec: "CredentialSourceWriteSpec"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        resolver_kind = self.resolver_kind.value

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resolverKind": resolver_kind,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credential_source_write_spec import CredentialSourceWriteSpec

        d = dict(src_dict)
        name = d.pop("name")

        resolver_kind = CredentialSourceResolverKind(d.pop("resolverKind"))

        spec = CredentialSourceWriteSpec.from_dict(d.pop("spec"))

        credential_source_write_request = cls(
            name=name,
            resolver_kind=resolver_kind,
            spec=spec,
        )

        credential_source_write_request.additional_properties = d
        return credential_source_write_request

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
