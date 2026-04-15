from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SandboxLogs")


@_attrs_define
class SandboxLogs:
    """
    Attributes:
        sandbox_id (str):
        pod_name (str):
        container (str):
        previous (bool):
        logs (str): Log text returned by Kubernetes for the selected container.
    """

    sandbox_id: str
    pod_name: str
    container: str
    previous: bool
    logs: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        pod_name = self.pod_name

        container = self.container

        previous = self.previous

        logs = self.logs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "pod_name": pod_name,
                "container": container,
                "previous": previous,
                "logs": logs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        pod_name = d.pop("pod_name")

        container = d.pop("container")

        previous = d.pop("previous")

        logs = d.pop("logs")

        sandbox_logs = cls(
            sandbox_id=sandbox_id,
            pod_name=pod_name,
            container=container,
            previous=previous,
            logs=logs,
        )

        sandbox_logs.additional_properties = d
        return sandbox_logs

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
