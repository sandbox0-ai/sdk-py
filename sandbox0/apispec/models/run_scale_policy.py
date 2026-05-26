from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RunScalePolicy")



@_attrs_define
class RunScalePolicy:
    """ Scale-to-zero policy. Runs do not have a minimum idle instance count.

        Attributes:
            max_instances (Union[Unset, int]):  Default: 1.
            target_concurrency (Union[Unset, int]):  Default: 1.
            idle_timeout_seconds (Union[Unset, int]): Seconds of inactivity before the runtime sandbox can scale back to
                zero. Default: 300.
            startup_timeout_seconds (Union[Unset, int]): Maximum seconds to wait for a cold-started service health check.
                Default: 90.
     """

    max_instances: Union[Unset, int] = 1
    target_concurrency: Union[Unset, int] = 1
    idle_timeout_seconds: Union[Unset, int] = 300
    startup_timeout_seconds: Union[Unset, int] = 90
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        max_instances = self.max_instances

        target_concurrency = self.target_concurrency

        idle_timeout_seconds = self.idle_timeout_seconds

        startup_timeout_seconds = self.startup_timeout_seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_instances is not UNSET:
            field_dict["max_instances"] = max_instances
        if target_concurrency is not UNSET:
            field_dict["target_concurrency"] = target_concurrency
        if idle_timeout_seconds is not UNSET:
            field_dict["idle_timeout_seconds"] = idle_timeout_seconds
        if startup_timeout_seconds is not UNSET:
            field_dict["startup_timeout_seconds"] = startup_timeout_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_instances = d.pop("max_instances", UNSET)

        target_concurrency = d.pop("target_concurrency", UNSET)

        idle_timeout_seconds = d.pop("idle_timeout_seconds", UNSET)

        startup_timeout_seconds = d.pop("startup_timeout_seconds", UNSET)

        run_scale_policy = cls(
            max_instances=max_instances,
            target_concurrency=target_concurrency,
            idle_timeout_seconds=idle_timeout_seconds,
            startup_timeout_seconds=startup_timeout_seconds,
        )


        run_scale_policy.additional_properties = d
        return run_scale_policy

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
