import random
from typing import List, Tuple


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

    def answer(self, number: List[int]) -> Tuple[int, int]:
        n_hit, n_blow = 0, 0
        for i, n in enumerate(number):
            if n == self.ans_list[i]:
                n_hit += 1
            elif n in self.ans_list:
                n_blow += 1
        return n_hit, n_blow

    def __repr__(self) -> str:
        return f"ans={self.ans}"
