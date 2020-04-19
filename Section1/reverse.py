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
