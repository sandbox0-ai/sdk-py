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
    from ..models.object_meta import ObjectMeta
    from ..models.sandbox_template_spec import SandboxTemplateSpec
    from ..models.sandbox_template_status import SandboxTemplateStatus


T = TypeVar("T", bound="SandboxTemplate")


@_attrs_define
class SandboxTemplate:
    """
    Attributes:
        api_version (Union[Unset, str]):
        kind (Union[Unset, str]):
        metadata (Union[Unset, ObjectMeta]):
        spec (Union[Unset, SandboxTemplateSpec]):
        status (Union[Unset, SandboxTemplateStatus]):
    """

    api_version: Union[Unset, str] = UNSET
    kind: Union[Unset, str] = UNSET
    metadata: Union[Unset, "ObjectMeta"] = UNSET
    spec: Union[Unset, "SandboxTemplateSpec"] = UNSET
    status: Union[Unset, "SandboxTemplateStatus"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_version = self.api_version

        kind = self.kind

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        spec: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version
        if kind is not UNSET:
            field_dict["kind"] = kind
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_meta import ObjectMeta
        from ..models.sandbox_template_spec import SandboxTemplateSpec
        from ..models.sandbox_template_status import SandboxTemplateStatus

        d = dict(src_dict)
        api_version = d.pop("apiVersion", UNSET)

        kind = d.pop("kind", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ObjectMeta]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ObjectMeta.from_dict(_metadata)

        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, SandboxTemplateSpec]
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = SandboxTemplateSpec.from_dict(_spec)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SandboxTemplateStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SandboxTemplateStatus.from_dict(_status)

        sandbox_template = cls(
            api_version=api_version,
            kind=kind,
            metadata=metadata,
            spec=spec,
            status=status,
        )

        sandbox_template.additional_properties = d
        return sandbox_template

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
