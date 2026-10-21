# operator precedence:w
"""
* operator precedence describes the order in which operations are performed

example
- parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
"""
print((6 + 3) - (6 + 3))

"""
example 
- multiplication "*" has higher precedence than addition "+", and therefore multiplications are evaluated before additions
"""
print(100 + 5 * 3)




# precedence order
"""
* the precedence order is described in the table below, starting with the highest precedence at the top 


 --------------------------------------------------------------------------------------------------
| operator                                  description                                            |
| ()                                        parantheses                                            |
| **                                        exponentiation                                         |
| +x -x ~x                                  unary plus, unary minus, and bitwise NOT               |
| * / // %                                  multiplication, division, floor division and modulus   |
| + -                                       addition and subtraction                               |
| << >>                                     bitwise left and right shifts                          |
| &                                         bitwise AND                                            |
| ^                                         bitwise XOR                                            |
| |                                         bitwise OR                                             |
| == != > >= < <= is is not in not in       comparisons, identity, and membership operators        |
| not                                       logical NOT                                            |
| and                                       AND                                                    |
| or                                        OR                                                     |
 --------------------------------------------------------------------------------------------------
"""



# left-to-right evaluation 
"""
if two operators have the same precedence, the expression is evaluated from left to right 

example 
- addition "+" and subtraction "-" has the same precedence, and therefor we evaluate the expression from left to right 
"""
print(5 + 4 - 7 + 3
