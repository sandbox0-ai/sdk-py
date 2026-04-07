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
    from ..models.claim_mount_request import ClaimMountRequest
    from ..models.sandbox_config import SandboxConfig


T = TypeVar("T", bound="ClaimRequest")


@_attrs_define
class ClaimRequest:
    """
    Attributes:
        template (Union[Unset, str]):
        config (Union[Unset, SandboxConfig]):
        mounts (Union[Unset, list['ClaimMountRequest']]):
        wait_for_mounts (Union[Unset, bool]): When true, claim waits best-effort for requested bootstrap mounts to
            reach a terminal state before returning. The wait is bounded by
            `mount_wait_timeout_ms`.
             Default: False.
        mount_wait_timeout_ms (Union[Unset, int]): Optional best-effort wait budget in milliseconds for bootstrap
            mounts when `wait_for_mounts` is true.
    """

    template: Union[Unset, str] = UNSET
    config: Union[Unset, "SandboxConfig"] = UNSET
    mounts: Union[Unset, list["ClaimMountRequest"]] = UNSET
    wait_for_mounts: Union[Unset, bool] = False
    mount_wait_timeout_ms: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template = self.template

        config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        mounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)

        wait_for_mounts = self.wait_for_mounts

        mount_wait_timeout_ms = self.mount_wait_timeout_ms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if config is not UNSET:
            field_dict["config"] = config
        if mounts is not UNSET:
            field_dict["mounts"] = mounts
        if wait_for_mounts is not UNSET:
            field_dict["wait_for_mounts"] = wait_for_mounts
        if mount_wait_timeout_ms is not UNSET:
            field_dict["mount_wait_timeout_ms"] = mount_wait_timeout_ms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.claim_mount_request import ClaimMountRequest
        from ..models.sandbox_config import SandboxConfig

        d = dict(src_dict)
        template = d.pop("template", UNSET)

        _config = d.pop("config", UNSET)
        config: Union[Unset, SandboxConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = SandboxConfig.from_dict(_config)

        mounts = []
        _mounts = d.pop("mounts", UNSET)
        for mounts_item_data in _mounts or []:
            mounts_item = ClaimMountRequest.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        wait_for_mounts = d.pop("wait_for_mounts", UNSET)

        mount_wait_timeout_ms = d.pop("mount_wait_timeout_ms", UNSET)

        claim_request = cls(
            template=template,
            config=config,
            mounts=mounts,
            wait_for_mounts=wait_for_mounts,
            mount_wait_timeout_ms=mount_wait_timeout_ms,
        )

        claim_request.additional_properties = d
        return claim_request

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
