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
    from ..models.app_armor_profile import AppArmorProfile
    from ..models.capabilities import Capabilities
    from ..models.seccomp_profile import SeccompProfile


T = TypeVar("T", bound="SecurityContext")


@_attrs_define
class SecurityContext:
    """
    Attributes:
        capabilities (Union[Unset, Capabilities]):
        privileged (Union[Unset, bool]):
        run_as_user (Union[Unset, int]):
        run_as_group (Union[Unset, int]):
        run_as_non_root (Union[Unset, bool]):
        read_only_root_filesystem (Union[Unset, bool]):
        allow_privilege_escalation (Union[Unset, bool]):
        seccomp_profile (Union[Unset, SeccompProfile]):
        app_armor_profile (Union[Unset, AppArmorProfile]):
    """

    capabilities: Union[Unset, "Capabilities"] = UNSET
    privileged: Union[Unset, bool] = UNSET
    run_as_user: Union[Unset, int] = UNSET
    run_as_group: Union[Unset, int] = UNSET
    run_as_non_root: Union[Unset, bool] = UNSET
    read_only_root_filesystem: Union[Unset, bool] = UNSET
    allow_privilege_escalation: Union[Unset, bool] = UNSET
    seccomp_profile: Union[Unset, "SeccompProfile"] = UNSET
    app_armor_profile: Union[Unset, "AppArmorProfile"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        privileged = self.privileged

        run_as_user = self.run_as_user

        run_as_group = self.run_as_group

        run_as_non_root = self.run_as_non_root

        read_only_root_filesystem = self.read_only_root_filesystem

        allow_privilege_escalation = self.allow_privilege_escalation

        seccomp_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.seccomp_profile, Unset):
            seccomp_profile = self.seccomp_profile.to_dict()

        app_armor_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.app_armor_profile, Unset):
            app_armor_profile = self.app_armor_profile.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if privileged is not UNSET:
            field_dict["privileged"] = privileged
        if run_as_user is not UNSET:
            field_dict["runAsUser"] = run_as_user
        if run_as_group is not UNSET:
            field_dict["runAsGroup"] = run_as_group
        if run_as_non_root is not UNSET:
            field_dict["runAsNonRoot"] = run_as_non_root
        if read_only_root_filesystem is not UNSET:
            field_dict["readOnlyRootFilesystem"] = read_only_root_filesystem
        if allow_privilege_escalation is not UNSET:
            field_dict["allowPrivilegeEscalation"] = allow_privilege_escalation
        if seccomp_profile is not UNSET:
            field_dict["seccompProfile"] = seccomp_profile
        if app_armor_profile is not UNSET:
            field_dict["appArmorProfile"] = app_armor_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_armor_profile import AppArmorProfile
        from ..models.capabilities import Capabilities
        from ..models.seccomp_profile import SeccompProfile

        d = dict(src_dict)
        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, Capabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = Capabilities.from_dict(_capabilities)

        privileged = d.pop("privileged", UNSET)

        run_as_user = d.pop("runAsUser", UNSET)

        run_as_group = d.pop("runAsGroup", UNSET)

        run_as_non_root = d.pop("runAsNonRoot", UNSET)

        read_only_root_filesystem = d.pop("readOnlyRootFilesystem", UNSET)

        allow_privilege_escalation = d.pop("allowPrivilegeEscalation", UNSET)

        _seccomp_profile = d.pop("seccompProfile", UNSET)
        seccomp_profile: Union[Unset, SeccompProfile]
        if isinstance(_seccomp_profile, Unset):
            seccomp_profile = UNSET
        else:
            seccomp_profile = SeccompProfile.from_dict(_seccomp_profile)

        _app_armor_profile = d.pop("appArmorProfile", UNSET)
        app_armor_profile: Union[Unset, AppArmorProfile]
        if isinstance(_app_armor_profile, Unset):
            app_armor_profile = UNSET
        else:
            app_armor_profile = AppArmorProfile.from_dict(_app_armor_profile)

        security_context = cls(
            capabilities=capabilities,
            privileged=privileged,
            run_as_user=run_as_user,
            run_as_group=run_as_group,
            run_as_non_root=run_as_non_root,
            read_only_root_filesystem=read_only_root_filesystem,
            allow_privilege_escalation=allow_privilege_escalation,
            seccomp_profile=seccomp_profile,
            app_armor_profile=app_armor_profile,
        )

        security_context.additional_properties = d
        return security_context

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
