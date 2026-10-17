from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="SandboxRootFSForkLaunchRequest")


@_attrs_define
class SandboxRootFSForkLaunchRequest:
    """
    Attributes:
        fork_operation_id (str):
        filesystem_id (str):
        head_generation_id (str):
        writer_epoch (int):
    """

    fork_operation_id: str
    filesystem_id: str
    head_generation_id: str
    writer_epoch: int

    def to_dict(self) -> dict[str, Any]:
        fork_operation_id = self.fork_operation_id

        filesystem_id = self.filesystem_id

        head_generation_id = self.head_generation_id

        writer_epoch = self.writer_epoch

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fork_operation_id": fork_operation_id,
                "filesystem_id": filesystem_id,
                "head_generation_id": head_generation_id,
                "writer_epoch": writer_epoch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fork_operation_id = d.pop("fork_operation_id")

        filesystem_id = d.pop("filesystem_id")

        head_generation_id = d.pop("head_generation_id")

        writer_epoch = d.pop("writer_epoch")

        sandbox_root_fs_fork_launch_request = cls(
            fork_operation_id=fork_operation_id,
            filesystem_id=filesystem_id,
            head_generation_id=head_generation_id,
            writer_epoch=writer_epoch,
        )

        return sandbox_root_fs_fork_launch_request
