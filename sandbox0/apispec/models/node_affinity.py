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
    from ..models.node_selector import NodeSelector
    from ..models.preferred_scheduling_term import PreferredSchedulingTerm


T = TypeVar("T", bound="NodeAffinity")


@_attrs_define
class NodeAffinity:
    """
    Attributes:
        required_during_scheduling_ignored_during_execution (Union[Unset, NodeSelector]):
        preferred_during_scheduling_ignored_during_execution (Union[Unset, list['PreferredSchedulingTerm']]):
    """

    required_during_scheduling_ignored_during_execution: Union[
        Unset, "NodeSelector"
    ] = UNSET
    preferred_during_scheduling_ignored_during_execution: Union[
        Unset, list["PreferredSchedulingTerm"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_during_scheduling_ignored_during_execution: Union[
            Unset, dict[str, Any]
        ] = UNSET
        if not isinstance(
            self.required_during_scheduling_ignored_during_execution, Unset
        ):
            required_during_scheduling_ignored_during_execution = (
                self.required_during_scheduling_ignored_during_execution.to_dict()
            )

        preferred_during_scheduling_ignored_during_execution: Union[
            Unset, list[dict[str, Any]]
        ] = UNSET
        if not isinstance(
            self.preferred_during_scheduling_ignored_during_execution, Unset
        ):
            preferred_during_scheduling_ignored_during_execution = []
            for (
                preferred_during_scheduling_ignored_during_execution_item_data
            ) in self.preferred_during_scheduling_ignored_during_execution:
                preferred_during_scheduling_ignored_during_execution_item = preferred_during_scheduling_ignored_during_execution_item_data.to_dict()
                preferred_during_scheduling_ignored_during_execution.append(
                    preferred_during_scheduling_ignored_during_execution_item
                )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_during_scheduling_ignored_during_execution is not UNSET:
            field_dict["requiredDuringSchedulingIgnoredDuringExecution"] = (
                required_during_scheduling_ignored_during_execution
            )
        if preferred_during_scheduling_ignored_during_execution is not UNSET:
            field_dict["preferredDuringSchedulingIgnoredDuringExecution"] = (
                preferred_during_scheduling_ignored_during_execution
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_selector import NodeSelector
        from ..models.preferred_scheduling_term import PreferredSchedulingTerm

        d = dict(src_dict)
        _required_during_scheduling_ignored_during_execution = d.pop(
            "requiredDuringSchedulingIgnoredDuringExecution", UNSET
        )
        required_during_scheduling_ignored_during_execution: Union[Unset, NodeSelector]
        if isinstance(_required_during_scheduling_ignored_during_execution, Unset):
            required_during_scheduling_ignored_during_execution = UNSET
        else:
            required_during_scheduling_ignored_during_execution = (
                NodeSelector.from_dict(
                    _required_during_scheduling_ignored_during_execution
                )
            )

        preferred_during_scheduling_ignored_during_execution = []
        _preferred_during_scheduling_ignored_during_execution = d.pop(
            "preferredDuringSchedulingIgnoredDuringExecution", UNSET
        )
        for preferred_during_scheduling_ignored_during_execution_item_data in (
            _preferred_during_scheduling_ignored_during_execution or []
        ):
            preferred_during_scheduling_ignored_during_execution_item = (
                PreferredSchedulingTerm.from_dict(
                    preferred_during_scheduling_ignored_during_execution_item_data
                )
            )

            preferred_during_scheduling_ignored_during_execution.append(
                preferred_during_scheduling_ignored_during_execution_item
            )

        node_affinity = cls(
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
        )

        node_affinity.additional_properties = d
        return node_affinity

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
