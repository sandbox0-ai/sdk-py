from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_selector import LabelSelector


T = TypeVar("T", bound="PodAffinityTerm")


@_attrs_define
class PodAffinityTerm:
    """
    Attributes:
        topology_key (str):
        label_selector (Union[Unset, LabelSelector]):
        namespaces (Union[Unset, list[str]]):
    """

    topology_key: str
    label_selector: Union[Unset, "LabelSelector"] = UNSET
    namespaces: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topology_key = self.topology_key

        label_selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.label_selector, Unset):
            label_selector = self.label_selector.to_dict()

        namespaces: Union[Unset, list[str]] = UNSET
        if not isinstance(self.namespaces, Unset):
            namespaces = self.namespaces

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "topologyKey": topology_key,
            }
        )
        if label_selector is not UNSET:
            field_dict["labelSelector"] = label_selector
        if namespaces is not UNSET:
            field_dict["namespaces"] = namespaces

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_selector import LabelSelector

        d = dict(src_dict)
        topology_key = d.pop("topologyKey")

        _label_selector = d.pop("labelSelector", UNSET)
        label_selector: Union[Unset, LabelSelector]
        if isinstance(_label_selector, Unset):
            label_selector = UNSET
        else:
            label_selector = LabelSelector.from_dict(_label_selector)

        namespaces = cast(list[str], d.pop("namespaces", UNSET))

        pod_affinity_term = cls(
            topology_key=topology_key,
            label_selector=label_selector,
            namespaces=namespaces,
        )

        pod_affinity_term.additional_properties = d
        return pod_affinity_term

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
