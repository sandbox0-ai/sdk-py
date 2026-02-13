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
    from ..models.object_meta_annotations import ObjectMetaAnnotations
    from ..models.object_meta_labels import ObjectMetaLabels


T = TypeVar("T", bound="ObjectMeta")


@_attrs_define
class ObjectMeta:
    """
    Attributes:
        name (Union[Unset, str]):
        namespace (Union[Unset, str]):
        labels (Union[Unset, ObjectMetaLabels]):
        annotations (Union[Unset, ObjectMetaAnnotations]):
    """

    name: Union[Unset, str] = UNSET
    namespace: Union[Unset, str] = UNSET
    labels: Union[Unset, "ObjectMetaLabels"] = UNSET
    annotations: Union[Unset, "ObjectMetaAnnotations"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        namespace = self.namespace

        labels: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        annotations: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if labels is not UNSET:
            field_dict["labels"] = labels
        if annotations is not UNSET:
            field_dict["annotations"] = annotations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_meta_annotations import ObjectMetaAnnotations
        from ..models.object_meta_labels import ObjectMetaLabels

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        namespace = d.pop("namespace", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: Union[Unset, ObjectMetaLabels]
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = ObjectMetaLabels.from_dict(_labels)

        _annotations = d.pop("annotations", UNSET)
        annotations: Union[Unset, ObjectMetaAnnotations]
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ObjectMetaAnnotations.from_dict(_annotations)

        object_meta = cls(
            name=name,
            namespace=namespace,
            labels=labels,
            annotations=annotations,
        )

        object_meta.additional_properties = d
        return object_meta

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
