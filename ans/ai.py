import random
import sys
from typing import List

from ans.history import History


class AI:
    def __init__(self, digit: int, name: str = "test", ai_id: int = 0) -> None:
        self.digit = digit
        self.name = name
        self.ai_id = ai_id
        self.history: List[History] = list()
        self.option: List[List[int]] = list()
        self._init_option()

    def _init_option(self) -> None:
        if self.digit == 4:
            for a in range(10):
                for b in range(10):
                    if b == a:
                        continue
                    for c in range(10):
                        if c == a or c == b:
                            continue
                        for d in range(10):
                            if d == a or d == b or d == c:
                                continue
                            self.option.append([a, b, c, d])

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

    def input_random(self) -> List[int]:
        input_number = random.choice(self.option)
        return input_number

    def _evaluate_opt(self, opt: List[int]) -> float:
        # 0h0bの場合
        # 0h1bの場合
        # 0h2bの場合
        # 0h3bの場合
        # 0h4bの場合
        # 1h0bの場合
        # 1h1bの場合
        # 1h2bの場合
        # 1h3bの場合
        # 2h0bの場合
        # 2h1bの場合
        # 2h2bの場合
        # 3h0bの場合
        pass

    def recommend_number(self) -> List[int]:
        min_eva = float(sys.maxsize)
        recommend_opt = self.option[0]
        for opt in self.option:
            evaluation = self._evaluate_opt(opt)
            if evaluation < min_eva:
                min_eva = evaluation
                recommend_opt = opt
        return recommend_opt

    def _remove_0h0b(self, input_num: List[int]) -> None:
        remove_index: List[int] = list()
        for n in input_num:
            for idx, l in enumerate(self.option):
                if n in l:
                    remove_index.append(idx)
        self.option = [opt for i, opt in enumerate(self.option) if i not in remove_index]

    def _remove_hit(self, input_num: List[int], n_hit: int) -> None:
        index_list: List[int] = list()
        for idx, opt_list in enumerate(self.option):
            hit_num = 0
            for i, n in enumerate(opt_list):
                if n == input_num[i]:
                    hit_num += 1
            if hit_num == n_hit:
                index_list.append(idx)
        self.option = [opt for i, opt in enumerate(self.option) if i in index_list]

    def _remove_blow(self, input_num: List[int], n_blow: int) -> None:
        index_list: List[int] = list()
        for idx, opt_list in enumerate(self.option):
            blow_num = 0
            for i, n in enumerate(input_num):
                if n in opt_list and n != opt_list[i]:
                    blow_num += 1
            if blow_num == n_blow:
                index_list.append(idx)
        self.option = [opt for i, opt in enumerate(self.option) if i in index_list]

    def feedback(self, input_num: List[int], n_hit: int, n_blow: int) -> None:
        history = History(turn=len(self.history) + 1, input_number=input_num, n_hit=n_hit, n_blow=n_blow)
        self.history.append(history)
        # 0H0Bの場合
        if n_hit == 0 and n_blow == 0:
            self._remove_0h0b(input_num)
        else:
            if n_hit > 0:
                self._remove_hit(input_num, n_hit)
            if n_blow > 0:
                self._remove_blow(input_num, n_blow)

    def print_option(self) -> None:
        for opt in self.option:
            print(opt)
        print(len(self.option))

    def __repr__(self) -> str:
        return f"AI{self.ai_id}: {self.name} ({len(self.option)})"
