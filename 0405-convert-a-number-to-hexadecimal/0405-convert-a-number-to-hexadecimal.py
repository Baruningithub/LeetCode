class Solution:
    def toHex(self, num: int) -> str:
        num = num & 0xFFFFFFFF #handle negative no.s with two's complement
        return hex(num)[2::]