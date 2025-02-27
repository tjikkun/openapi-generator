# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from petstore_api.models.animal import Animal
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MixedPropertiesAndAdditionalPropertiesClass(BaseModel):
    """
    MixedPropertiesAndAdditionalPropertiesClass
    """ # noqa: E501
    uuid: Optional[StrictStr] = None
    date_time: Optional[datetime] = Field(default=None, alias="dateTime")
    map: Optional[Dict[str, Animal]] = None
    __properties: ClassVar[List[str]] = ["uuid", "dateTime", "map"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MixedPropertiesAndAdditionalPropertiesClass from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in map (dict)
        _field_dict = {}
        if self.map:
            for _key in self.map:
                if self.map[_key]:
                    _field_dict[_key] = self.map[_key].to_dict()
            _dict['map'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MixedPropertiesAndAdditionalPropertiesClass from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "dateTime": obj.get("dateTime"),
            "map": dict(
                (_k, Animal.from_dict(_v))
                for _k, _v in obj.get("map").items()
            )
            if obj.get("map") is not None
            else None
        })
        return _obj


