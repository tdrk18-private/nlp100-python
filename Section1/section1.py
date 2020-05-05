from enum import Enum
from random import sample
from re import sub
from typing import List, Dict, Set


class NGramType(Enum):
    WORD = 1
    CHAR = 2


class Section1:
    @staticmethod
    def reverse(s: str) -> str:
        return s[::-1]

    @staticmethod
    def extract_odd(s: str) -> str:
        return s[::2]

    @staticmethod
    def merge_strings(s: str, t: str) -> str:
        res: str = ""
        for a, b in zip(list(s), list(t)):
            res += a
            res += b
        return res

    @staticmethod
    def pi_list(s: str) -> List[int]:
        res: List[int] = []
        s_list = s.split(" ")
        for text in s_list:
            clean_text = sub(r"\W", "", text)
            res.append(len(clean_text))
        return res

    @staticmethod
    def element_symbol(s: str, one_length_list: List[int]) -> Dict[str, int]:
        res: Dict[str, int] = {}
        s_list = s.split(" ")
        for idx, text in enumerate(s_list):
            if idx + 1 in one_length_list:
                key = text[:1].strip()
            else:
                key = text[:2].strip()
            res[key] = idx + 1
        return res

    @staticmethod
    def n_gram(s: str, n: int, t: NGramType) -> List[str]:
        s_list: List[str] = []
        delimiter: str = ""

        if t == NGramType.WORD:
            s_list = s.split(" ")
            delimiter = " "
        elif t == NGramType.CHAR:
            s_list = list(s.replace(" ", ""))
            delimiter = ""

        res: List[str] = []
        for idx, text in enumerate(s_list):
            end = idx + n
            if end > len(s_list):
                break
            res.append(delimiter.join(s_list[idx:end]))
        return res

    @staticmethod
    def union(x: List[str], y: List[str]) -> Set[str]:
        return set(x).union(set(y))

    @staticmethod
    def intersection(x: List[str], y: List[str]) -> Set[str]:
        return set(x).intersection(set(y))

    @staticmethod
    def set_difference(x: List[str], y: List[str]) -> Set[str]:
        return set(x).difference(set(y))

    @staticmethod
    def template(x: int, y: str, z: float) -> str:
        return f"{x}時の{y}は{z}"

    @staticmethod
    def cipher(x: str) -> str:
        s_list: List[str] = list(x)
        res: str = ""
        for s in s_list:
            if s.islower():
                res += chr(219 - ord(s))
            else:
                res += s
        return res

    @staticmethod
    def typoglycemia(x: str) -> str:
        res: List[str] = []
        s_list: List[str] = x.split(" ")
        for s in s_list:
            if len(s) <= 4:
                res.append(s)
            else:
                head: str = s[0]
                tail: str = s[-1]
                internal: str = s[1:-1]
                word: str = ''.join(sample(internal, len(internal)))
                res.append(f"{head}{word}{tail}")
        return " ".join(res)
