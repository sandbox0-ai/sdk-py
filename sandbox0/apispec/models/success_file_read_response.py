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
    from ..models.file_content_response import FileContentResponse
    from ..models.file_info import FileInfo
    from ..models.success_file_read_response_data_type_1 import (
        SuccessFileReadResponseDataType1,
    )


T = TypeVar("T", bound="SuccessFileReadResponse")


@_attrs_define
class SuccessFileReadResponse:
    """
    Attributes:
        success (bool):
        data (Union['FileContentResponse', 'FileInfo', 'SuccessFileReadResponseDataType1', Unset]):
    """

    success: bool
    data: Union[
        "FileContentResponse", "FileInfo", "SuccessFileReadResponseDataType1", Unset
    ] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_info import FileInfo
        from ..models.success_file_read_response_data_type_1 import (
            SuccessFileReadResponseDataType1,
        )

        success = self.success

        data: Union[Unset, dict[str, Any]]
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, FileInfo):
            data = self.data.to_dict()
        elif isinstance(self.data, SuccessFileReadResponseDataType1):
            data = self.data.to_dict()
        else:
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_content_response import FileContentResponse
        from ..models.file_info import FileInfo
        from ..models.success_file_read_response_data_type_1 import (
            SuccessFileReadResponseDataType1,
        )

        d = dict(src_dict)
        success = d.pop("success")

        def _parse_data(
            data: object,
        ) -> Union[
            "FileContentResponse", "FileInfo", "SuccessFileReadResponseDataType1", Unset
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = FileInfo.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_1 = SuccessFileReadResponseDataType1.from_dict(data)

                return data_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_2 = FileContentResponse.from_dict(data)

            return data_type_2

        data = _parse_data(d.pop("data", UNSET))

        success_file_read_response = cls(
            success=success,
            data=data,
        )

        success_file_read_response.additional_properties = d
        return success_file_read_response

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
