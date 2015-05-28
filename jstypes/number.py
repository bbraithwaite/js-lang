from .types import Boolean, NaN, String, BaseType
import re


#
# Number Type (8.5)
#
class Number(BaseType):
    def __init__(self, value):
        if isinstance(value, String):
            self.__value = self.computeMV(value.value())
        elif isinstance(value, str):
            self.__value = self.computeMV(value)
        else:
            self.__value = value

    def _computeHex(self, value):
        mv = 0  # mathematical value
        for hex_digit in value[2:]:
            mv = mv * 16
            if hex_digit.isdigit():
                mv += int(hex_digit)
            elif hex_digit.upper() == 'A':
                mv += 10
            elif hex_digit.upper() == 'B':
                mv += 11
            elif hex_digit.upper() == 'C':
                mv += 12
            elif hex_digit.upper() == 'D':
                mv += 13
            elif hex_digit.upper() == 'E':
                mv += 14
            elif hex_digit.upper() == 'F':
                mv += 15

        return mv

    def computeMV(self, string):
        stripped = string.strip()
        if stripped == '':
            return 0

        if re.match('0[x|X][0-9a-fA-F]+', stripped):
            mv = self._computeHex(stripped)
        else:
            try:
                mv = float(stripped)
            except Exception:
                mv = NaN()

        return mv

    def toBoolean(self):
        if isinstance(self.value(), NaN):
            return Boolean('false')

        if self.value() == 0:
            return Boolean('false')

        return Boolean('true')

    def toNumber(self):
        return self

    def value(self):
        return self.__value

    def toString(self):
        if self.__value == float('inf'):
            return String('Infinity')

        if self.__value == float('-inf'):
            return String('-Infinity')

        return String(str(self.__value))
