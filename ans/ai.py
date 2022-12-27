from typing import List


class AI:
    def __init__(self, digit: int, name: str = "test", ai_id: int = 0) -> None:
        self.digit = digit
        self.name = name
        self.ai_id = ai_id

    def input_num(self) -> List[int]:
        err = True
        while err:
            err = False
            input_str = input(f"Input {self.digit} digit number> ")
            input_str = input_str.rstrip()
            if len(input_str) != self.digit:
                print(f"Please input {self.digit} digit number!")
                err = True
                continue
            input_number: List[int] = list()
            for s in input_str:
                try:
                    s_int = int(s)
                    if s_int in input_number:
                        print("Please input not same numbers!")
                        input_number = list()
                        err = True
                        break
                except Exception:
                    print("Please input number!")
                    input_number = list()
                    err = True
                    break
                input_number.append(s_int)
        return input_number

    def __repr__(self) -> str:
        return f"AI{self.ai_id}: {self.name}"
