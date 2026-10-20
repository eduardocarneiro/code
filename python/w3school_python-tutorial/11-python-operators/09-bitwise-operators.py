# bitwise operators
"""
NOTE: 
1. the binary representation of 6 is 0110
2. the binary representation of 3 is 0011

then the "&" operator compares the bits and returns 0010, which is 2 in decimal
"""
"""
NOTE: 
1. the binary representation of 6 is 0110
2. the binary representation of 3 is 0011

then the "&" operator compares the bits and returns 0010, which is 2 in decimal
"""
"""
NOTE: 
1. the binary representation of 6 is 0110
2. the binary representation of 3 is 0011

then the "&" operator compares the bits and returns 0010, which is 2 in decimal
"""
"""
* bitwise operators are used to compare (binary) numbers


 ------------------------------------------------------------------------------------------------
| operator  name                    description                                         example  |
| &         AND                     sets each bit to 1 if both bits are 1               x & y    |
| |         OR                      sets each bit to 1 if one of two bits is 1          x | y    |
| ^         XOR                     sets each bit to 1 if only one of two bits is 1     x ^ y    |
| ~         NOT                     inverts all the bits                                ~x       |
| <<        Zero fill left shift    shift left by pushing zeros in from the right                |
|                                   and let the leftmost bits fall off                  x << 2   |
| >>        Signed right shift      shift right by pushing copies of the leftmost                |
|                                   bit in from the left, and let the rightmost bits             | 
|                                   fall out                                            x >> 2   |
 ------------------------------------------------------------------------------------------------
"""

# examples
"""
example
- the "&" operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0

NOTE: 
1. the binary representation of 6 is 0110
2. the binary representation of 3 is 0011

then the "&" operator compares the bits and returns 0010, which is 2 in decimal
"""
print(6 & 3) # output number 2


"""
example
- the "|" operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0 

NOTE: 
1. the binary representation of 6 is 0110 
2. the binary representation of 3 is 0011 

then the "|" operator compares the bits and returns 0111, which is 7 in decimal 
"""
print(6 | 3) # output number 7


"""
example
- the "^" operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0110

NOTE: 
1. the binary representation of 6 is 0110
2. the binary representation of 3 is 0011 

then the "^" operator compares the bits and returns 0101, which is 5 in decimal 
"""
print(6 ^ 3) # output number 5



