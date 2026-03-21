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
    from ..models.cache_policy_spec import CachePolicySpec
    from ..models.projection_spec import ProjectionSpec


T = TypeVar("T", bound="CredentialBinding")


@_attrs_define
class CredentialBinding:
    """
    Attributes:
        ref (str): Stable credential binding reference matched by `credentialRef`.
        source_ref (str): Region-scoped credential source reference resolved by `manager`.
        projection (ProjectionSpec):
        cache_policy (Union[Unset, CachePolicySpec]):
    """

    ref: str
    source_ref: str
    projection: "ProjectionSpec"
    cache_policy: Union[Unset, "CachePolicySpec"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ref = self.ref

        source_ref = self.source_ref

        projection = self.projection.to_dict()

        cache_policy: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cache_policy, Unset):
            cache_policy = self.cache_policy.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ref": ref,
                "sourceRef": source_ref,
                "projection": projection,
            }
        )
        if cache_policy is not UNSET:
            field_dict["cachePolicy"] = cache_policy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cache_policy_spec import CachePolicySpec
        from ..models.projection_spec import ProjectionSpec

        d = dict(src_dict)
        ref = d.pop("ref")

        source_ref = d.pop("sourceRef")

        projection = ProjectionSpec.from_dict(d.pop("projection"))

        _cache_policy = d.pop("cachePolicy", UNSET)
        cache_policy: Union[Unset, CachePolicySpec]
        if isinstance(_cache_policy, Unset):
            cache_policy = UNSET
        else:
            cache_policy = CachePolicySpec.from_dict(_cache_policy)

        credential_binding = cls(
            ref=ref,
            source_ref=source_ref,
            projection=projection,
            cache_policy=cache_policy,
        )

        credential_binding.additional_properties = d
        return credential_binding

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
