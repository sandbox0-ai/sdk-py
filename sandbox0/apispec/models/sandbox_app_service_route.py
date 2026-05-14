from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.public_gateway_auth import PublicGatewayAuth
    from ..models.public_gateway_cors import PublicGatewayCORS
    from ..models.public_gateway_rate_limit import PublicGatewayRateLimit


T = TypeVar("T", bound="SandboxAppServiceRoute")


@_attrs_define
class SandboxAppServiceRoute:
    """
    Attributes:
        id (str):
        resume (bool):
        path_prefix (Union[Unset, str]):
        methods (Union[Unset, list[str]]):
        rewrite_prefix (Union[None, Unset, str]):
        auth (Union[Unset, PublicGatewayAuth]):
        cors (Union[Unset, PublicGatewayCORS]):
        rate_limit (Union[Unset, PublicGatewayRateLimit]):
        timeout_seconds (Union[Unset, int]):
    """

    id: str
    resume: bool
    path_prefix: Union[Unset, str] = UNSET
    methods: Union[Unset, list[str]] = UNSET
    rewrite_prefix: Union[None, Unset, str] = UNSET
    auth: Union[Unset, "PublicGatewayAuth"] = UNSET
    cors: Union[Unset, "PublicGatewayCORS"] = UNSET
    rate_limit: Union[Unset, "PublicGatewayRateLimit"] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        resume = self.resume

        path_prefix = self.path_prefix

        methods: Union[Unset, list[str]] = UNSET
        if not isinstance(self.methods, Unset):
            methods = self.methods

        rewrite_prefix: Union[None, Unset, str]
        if isinstance(self.rewrite_prefix, Unset):
            rewrite_prefix = UNSET
        else:
            rewrite_prefix = self.rewrite_prefix

        auth: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        cors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cors, Unset):
            cors = self.cors.to_dict()

        rate_limit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rate_limit, Unset):
            rate_limit = self.rate_limit.to_dict()

        timeout_seconds = self.timeout_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "resume": resume,
            }
        )
        if path_prefix is not UNSET:
            field_dict["path_prefix"] = path_prefix
        if methods is not UNSET:
            field_dict["methods"] = methods
        if rewrite_prefix is not UNSET:
            field_dict["rewrite_prefix"] = rewrite_prefix
        if auth is not UNSET:
            field_dict["auth"] = auth
        if cors is not UNSET:
            field_dict["cors"] = cors
        if rate_limit is not UNSET:
            field_dict["rate_limit"] = rate_limit
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_gateway_auth import PublicGatewayAuth
        from ..models.public_gateway_cors import PublicGatewayCORS
        from ..models.public_gateway_rate_limit import PublicGatewayRateLimit

        d = dict(src_dict)
        id = d.pop("id")

        resume = d.pop("resume")

        path_prefix = d.pop("path_prefix", UNSET)

        methods = cast(list[str], d.pop("methods", UNSET))

        def _parse_rewrite_prefix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rewrite_prefix = _parse_rewrite_prefix(d.pop("rewrite_prefix", UNSET))

        _auth = d.pop("auth", UNSET)
        auth: Union[Unset, PublicGatewayAuth]
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = PublicGatewayAuth.from_dict(_auth)

        _cors = d.pop("cors", UNSET)
        cors: Union[Unset, PublicGatewayCORS]
        if isinstance(_cors, Unset):
            cors = UNSET
        else:
            cors = PublicGatewayCORS.from_dict(_cors)

        _rate_limit = d.pop("rate_limit", UNSET)
        rate_limit: Union[Unset, PublicGatewayRateLimit]
        if isinstance(_rate_limit, Unset):
            rate_limit = UNSET
        else:
            rate_limit = PublicGatewayRateLimit.from_dict(_rate_limit)

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        sandbox_app_service_route = cls(
            id=id,
            resume=resume,
            path_prefix=path_prefix,
            methods=methods,
            rewrite_prefix=rewrite_prefix,
            auth=auth,
            cors=cors,
            rate_limit=rate_limit,
            timeout_seconds=timeout_seconds,
        )

        sandbox_app_service_route.additional_properties = d
        return sandbox_app_service_route

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
