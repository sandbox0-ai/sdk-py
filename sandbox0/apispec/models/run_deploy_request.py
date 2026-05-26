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
  from ..models.run_revision_spec import RunRevisionSpec
  from ..models.run_source import RunSource





T = TypeVar("T", bound="RunDeployRequest")



@_attrs_define
class RunDeployRequest:
    """ 
        Attributes:
            name (Union[Unset, str]):
            slug (Union[Unset, str]):
            scale (Union[Unset, RunScalePolicy]): Scale-to-zero policy. Runs do not have a minimum idle instance count.
            source (Union[Unset, RunSource]):
            spec (Union[Unset, RunRevisionSpec]): Canonical runtime contract compiled from every run deploy mode.
            activate (Union[Unset, bool]):  Default: True.
     """

    name: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    scale: Union[Unset, 'RunScalePolicy'] = UNSET
    source: Union[Unset, 'RunSource'] = UNSET
    spec: Union[Unset, 'RunRevisionSpec'] = UNSET
    activate: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.run_scale_policy import RunScalePolicy
        from ..models.run_revision_spec import RunRevisionSpec
        from ..models.run_source import RunSource
        name = self.name

        slug = self.slug

        scale: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scale, Unset):
            scale = self.scale.to_dict()

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        spec: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        activate = self.activate


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if slug is not UNSET:
            field_dict["slug"] = slug
        if scale is not UNSET:
            field_dict["scale"] = scale
        if source is not UNSET:
            field_dict["source"] = source
        if spec is not UNSET:
            field_dict["spec"] = spec
        if activate is not UNSET:
            field_dict["activate"] = activate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.run_scale_policy import RunScalePolicy
        from ..models.run_revision_spec import RunRevisionSpec
        from ..models.run_source import RunSource
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        slug = d.pop("slug", UNSET)

        _scale = d.pop("scale", UNSET)
        scale: Union[Unset, RunScalePolicy]
        if isinstance(_scale,  Unset):
            scale = UNSET
        else:
            scale = RunScalePolicy.from_dict(_scale)




        _source = d.pop("source", UNSET)
        source: Union[Unset, RunSource]
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = RunSource.from_dict(_source)




        _spec = d.pop("spec", UNSET)
        spec: Union[Unset, RunRevisionSpec]
        if isinstance(_spec,  Unset):
            spec = UNSET
        else:
            spec = RunRevisionSpec.from_dict(_spec)




        activate = d.pop("activate", UNSET)

        run_deploy_request = cls(
            name=name,
            slug=slug,
            scale=scale,
            source=source,
            spec=spec,
            activate=activate,
        )


        run_deploy_request.additional_properties = d
        return run_deploy_request

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
