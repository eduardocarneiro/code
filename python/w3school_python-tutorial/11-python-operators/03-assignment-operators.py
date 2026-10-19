# assignment operators
"""
* assignment operators are used to assign values to variables


 _______________________________________________ 
| operator      example         same as         |
| =             x = 5           x = 5           |
| +=            x += 3          x = x + 3       |
| -=            x -= 3          x = x - 3       |
| *=            x *= 3          x = x * 3       |
| /=            x /= 3          x = x / 3       |
| %=            x %= 3          x = x % 3       |
| //=           x //= 3         x = x // 3      |
| **=           x **=           x = x ** 3      |
| &=            x &= 3          x = x & 3       |
| |=            x |= 3          x = x | 3       |
| ^=            x ^= 3          x = x ^ 3       |
| >>=           x >>= 3         x = x >> 3      |
| <<=           x <<= 3         x = x << 3      |
| :=            print(x := 3)   x = 3 print(x)  |
 -----------------------------------------------
"""

 

# the walrus operator
"""
* python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a large expression

example
- the count variable is assigned in the if statement, and given the value 5
"""

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

