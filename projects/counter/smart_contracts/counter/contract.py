from algopy import ARC4Contract, String, UInt64, arc4
from algopy.arc4 import abimethod


class Counter(ARC4Contract):
    @abimethod()
    def add(self, a: UInt64, b: UInt64) -> UInt64: # Unsign integer 64(Số nguyên không âm)
       return a + b

    @abimethod()
    def sub(self,a: UInt64, b: UInt64) -> UInt64:
        assert a > b, "a must be greater than b"
        return a - b

    @abimethod()
    def mul(self, a: UInt64, b: UInt64) -> UInt64:
        assert a > 0 and b > 0, "a and b must be greater than 0"
        return a * b

    @abimethod()
    def div(self, a: UInt64, b: UInt64) -> UInt64:
        assert b > 0, "b must be greater than 0"
        return a // b
