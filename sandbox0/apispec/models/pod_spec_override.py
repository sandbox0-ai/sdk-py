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
    from ..models.affinity import Affinity
    from ..models.pod_spec_override_node_selector import PodSpecOverrideNodeSelector
    from ..models.toleration import Toleration


T = TypeVar("T", bound="PodSpecOverride")


@_attrs_define
class PodSpecOverride:
    """
    Attributes:
        node_selector (Union[Unset, PodSpecOverrideNodeSelector]):
        affinity (Union[Unset, Affinity]):
        tolerations (Union[Unset, list['Toleration']]):
        service_account_name (Union[Unset, str]):
    """

    node_selector: Union[Unset, "PodSpecOverrideNodeSelector"] = UNSET
    affinity: Union[Unset, "Affinity"] = UNSET
    tolerations: Union[Unset, list["Toleration"]] = UNSET
    service_account_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_selector: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.node_selector, Unset):
            node_selector = self.node_selector.to_dict()

        affinity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.affinity, Unset):
            affinity = self.affinity.to_dict()

        tolerations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tolerations, Unset):
            tolerations = []
            for tolerations_item_data in self.tolerations:
                tolerations_item = tolerations_item_data.to_dict()
                tolerations.append(tolerations_item)

        service_account_name = self.service_account_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_selector is not UNSET:
            field_dict["nodeSelector"] = node_selector
        if affinity is not UNSET:
            field_dict["affinity"] = affinity
        if tolerations is not UNSET:
            field_dict["tolerations"] = tolerations
        if service_account_name is not UNSET:
            field_dict["serviceAccountName"] = service_account_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.affinity import Affinity
        from ..models.pod_spec_override_node_selector import PodSpecOverrideNodeSelector
        from ..models.toleration import Toleration

        d = dict(src_dict)
        _node_selector = d.pop("nodeSelector", UNSET)
        node_selector: Union[Unset, PodSpecOverrideNodeSelector]
        if isinstance(_node_selector, Unset):
            node_selector = UNSET
        else:
            node_selector = PodSpecOverrideNodeSelector.from_dict(_node_selector)

        _affinity = d.pop("affinity", UNSET)
        affinity: Union[Unset, Affinity]
        if isinstance(_affinity, Unset):
            affinity = UNSET
        else:
            affinity = Affinity.from_dict(_affinity)

        tolerations = []
        _tolerations = d.pop("tolerations", UNSET)
        for tolerations_item_data in _tolerations or []:
            tolerations_item = Toleration.from_dict(tolerations_item_data)

            tolerations.append(tolerations_item)

        service_account_name = d.pop("serviceAccountName", UNSET)

        pod_spec_override = cls(
            node_selector=node_selector,
            affinity=affinity,
            tolerations=tolerations,
            service_account_name=service_account_name,
        )

        pod_spec_override.additional_properties = d
        return pod_spec_override

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
