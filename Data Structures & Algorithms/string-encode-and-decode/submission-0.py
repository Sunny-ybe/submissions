class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string = string+s+"✌🏻"
        return string


        # sbkb😏✌️😳👍🏻😳

    def decode(self, s: str) -> List[str]:
        lst = s.split("✌🏻")[:-1]
        return lst
    
