import dataclasses
from typing import List


@dataclasses.dataclass
class History:
    turn: int
    input_number: List[int]
    n_hit: int
    n_blow: int
