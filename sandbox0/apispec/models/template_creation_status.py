import datetime
from collections.abc import Mapping
from typing import (
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.template_creation_status_stage import TemplateCreationStatusStage
from ..models.template_creation_status_state import TemplateCreationStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCreationStatus")


@_attrs_define
class TemplateCreationStatus:
    """Asynchronous creation status for templates built from a sandbox.
    Traditional image-based templates omit this object and are ready
    immediately after creation. Ready means the template is visible in at
    least one data-plane cluster and the claim API accepts it; when the
    pool is zero, it does not imply that a sandbox image has already been
    pulled.

        Attributes:
            state (TemplateCreationStatusState):
            stage (TemplateCreationStatusStage):
            started_at (Union[Unset, datetime.datetime]):
            captured_at (Union[Unset, datetime.datetime]):
            completed_at (Union[Unset, datetime.datetime]):
            output_image (Union[Unset, str]): Digest-pinned image reference published to the configured team registry.
            reason (Union[Unset, str]):
            message (Union[Unset, str]):
    """

    state: TemplateCreationStatusState
    stage: TemplateCreationStatusStage
    started_at: Union[Unset, datetime.datetime] = UNSET
    captured_at: Union[Unset, datetime.datetime] = UNSET
    completed_at: Union[Unset, datetime.datetime] = UNSET
    output_image: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        stage = self.stage.value

        started_at: Union[Unset, str] = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        captured_at: Union[Unset, str] = UNSET
        if not isinstance(self.captured_at, Unset):
            captured_at = self.captured_at.isoformat()

        completed_at: Union[Unset, str] = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()

        output_image = self.output_image

        reason = self.reason

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "stage": stage,
            }
        )
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if captured_at is not UNSET:
            field_dict["capturedAt"] = captured_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if output_image is not UNSET:
            field_dict["outputImage"] = output_image
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = TemplateCreationStatusState(d.pop("state"))

        stage = TemplateCreationStatusStage(d.pop("stage"))

        _started_at = d.pop("startedAt", UNSET)
        started_at: Union[Unset, datetime.datetime]
        if isinstance(_started_at, Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)

        _captured_at = d.pop("capturedAt", UNSET)
        captured_at: Union[Unset, datetime.datetime]
        if isinstance(_captured_at, Unset):
            captured_at = UNSET
        else:
            captured_at = isoparse(_captured_at)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: Union[Unset, datetime.datetime]
        if isinstance(_completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)

        output_image = d.pop("outputImage", UNSET)

        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        template_creation_status = cls(
            state=state,
            stage=stage,
            started_at=started_at,
            captured_at=captured_at,
            completed_at=completed_at,
            output_image=output_image,
            reason=reason,
            message=message,
        )

        template_creation_status.additional_properties = d
        return template_creation_status

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
