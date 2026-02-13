from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClaimResponse")


@_attrs_define
class ClaimResponse:
    """
    Attributes:
        sandbox_id (str):
        status (str):
        pod_name (str):
        template (str):
        cluster_id (Union[None, Unset, str]):
    """

    sandbox_id: str
    status: str
    pod_name: str
    template: str
    cluster_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sandbox_id = self.sandbox_id

        status = self.status

        pod_name = self.pod_name

        template = self.template

        cluster_id: Union[None, Unset, str]
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = self.cluster_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sandbox_id": sandbox_id,
                "status": status,
                "pod_name": pod_name,
                "template": template,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sandbox_id = d.pop("sandbox_id")

        status = d.pop("status")

        pod_name = d.pop("pod_name")

        template = d.pop("template")

        def _parse_cluster_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        claim_response = cls(
            sandbox_id=sandbox_id,
            status=status,
            pod_name=pod_name,
            template=template,
            cluster_id=cluster_id,
        )

        claim_response.additional_properties = d
        return claim_response

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
