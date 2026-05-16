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
    from ..models.pod_affinity_term import PodAffinityTerm
    from ..models.weighted_pod_affinity_term import WeightedPodAffinityTerm


T = TypeVar("T", bound="PodAffinity")


@_attrs_define
class PodAffinity:
    """
    Attributes:
        required_during_scheduling_ignored_during_execution (Union[Unset, list['PodAffinityTerm']]):
        preferred_during_scheduling_ignored_during_execution (Union[Unset, list['WeightedPodAffinityTerm']]):
    """

    required_during_scheduling_ignored_during_execution: Union[
        Unset, list["PodAffinityTerm"]
    ] = UNSET
    preferred_during_scheduling_ignored_during_execution: Union[
        Unset, list["WeightedPodAffinityTerm"]
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_during_scheduling_ignored_during_execution: Union[
            Unset, list[dict[str, Any]]
        ] = UNSET
        if not isinstance(
            self.required_during_scheduling_ignored_during_execution, Unset
        ):
            required_during_scheduling_ignored_during_execution = []
            for (
                required_during_scheduling_ignored_during_execution_item_data
            ) in self.required_during_scheduling_ignored_during_execution:
                required_during_scheduling_ignored_during_execution_item = required_during_scheduling_ignored_during_execution_item_data.to_dict()
                required_during_scheduling_ignored_during_execution.append(
                    required_during_scheduling_ignored_during_execution_item
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
        from ..models.pod_affinity_term import PodAffinityTerm
        from ..models.weighted_pod_affinity_term import WeightedPodAffinityTerm

        d = dict(src_dict)
        required_during_scheduling_ignored_during_execution = []
        _required_during_scheduling_ignored_during_execution = d.pop(
            "requiredDuringSchedulingIgnoredDuringExecution", UNSET
        )
        for required_during_scheduling_ignored_during_execution_item_data in (
            _required_during_scheduling_ignored_during_execution or []
        ):
            required_during_scheduling_ignored_during_execution_item = (
                PodAffinityTerm.from_dict(
                    required_during_scheduling_ignored_during_execution_item_data
                )
            )

            required_during_scheduling_ignored_during_execution.append(
                required_during_scheduling_ignored_during_execution_item
            )

        preferred_during_scheduling_ignored_during_execution = []
        _preferred_during_scheduling_ignored_during_execution = d.pop(
            "preferredDuringSchedulingIgnoredDuringExecution", UNSET
        )
        for preferred_during_scheduling_ignored_during_execution_item_data in (
            _preferred_during_scheduling_ignored_during_execution or []
        ):
            preferred_during_scheduling_ignored_during_execution_item = (
                WeightedPodAffinityTerm.from_dict(
                    preferred_during_scheduling_ignored_during_execution_item_data
                )
            )

            preferred_during_scheduling_ignored_during_execution.append(
                preferred_during_scheduling_ignored_during_execution_item
            )

        pod_affinity = cls(
            required_during_scheduling_ignored_during_execution=required_during_scheduling_ignored_during_execution,
            preferred_during_scheduling_ignored_during_execution=preferred_during_scheduling_ignored_during_execution,
        )

        pod_affinity.additional_properties = d
        return pod_affinity

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
