import sys

from src import Result, OkResult, ErrResult, is_err, is_ok
class MyErr:
    message: str
    def __init__(self, m: str) -> None:
        self.message = m

def parse_int(val: str) -> Result[int, MyErr]:
    try:
        parsed = int(val)
        return OkResult(parsed)
    except Exception as exc:
        message = f"Error while parsing {val}: {exc}"
        return ErrResult(MyErr(message))


def main() -> None:

    val = sys.argv[1]

    parse_result = parse_int(val)

    if is_err(parse_result):
        # error type narrowed to `MyErr`
        error = parse_result.error

        # As `MyErr` class, a message property is present with
        # The error message

        print(error.message)

    if is_ok(parse_result):
        # result type narrowed to `int`
        result = parse_result.result
        print(f'Parsed {result} to {type(result)}')

    

if __name__ == '__main__':
    main()