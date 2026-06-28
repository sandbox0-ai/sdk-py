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
    from ..models.exec_candidate import ExecCandidate
    from ..models.repl_env_var import REPLEnvVar
    from ..models.repl_prompt_config import REPLPromptConfig
    from ..models.repl_ready_config import REPLReadyConfig


T = TypeVar("T", bound="REPLConfig")


@_attrs_define
class REPLConfig:
    """
    Attributes:
        name (str):
        candidates (list['ExecCandidate']):
        display_name (Union[Unset, str]):
        description (Union[Unset, str]):
        env (Union[Unset, list['REPLEnvVar']]):
        default_term (Union[Unset, str]):
        prompt (Union[Unset, REPLPromptConfig]):
        ready (Union[Unset, REPLReadyConfig]):
    """

    name: str
    candidates: list["ExecCandidate"]
    display_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    env: Union[Unset, list["REPLEnvVar"]] = UNSET
    default_term: Union[Unset, str] = UNSET
    prompt: Union[Unset, "REPLPromptConfig"] = UNSET
    ready: Union[Unset, "REPLReadyConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        display_name = self.display_name

        description = self.description

        env: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.env, Unset):
            env = []
            for env_item_data in self.env:
                env_item = env_item_data.to_dict()
                env.append(env_item)

        default_term = self.default_term

        prompt: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.prompt, Unset):
            prompt = self.prompt.to_dict()

        ready: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ready, Unset):
            ready = self.ready.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "candidates": candidates,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if description is not UNSET:
            field_dict["description"] = description
        if env is not UNSET:
            field_dict["env"] = env
        if default_term is not UNSET:
            field_dict["default_term"] = default_term
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if ready is not UNSET:
            field_dict["ready"] = ready

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exec_candidate import ExecCandidate
        from ..models.repl_env_var import REPLEnvVar
        from ..models.repl_prompt_config import REPLPromptConfig
        from ..models.repl_ready_config import REPLReadyConfig

        d = dict(src_dict)
        name = d.pop("name")

        candidates = []
        _candidates = d.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = ExecCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        display_name = d.pop("display_name", UNSET)

        description = d.pop("description", UNSET)

        env = []
        _env = d.pop("env", UNSET)
        for env_item_data in _env or []:
            env_item = REPLEnvVar.from_dict(env_item_data)

            env.append(env_item)

        default_term = d.pop("default_term", UNSET)

        _prompt = d.pop("prompt", UNSET)
        prompt: Union[Unset, REPLPromptConfig]
        if isinstance(_prompt, Unset):
            prompt = UNSET
        else:
            prompt = REPLPromptConfig.from_dict(_prompt)

        _ready = d.pop("ready", UNSET)
        ready: Union[Unset, REPLReadyConfig]
        if isinstance(_ready, Unset):
            ready = UNSET
        else:
            ready = REPLReadyConfig.from_dict(_ready)

        repl_config = cls(
            name=name,
            candidates=candidates,
            display_name=display_name,
            description=description,
            env=env,
            default_term=default_term,
            prompt=prompt,
            ready=ready,
        )

        repl_config.additional_properties = d
        return repl_config

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
