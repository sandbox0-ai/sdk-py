import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
    cast,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_health_observation_reason import SandboxHealthObservationReason
from ..models.sandbox_health_observation_source import SandboxHealthObservationSource
from ..models.sandbox_health_observation_state import SandboxHealthObservationState

T = TypeVar("T", bound="SandboxHealthObservation")


@_attrs_define
class SandboxHealthObservation:
    """
    Attributes:
        state (SandboxHealthObservationState):
        reason (SandboxHealthObservationReason): Fixed explanation code; no raw backend error or guest output.
        source (SandboxHealthObservationSource): Evidence origin. Guest evidence and its clock are workload-controlled
            and advisory.
        observed_at (Union[None, datetime.datetime]): Original observation time, including cached guest observations;
            null when unobserved.
    """

    state: SandboxHealthObservationState
    reason: SandboxHealthObservationReason
    source: SandboxHealthObservationSource
    observed_at: Union[None, datetime.datetime]

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        reason = self.reason.value

        source = self.source.value

        observed_at: Union[None, str]
        if isinstance(self.observed_at, datetime.datetime):
            observed_at = self.observed_at.isoformat()
        else:
            observed_at = self.observed_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "state": state,
                "reason": reason,
                "source": source,
                "observed_at": observed_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = SandboxHealthObservationState(d.pop("state"))

        reason = SandboxHealthObservationReason(d.pop("reason"))

        source = SandboxHealthObservationSource(d.pop("source"))

        def _parse_observed_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observed_at_type_0 = isoparse(data)

                return observed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        observed_at = _parse_observed_at(d.pop("observed_at"))

        sandbox_health_observation = cls(
            state=state,
            reason=reason,
            source=source,
            observed_at=observed_at,
        )

        return sandbox_health_observation
