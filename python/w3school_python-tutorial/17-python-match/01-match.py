# python - match 
"""
* the "match" statement is used to perform different actions based on different conditions
"""



# the python "match" statement 
"""
* instead of writing many if..else statements, you can use the "match" statement

* the "match" statement selects one of many code blocks to be executed 


syntax:

match expression:
    case x:
        code block 
    case y: 
        code block 
    case z:
        code block


* this is how it works:
    - the "match" expression is evaluated once
    - the value of the expression is compared with de values of each "case"
    - if there is a "match", the associated block of code is executed 

* the example below uses the weekday number to print the weekday name 

example
"""
day = 4

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")



# default value 
"""
* use the underscore character "_" as the last case value if you want a code block to execute when there are not other machines

* the value "_" will always match, so it is important to place it as the last "case" to make it behave as a default "case"

example 
"""
day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the weekend")



# combine values 
"""
* use the pipe character "|" as an or operator in the "case" evaluation to check for more than one value match in one "case"

example 
"""
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("weekday")
    case 6 | 7:
        print("weekend")



# if statement as guards
"""
* you can add "if" statement in the case evaluation as an extra condition-check

example 
"""
month = 5
day = 2
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")





























