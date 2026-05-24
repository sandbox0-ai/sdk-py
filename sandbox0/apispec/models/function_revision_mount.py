from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.function_revision_mount_mode import FunctionRevisionMountMode
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.function_revision_mount_source import FunctionRevisionMountSource





T = TypeVar("T", bound="FunctionRevisionMount")



@_attrs_define
class FunctionRevisionMount:
    """
        Attributes:
            mount_point (str):
            source (FunctionRevisionMountSource):
            name (Union[Unset, str]):
            mode (Union[Unset, FunctionRevisionMountMode]):
            materialization (Union[Unset, str]): Optional materialization policy such as fork_per_runtime for future
                artifact/volume flows.
     """

    mount_point: str
    source: 'FunctionRevisionMountSource'
    name: Union[Unset, str] = UNSET
    mode: Union[Unset, FunctionRevisionMountMode] = UNSET
    materialization: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.function_revision_mount_source import FunctionRevisionMountSource
        mount_point = self.mount_point

        source = self.source.to_dict()

        name = self.name

        mode: Union[Unset, str] = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        materialization = self.materialization


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "mount_point": mount_point,
            "source": source,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if materialization is not UNSET:
            field_dict["materialization"] = materialization

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.function_revision_mount_source import FunctionRevisionMountSource
        d = dict(src_dict)
        mount_point = d.pop("mount_point")

        source = FunctionRevisionMountSource.from_dict(d.pop("source"))




        name = d.pop("name", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: Union[Unset, FunctionRevisionMountMode]
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = FunctionRevisionMountMode(_mode)




        materialization = d.pop("materialization", UNSET)

        function_revision_mount = cls(
            mount_point=mount_point,
            source=source,
            name=name,
            mode=mode,
            materialization=materialization,
        )


        function_revision_mount.additional_properties = d
        return function_revision_mount

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
