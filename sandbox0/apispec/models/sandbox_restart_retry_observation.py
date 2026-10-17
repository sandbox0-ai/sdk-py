import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.sandbox_restart_retry_observation_blocked_reason import (
    SandboxRestartRetryObservationBlockedReason,
)
from ..models.sandbox_restart_retry_observation_observed_stage import (
    SandboxRestartRetryObservationObservedStage,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SandboxRestartRetryObservation")


@_attrs_define
class SandboxRestartRetryObservation:
    """
    Attributes:
        attempts (int):
        observed_at (Union[Unset, datetime.datetime]):
        observed_stage (Union[Unset, SandboxRestartRetryObservationObservedStage]):
        next_attempt_at (Union[Unset, datetime.datetime]):
        blocked_reason (Union[Unset, SandboxRestartRetryObservationBlockedReason]): Fixed diagnostic code for the
            current stage. storage_not_writable means the host could not provide a writable RootFS and does not identify the
            underlying cause or authorize repair. No raw node errors, credentials, or topology are exposed.
    """

    attempts: int
    observed_at: Union[Unset, datetime.datetime] = UNSET
    observed_stage: Union[Unset, SandboxRestartRetryObservationObservedStage] = UNSET
    next_attempt_at: Union[Unset, datetime.datetime] = UNSET
    blocked_reason: Union[Unset, SandboxRestartRetryObservationBlockedReason] = UNSET

    def to_dict(self) -> dict[str, Any]:
        attempts = self.attempts

        observed_at: Union[Unset, str] = UNSET
        if not isinstance(self.observed_at, Unset):
            observed_at = self.observed_at.isoformat()

        observed_stage: Union[Unset, str] = UNSET
        if not isinstance(self.observed_stage, Unset):
            observed_stage = self.observed_stage.value

        next_attempt_at: Union[Unset, str] = UNSET
        if not isinstance(self.next_attempt_at, Unset):
            next_attempt_at = self.next_attempt_at.isoformat()

        blocked_reason: Union[Unset, str] = UNSET
        if not isinstance(self.blocked_reason, Unset):
            blocked_reason = self.blocked_reason.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "attempts": attempts,
            }
        )
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at
        if observed_stage is not UNSET:
            field_dict["observed_stage"] = observed_stage
        if next_attempt_at is not UNSET:
            field_dict["next_attempt_at"] = next_attempt_at
        if blocked_reason is not UNSET:
            field_dict["blocked_reason"] = blocked_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attempts = d.pop("attempts")

        _observed_at = d.pop("observed_at", UNSET)
        observed_at: Union[Unset, datetime.datetime]
        if isinstance(_observed_at, Unset):
            observed_at = UNSET
        else:
            observed_at = isoparse(_observed_at)

        _observed_stage = d.pop("observed_stage", UNSET)
        observed_stage: Union[Unset, SandboxRestartRetryObservationObservedStage]
        if isinstance(_observed_stage, Unset):
            observed_stage = UNSET
        else:
            observed_stage = SandboxRestartRetryObservationObservedStage(
                _observed_stage
            )

        _next_attempt_at = d.pop("next_attempt_at", UNSET)
        next_attempt_at: Union[Unset, datetime.datetime]
        if isinstance(_next_attempt_at, Unset):
            next_attempt_at = UNSET
        else:
            next_attempt_at = isoparse(_next_attempt_at)

        _blocked_reason = d.pop("blocked_reason", UNSET)
        blocked_reason: Union[Unset, SandboxRestartRetryObservationBlockedReason]
        if isinstance(_blocked_reason, Unset):
            blocked_reason = UNSET
        else:
            blocked_reason = SandboxRestartRetryObservationBlockedReason(
                _blocked_reason
            )

        sandbox_restart_retry_observation = cls(
            attempts=attempts,
            observed_at=observed_at,
            observed_stage=observed_stage,
            next_attempt_at=next_attempt_at,
            blocked_reason=blocked_reason,
        )

        return sandbox_restart_retry_observation
