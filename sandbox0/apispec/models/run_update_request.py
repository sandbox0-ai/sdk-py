from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.run_scale_policy import RunScalePolicy





T = TypeVar("T", bound="RunUpdateRequest")



@_attrs_define
class RunUpdateRequest:
    """ 
        Attributes:
            name (Union[Unset, str]):
            enabled (Union[Unset, bool]):
            scale (Union[Unset, RunScalePolicy]): Scale-to-zero policy. Runs do not have a minimum idle instance count.
     """

    name: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    scale: Union[Unset, 'RunScalePolicy'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_scale_policy import RunScalePolicy
        name = self.name

        enabled = self.enabled

        scale: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if scale is not UNSET:
            field_dict["scale"] = scale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_scale_policy import RunScalePolicy
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _scale = d.pop("scale", UNSET)
        scale: Union[Unset, RunScalePolicy]
        if isinstance(_scale,  Unset):
            scale = UNSET
        else:
            scale = RunScalePolicy.from_dict(_scale)




        run_update_request = cls(
            name=name,
            enabled=enabled,
            scale=scale,
        )


        run_update_request.additional_properties = d
        return run_update_request

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
