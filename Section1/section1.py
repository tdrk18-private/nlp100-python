import re
from typing import List, Dict


class Section1:
    @staticmethod
    def reverse(s: str) -> str:
        return s[::-1]

    @staticmethod
    def extract_odd(s: str) -> str:
        return s[::2]

    @staticmethod
    def merge_strings(s: str, t: str) -> str:
        res = ""
        for a, b in zip(list(s), list(t)):
            res += a
            res += b
        return res

    @staticmethod
    def pi_list(s: str) -> List[int]:
        res = []
        s_list = s.split(" ")
        for text in s_list:
            clean_text = re.sub(r"\W", "", text)
            res.append(len(clean_text))
        return res

    @staticmethod
    def element_symbol(s: str, one_length_list: List[int]) -> Dict[str, int]:
        res = {}
        s_list = s.split(" ")
        for idx, text in enumerate(s_list):
            if idx + 1 in one_length_list:
                key = text[:1].strip()
            else:
                key = text[:2].strip()
            res[key] = idx + 1
        return res
