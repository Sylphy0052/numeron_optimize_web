import random
import sys
from typing import List

import numpy as np
import numpy.typing as npt

from ans.history import History


class AI:
    def __init__(self, digit: int, name: str = "test", ai_id: int = 0) -> None:
        self.digit = digit
        self.name = name
        self.ai_id = ai_id
        self.history: List[History] = list()
        self.option: List[List[int]] = list()
        self.weight: npt.NDArray[np.float16] = np.array(
            [1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.8], dtype=np.float16
        )
        self.is_first = True
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
        evaluation = 0.0
        # 0h0bの場合
        n00 = len(self.option)
        for n in opt:
            for opt_ in self.option:
                if n in opt_:
                    n00 -= 1

        # それ以外の場合
        n01, n02, n03, n04 = 0, 0, 0, 0
        n10, n11, n12, n13 = 0, 0, 0, 0
        n20, n21, n22, n30 = 0, 0, 0, 0
        for opt_list in self.option:
            hit_num, blow_num = 0, 0
            for i, n in enumerate(opt_list):
                if n == opt[i]:
                    hit_num += 1
                elif n in opt_list:
                    blow_num += 1
            if hit_num == 0 and blow_num == 1:
                n01 += 1
            elif hit_num == 0 and blow_num == 2:
                n02 += 1
            elif hit_num == 0 and blow_num == 3:
                n03 += 1
            elif hit_num == 0 and blow_num == 4:
                n04 += 1
            elif hit_num == 1 and blow_num == 0:
                n10 += 1
            elif hit_num == 1 and blow_num == 1:
                n11 += 1
            elif hit_num == 1 and blow_num == 2:
                n12 += 1
            elif hit_num == 1 and blow_num == 3:
                n13 += 1
            elif hit_num == 2 and blow_num == 0:
                n20 += 1
            elif hit_num == 2 and blow_num == 1:
                n21 += 1
            elif hit_num == 2 and blow_num == 2:
                n22 += 1
            elif hit_num == 3 and blow_num == 0:
                n30 += 1

        n_vector = np.array([n00, n01, n02, n03, n04, n10, n11, n12, n13, n20, n21, n22, n30])
        evaluation = np.dot(n_vector, self.weight)
        return evaluation

    def recommend_number(self) -> List[int]:
        if self.is_first:
            self.is_first = False
            return self.input_random()
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
