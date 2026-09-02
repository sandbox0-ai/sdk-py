from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    TypeVar,
    Union,
)

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
        data (Union['FileContentResponse', 'FileInfo', 'SuccessFileReadResponseDataType1']):
    """

    success: bool
    data: Union["FileContentResponse", "FileInfo", "SuccessFileReadResponseDataType1"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_info import FileInfo
        from ..models.success_file_read_response_data_type_1 import (
            SuccessFileReadResponseDataType1,
        )

        success = self.success

        data: dict[str, Any]
        if isinstance(self.data, FileInfo):
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
                "data": data,
            }
        )

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
            "FileContentResponse", "FileInfo", "SuccessFileReadResponseDataType1"
        ]:
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

        data = _parse_data(d.pop("data"))

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
