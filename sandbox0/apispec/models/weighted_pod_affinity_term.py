from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.pod_affinity_term import PodAffinityTerm


T = TypeVar("T", bound="WeightedPodAffinityTerm")


@_attrs_define
class WeightedPodAffinityTerm:
    """
    Attributes:
        weight (int):
        pod_affinity_term (PodAffinityTerm):
    """

    weight: int
    pod_affinity_term: "PodAffinityTerm"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight = self.weight

        pod_affinity_term = self.pod_affinity_term.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "weight": weight,
                "podAffinityTerm": pod_affinity_term,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pod_affinity_term import PodAffinityTerm

        d = dict(src_dict)
        weight = d.pop("weight")

        pod_affinity_term = PodAffinityTerm.from_dict(d.pop("podAffinityTerm"))

        weighted_pod_affinity_term = cls(
            weight=weight,
            pod_affinity_term=pod_affinity_term,
        )

        weighted_pod_affinity_term.additional_properties = d
        return weighted_pod_affinity_term

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
