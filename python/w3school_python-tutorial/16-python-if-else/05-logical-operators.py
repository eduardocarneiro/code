# python - logical operators


# python logical operators
"""
* logical operators are used to combine conditional statements. python has three logical operators 
    - "and" - returns True if both statements are true
    - "or"  - returns True if one of the statements is true 
    - "not" - reverses the result, returns False if the result is true 
"""



# the AND operator 
"""
- the "and" keyword is a logical operator, and is used to combine conditional statements. Both conditions must be true for the entire expression to be true

example
- test if "a" is greater than "b", AND if "c" is greater than "a"
"""
a = 100
b = 99
c = 105

if a > b and c > a:
    print("both conditions are True")



# the OR operator 
"""
* the "or" keyword is a logical operator, and is used to combine conditional statements. at least one condition must be true for the entire expression to be true

example
- test if "a" is greater than "b", OR if "a" is greater than "c"
"""
a = 200
b = 215
c = 85

if a > b or a > c:
    print("at least one of the conditions is True")



# the NOT operator 
"""
* the "not" keyword is a logical operator, and is used to reverse the result of the conditional statement 

example 
- test if "a" is NOT greater than "b"
"""
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")



# combining multiple operators 
"""
* you can combine multiple logical operators in a single expression. 

* python evaluates:
    - NOT first, then
    - AND, then
    - OR 

example 
- combining "AND", "OR", and "NOT"
"""
age = 215
is_student = False
has_discount_code = True 

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("discount applies")



# truth table
"""
* understanding how logical operators work with different values

AND operator truth table
 ------------------------------------------------
| condition 1       condition 2         result   |
| True              True                True     |
| True              False               False    |
| False             True                False    |
| False             False               False    |
 ------------------------------------------------

OR operator truth table 
 -------------------------------------------------
| condition 1       condition 2         result    |
| True              True                True      |
| True              False               True      |
| False             True                True      |
| False             False               False     |
 -------------------------------------------------
"""



# using parentheses for clarity 
"""
* when combining multiple logical operators, use parentheses to make your intentions clear and control the order of evalution

example 
- using parentheses for complex conditions 
"""
temperature = 25 
is_raining = False
is_weekend = True 

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities")



# more examples 
"""
example
- user authentication check
"""
username = "eoc"
password = "secret123"
is_verified = True 

if username and password and is_verified:
    print("login successful")
else:
    print("Login failed")


"""
example 
- range checking with logical operators 
"""
score = 85 

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")















































