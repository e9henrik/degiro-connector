"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class Config(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    USER_TOKEN_FIELD_NUMBER: builtins.int
    AUTO_CONNECT_FIELD_NUMBER: builtins.int
    user_token: builtins.int = ...
    auto_connect: builtins.bool = ...
    def __init__(self,
        *,
        user_token : builtins.int = ...,
        auto_connect : builtins.bool = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"auto_connect",b"auto_connect",u"user_token",b"user_token"]) -> None: ...
global___Config = Config
