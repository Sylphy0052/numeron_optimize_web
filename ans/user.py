from typing import List


class User:
    def __init__(self, digit: int, name: str = "test", user_id: int = 0) -> None:
        self.digit = digit
        self.name = name
        self.user_id = user_id

    def input_num(self) -> List[int]:
        input_number: List[int] = list()
        err = True
        while err:
            err = False
            input_str = input(f"Input {self.digit} digit number> ")
            input_str = input_str.rstrip()
            if len(input_str) != self.digit:
                print(f"Please input {self.digit} digit number!")
                err = True
                continue
            for s in input_str:
                try:
                    s_int = int(s)
                except Exception:
                    print("Please input number!")
                    input_number = list()
                    err = True
                    break
                input_number.append(s_int)
        return input_number

    def __repr__(self) -> str:
        return f"User{self.user_id}: {self.name}"
