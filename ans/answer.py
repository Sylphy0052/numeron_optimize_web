import random
from typing import List


class Answer:
    def __init__(self, digit: int = 4) -> None:
        self.digit = digit
        self.ans_list: List[int] = list()
        while len(self.ans_list) < digit:
            ans_d = random.randint(0, 9)
            if ans_d not in self.ans_list:
                self.ans_list.append(ans_d)
        self.ans = ""
        for ans_d in self.ans_list:
            self.ans += str(ans_d)

    def __repr__(self) -> str:
        return f"ans={self.ans}"
