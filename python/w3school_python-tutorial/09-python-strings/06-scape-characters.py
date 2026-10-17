# escape character
"""
* to insert characters that are ilegal in a string, use an escape character
* an escape character is a backslash "\" followed by the character you want to insert
* an example of an ilegal character is a double quote inside a string that is surrounded by double quotes

sample
- you will get an error if you use double quotes inside a string that is surrounded by double quotes
txt = "test test test "will bring a error" test test"

* to fix this problem, use the escape character \"
"""
txt = "test test test \"It is OK\" test test"
print(txt)

# escape characters
"""
* Other escape characters used in python
 ________________________________ 
| Code          Result           |
| \'            Single quote     |
| \\            Backslash        |
| \n            New Line         |
| \r            Carriage Return  |
| \t            Tab              |
| \b            Baclspace        |
| \f            Form Feed        |
| \ooo          Octal value      |
| \xhh          Hex value        |
 ________________________________
"""






