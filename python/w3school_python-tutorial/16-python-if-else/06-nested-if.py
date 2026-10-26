# python - nested if


# nested if statements 
"""
* you can have "if" statements inside "if" statements. this is called nested "if" statements 

NOTE: in this example, the inner "if" statement only runs if the outer condition (x > 10) is true

example
"""
x = 12

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20")
    else:
        print("but not above 20")



# how nested if works
"""
* each level of nesting creates a deeper level of decision-making. the code evaluates from the outermost condition inward

example 
- checking multiple conditions with nesting 
"""
age = 25
has_license = True 

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")



# multiple levels of nesting
"""
* you can nest as many levels deep as needed, but keep in mind that too many levels can make code harder to read 

example 
- three levels of nesting 
"""
score = 85
attendance = 90
submitted = True 

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but missing assignment")
    else:
        print("pass but low attendance")
else:
    print("fail")



# nested if vs logical operators
"""
* sometimes nested if statements can be simplified using logical operators like "and". the choice depends on your logic 

example 
- this nested if
"""
temperature = 25
is_sunny = True 

if temperature > 20:
    if is_sunny:
        print("perfect beach weather!")


"""
example 
- could also be written with "and"
"""
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("perfect beach weather...")

"""
* both approaches produce the same result. use nested if statements when the inner logic is complex or depends on the outer condition
* Use "and" when both conditions are simple and equally important
"""



# more examples
"""
example 
- login validation with nested checks
"""
username = "eoc"
password = "secret1234"
#password = ""
#is_active = True 
is_active = False 

if username:
    if password:
        if is_active:
            print("login successful")
        else:
            print("account is not active")
    else:
        print("password required")
else:
    print("username required")


"""
example
- grade calculation with nested logic 
"""
score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade or below")

