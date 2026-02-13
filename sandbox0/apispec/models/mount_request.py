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
    from ..models.volume_config import VolumeConfig


T = TypeVar("T", bound="MountRequest")


@_attrs_define
class MountRequest:
    """
    Attributes:
        sandboxvolume_id (str):
        mount_point (str):
        sandbox_id (Union[Unset, str]):
        volume_config (Union[Unset, VolumeConfig]):
    """

    sandboxvolume_id: str
    mount_point: str
    sandbox_id: Union[Unset, str] = UNSET
    volume_config: Union[Unset, "VolumeConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandboxvolume_id = self.sandboxvolume_id

        mount_point = self.mount_point

        sandbox_id = self.sandbox_id

        volume_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.volume_config, Unset):
            volume_config = self.volume_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandboxvolume_id": sandboxvolume_id,
                "mount_point": mount_point,
            }
        )
        if sandbox_id is not UNSET:
            field_dict["sandbox_id"] = sandbox_id
        if volume_config is not UNSET:
            field_dict["volume_config"] = volume_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.volume_config import VolumeConfig

        d = dict(src_dict)
        sandboxvolume_id = d.pop("sandboxvolume_id")

        mount_point = d.pop("mount_point")

        sandbox_id = d.pop("sandbox_id", UNSET)

        _volume_config = d.pop("volume_config", UNSET)
        volume_config: Union[Unset, VolumeConfig]
        if isinstance(_volume_config, Unset):
            volume_config = UNSET
        else:
            volume_config = VolumeConfig.from_dict(_volume_config)

        mount_request = cls(
            sandboxvolume_id=sandboxvolume_id,
            mount_point=mount_point,
            sandbox_id=sandbox_id,
            volume_config=volume_config,
        )

        mount_request.additional_properties = d
        return mount_request

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
