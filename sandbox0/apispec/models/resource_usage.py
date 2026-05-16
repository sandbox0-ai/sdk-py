from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResourceUsage")


@_attrs_define
class ResourceUsage:
    """
    Attributes:
        cpu_percent (Union[Unset, float]):
        memory_rss (Union[Unset, int]):
        memory_vms (Union[Unset, int]):
        open_files (Union[Unset, int]):
        thread_count (Union[Unset, int]):
        container_memory_usage (Union[Unset, int]):
        container_memory_limit (Union[Unset, int]):
        container_memory_working_set (Union[Unset, int]):
        io_read_bytes (Union[Unset, int]):
        io_write_bytes (Union[Unset, int]):
        memory_bytes (Union[Unset, int]):
    """

    cpu_percent: Union[Unset, float] = UNSET
    memory_rss: Union[Unset, int] = UNSET
    memory_vms: Union[Unset, int] = UNSET
    open_files: Union[Unset, int] = UNSET
    thread_count: Union[Unset, int] = UNSET
    container_memory_usage: Union[Unset, int] = UNSET
    container_memory_limit: Union[Unset, int] = UNSET
    container_memory_working_set: Union[Unset, int] = UNSET
    io_read_bytes: Union[Unset, int] = UNSET
    io_write_bytes: Union[Unset, int] = UNSET
    memory_bytes: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cpu_percent = self.cpu_percent

        memory_rss = self.memory_rss

        memory_vms = self.memory_vms

        open_files = self.open_files

        thread_count = self.thread_count

        container_memory_usage = self.container_memory_usage

        container_memory_limit = self.container_memory_limit

        container_memory_working_set = self.container_memory_working_set

        io_read_bytes = self.io_read_bytes

        io_write_bytes = self.io_write_bytes

        memory_bytes = self.memory_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_percent is not UNSET:
            field_dict["cpu_percent"] = cpu_percent
        if memory_rss is not UNSET:
            field_dict["memory_rss"] = memory_rss
        if memory_vms is not UNSET:
            field_dict["memory_vms"] = memory_vms
        if open_files is not UNSET:
            field_dict["open_files"] = open_files
        if thread_count is not UNSET:
            field_dict["thread_count"] = thread_count
        if container_memory_usage is not UNSET:
            field_dict["container_memory_usage"] = container_memory_usage
        if container_memory_limit is not UNSET:
            field_dict["container_memory_limit"] = container_memory_limit
        if container_memory_working_set is not UNSET:
            field_dict["container_memory_working_set"] = container_memory_working_set
        if io_read_bytes is not UNSET:
            field_dict["io_read_bytes"] = io_read_bytes
        if io_write_bytes is not UNSET:
            field_dict["io_write_bytes"] = io_write_bytes
        if memory_bytes is not UNSET:
            field_dict["memory_bytes"] = memory_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cpu_percent = d.pop("cpu_percent", UNSET)

        memory_rss = d.pop("memory_rss", UNSET)

        memory_vms = d.pop("memory_vms", UNSET)

        open_files = d.pop("open_files", UNSET)

        thread_count = d.pop("thread_count", UNSET)

        container_memory_usage = d.pop("container_memory_usage", UNSET)

        container_memory_limit = d.pop("container_memory_limit", UNSET)

        container_memory_working_set = d.pop("container_memory_working_set", UNSET)

        io_read_bytes = d.pop("io_read_bytes", UNSET)

        io_write_bytes = d.pop("io_write_bytes", UNSET)

        memory_bytes = d.pop("memory_bytes", UNSET)

        resource_usage = cls(
            cpu_percent=cpu_percent,
            memory_rss=memory_rss,
            memory_vms=memory_vms,
            open_files=open_files,
            thread_count=thread_count,
            container_memory_usage=container_memory_usage,
            container_memory_limit=container_memory_limit,
            container_memory_working_set=container_memory_working_set,
            io_read_bytes=io_read_bytes,
            io_write_bytes=io_write_bytes,
            memory_bytes=memory_bytes,
        )

        resource_usage.additional_properties = d
        return resource_usage

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
