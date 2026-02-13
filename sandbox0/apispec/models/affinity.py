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
    from ..models.node_affinity import NodeAffinity
    from ..models.pod_affinity import PodAffinity


T = TypeVar("T", bound="Affinity")


@_attrs_define
class Affinity:
    """
    Attributes:
        node_affinity (Union[Unset, NodeAffinity]):
        pod_affinity (Union[Unset, PodAffinity]):
    """

    node_affinity: Union[Unset, "NodeAffinity"] = UNSET
    pod_affinity: Union[Unset, "PodAffinity"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_affinity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.node_affinity, Unset):
            node_affinity = self.node_affinity.to_dict()

        pod_affinity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pod_affinity, Unset):
            pod_affinity = self.pod_affinity.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_affinity is not UNSET:
            field_dict["nodeAffinity"] = node_affinity
        if pod_affinity is not UNSET:
            field_dict["podAffinity"] = pod_affinity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_affinity import NodeAffinity
        from ..models.pod_affinity import PodAffinity

        d = dict(src_dict)
        _node_affinity = d.pop("nodeAffinity", UNSET)
        node_affinity: Union[Unset, NodeAffinity]
        if isinstance(_node_affinity, Unset):
            node_affinity = UNSET
        else:
            node_affinity = NodeAffinity.from_dict(_node_affinity)

        _pod_affinity = d.pop("podAffinity", UNSET)
        pod_affinity: Union[Unset, PodAffinity]
        if isinstance(_pod_affinity, Unset):
            pod_affinity = UNSET
        else:
            pod_affinity = PodAffinity.from_dict(_pod_affinity)

        affinity = cls(
            node_affinity=node_affinity,
            pod_affinity=pod_affinity,
        )

        affinity.additional_properties = d
        return affinity

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
