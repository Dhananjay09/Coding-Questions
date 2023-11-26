import math
import os
import random
import re
import sys


#
# Complete the 'binary_converter' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER_ARRAY binary
#  2. CHARACTER base
#

def binary_converter(binary: list[int], base: str = 10) -> str:
    binary_string = ''.join(str(bit) for bit in binary)
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    decimal_number = int(binary_string, 2)

    if base == 10:
        return str(decimal_number)
    else:
        if decimal_number == 0:
            return "0"
        result = ""
        base_map = {
            'b': 2, 'o': 8, 'd': 10, 'h': 16, 'x': 16
        }
        base_number = base_map.get(base.lower())
        while decimal_number > 0:
            remdr = decimal_number % base_number
            result = digits[remdr] + result
            decimal_number //= base_number
        return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binary = list(map(int, input().strip().split()))

    try:
        base = input().strip()
        result = binary_converter(binary, base)
    except:
        result = binary_converter(binary)

    fptr.write(result + '\n')

    fptr.close()
    