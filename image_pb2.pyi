from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ["columns", "data", "rows"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columns: int
    data: bytes
    rows: int
    def __init__(self, data: _Optional[bytes] = ..., rows: _Optional[int] = ..., columns: _Optional[int] = ...) -> None: ...

class PointCloud(_message.Message):
    __slots__ = ["columns", "data", "depth", "rows"]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DEPTH_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    columns: int
    data: bytes
    depth: int
    rows: int
    def __init__(self, data: _Optional[bytes] = ..., rows: _Optional[int] = ..., columns: _Optional[int] = ..., depth: _Optional[int] = ...) -> None: ...

class Processed(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
