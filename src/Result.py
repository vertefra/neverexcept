from typing import Generic, TypeGuard, TypeVar

RES = TypeVar("RES")
ERR = TypeVar("ERR")

class OkResult(Generic[RES]):
    _result: RES
    _error: None

    def __init__(self, result: RES) -> None:
        self._result = result
        self._error = None

    @property
    def result(self) -> RES:
        return self._result

class ErrResult(Generic[ERR]):
    _error: ERR
    _result: None

    def __init__(self, error: ERR) -> None:
        self._error = error
        self._result = None
    
    @property
    def error(self) -> ERR:
        return self._error

    
Result = OkResult[RES] | ErrResult[ERR]


def is_ok(res: Result[RES, ERR]) -> TypeGuard[OkResult[RES]]:
    return res._error == None

def is_err(res: Result[RES, ERR]) -> TypeGuard[ErrResult[ERR]]:
    return res._result == None