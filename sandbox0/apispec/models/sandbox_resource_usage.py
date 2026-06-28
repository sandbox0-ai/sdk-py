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
    from ..models.context_resource_usage import ContextResourceUsage


T = TypeVar("T", bound="SandboxResourceUsage")


@_attrs_define
class SandboxResourceUsage:
    """
    Attributes:
        container_memory_usage (Union[Unset, int]):
        container_memory_limit (Union[Unset, int]):
        container_memory_working_set (Union[Unset, int]):
        total_memory_rss (Union[Unset, int]):
        total_memory_vms (Union[Unset, int]):
        total_open_files (Union[Unset, int]):
        total_thread_count (Union[Unset, int]):
        total_io_read_bytes (Union[Unset, int]):
        total_io_write_bytes (Union[Unset, int]):
        context_count (Union[Unset, int]):
        running_context_count (Union[Unset, int]):
        paused_context_count (Union[Unset, int]):
        contexts (Union[Unset, list['ContextResourceUsage']]):
    """

    container_memory_usage: Union[Unset, int] = UNSET
    container_memory_limit: Union[Unset, int] = UNSET
    container_memory_working_set: Union[Unset, int] = UNSET
    total_memory_rss: Union[Unset, int] = UNSET
    total_memory_vms: Union[Unset, int] = UNSET
    total_open_files: Union[Unset, int] = UNSET
    total_thread_count: Union[Unset, int] = UNSET
    total_io_read_bytes: Union[Unset, int] = UNSET
    total_io_write_bytes: Union[Unset, int] = UNSET
    context_count: Union[Unset, int] = UNSET
    running_context_count: Union[Unset, int] = UNSET
    paused_context_count: Union[Unset, int] = UNSET
    contexts: Union[Unset, list["ContextResourceUsage"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container_memory_usage = self.container_memory_usage

        container_memory_limit = self.container_memory_limit

        container_memory_working_set = self.container_memory_working_set

        total_memory_rss = self.total_memory_rss

        total_memory_vms = self.total_memory_vms

        total_open_files = self.total_open_files

        total_thread_count = self.total_thread_count

        total_io_read_bytes = self.total_io_read_bytes

        total_io_write_bytes = self.total_io_write_bytes

        context_count = self.context_count

        running_context_count = self.running_context_count

        paused_context_count = self.paused_context_count

        contexts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = []
            for contexts_item_data in self.contexts:
                contexts_item = contexts_item_data.to_dict()
                contexts.append(contexts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if container_memory_usage is not UNSET:
            field_dict["container_memory_usage"] = container_memory_usage
        if container_memory_limit is not UNSET:
            field_dict["container_memory_limit"] = container_memory_limit
        if container_memory_working_set is not UNSET:
            field_dict["container_memory_working_set"] = container_memory_working_set
        if total_memory_rss is not UNSET:
            field_dict["total_memory_rss"] = total_memory_rss
        if total_memory_vms is not UNSET:
            field_dict["total_memory_vms"] = total_memory_vms
        if total_open_files is not UNSET:
            field_dict["total_open_files"] = total_open_files
        if total_thread_count is not UNSET:
            field_dict["total_thread_count"] = total_thread_count
        if total_io_read_bytes is not UNSET:
            field_dict["total_io_read_bytes"] = total_io_read_bytes
        if total_io_write_bytes is not UNSET:
            field_dict["total_io_write_bytes"] = total_io_write_bytes
        if context_count is not UNSET:
            field_dict["context_count"] = context_count
        if running_context_count is not UNSET:
            field_dict["running_context_count"] = running_context_count
        if paused_context_count is not UNSET:
            field_dict["paused_context_count"] = paused_context_count
        if contexts is not UNSET:
            field_dict["contexts"] = contexts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.context_resource_usage import ContextResourceUsage

        d = dict(src_dict)
        container_memory_usage = d.pop("container_memory_usage", UNSET)

        container_memory_limit = d.pop("container_memory_limit", UNSET)

        container_memory_working_set = d.pop("container_memory_working_set", UNSET)

        total_memory_rss = d.pop("total_memory_rss", UNSET)

        total_memory_vms = d.pop("total_memory_vms", UNSET)

        total_open_files = d.pop("total_open_files", UNSET)

        total_thread_count = d.pop("total_thread_count", UNSET)

        total_io_read_bytes = d.pop("total_io_read_bytes", UNSET)

        total_io_write_bytes = d.pop("total_io_write_bytes", UNSET)

        context_count = d.pop("context_count", UNSET)

        running_context_count = d.pop("running_context_count", UNSET)

        paused_context_count = d.pop("paused_context_count", UNSET)

        contexts = []
        _contexts = d.pop("contexts", UNSET)
        for contexts_item_data in _contexts or []:
            contexts_item = ContextResourceUsage.from_dict(contexts_item_data)

            contexts.append(contexts_item)

        sandbox_resource_usage = cls(
            container_memory_usage=container_memory_usage,
            container_memory_limit=container_memory_limit,
            container_memory_working_set=container_memory_working_set,
            total_memory_rss=total_memory_rss,
            total_memory_vms=total_memory_vms,
            total_open_files=total_open_files,
            total_thread_count=total_thread_count,
            total_io_read_bytes=total_io_read_bytes,
            total_io_write_bytes=total_io_write_bytes,
            context_count=context_count,
            running_context_count=running_context_count,
            paused_context_count=paused_context_count,
            contexts=contexts,
        )

        sandbox_resource_usage.additional_properties = d
        return sandbox_resource_usage

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
