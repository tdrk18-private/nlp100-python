import re
from typing import List


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
