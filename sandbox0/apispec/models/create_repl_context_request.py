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
    from ..models.repl_config import REPLConfig


T = TypeVar("T", bound="CreateREPLContextRequest")


@_attrs_define
class CreateREPLContextRequest:
    """
    Attributes:
        alias (Union[Unset, str]): Alias for the REPL or CLI tool (e.g., python, node, bash, redis-cli)
        input_ (Union[Unset, str]):
        repl_config (Union[Unset, REPLConfig]):
    """

    alias: Union[Unset, str] = UNSET
    input_: Union[Unset, str] = UNSET
    repl_config: Union[Unset, "REPLConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alias = self.alias

        input_ = self.input_

        repl_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.repl_config, Unset):
            repl_config = self.repl_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alias is not UNSET:
            field_dict["alias"] = alias
        if input_ is not UNSET:
            field_dict["input"] = input_
        if repl_config is not UNSET:
            field_dict["repl_config"] = repl_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repl_config import REPLConfig

        d = dict(src_dict)
        alias = d.pop("alias", UNSET)

        input_ = d.pop("input", UNSET)

        _repl_config = d.pop("repl_config", UNSET)
        repl_config: Union[Unset, REPLConfig]
        if isinstance(_repl_config, Unset):
            repl_config = UNSET
        else:
            repl_config = REPLConfig.from_dict(_repl_config)

        create_repl_context_request = cls(
            alias=alias,
            input_=input_,
            repl_config=repl_config,
        )

        create_repl_context_request.additional_properties = d
        return create_repl_context_request

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
