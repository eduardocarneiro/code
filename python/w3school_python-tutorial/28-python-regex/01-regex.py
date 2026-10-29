# python - regex
"""
* a regex, or regular expression, is a sequence of characters that forms a search pattern 

* regex can be used to check if a string contains the specified search pattern 
"""



# regex module 
"""
* python has a built-in package caleed "re", which can be used to work with regular expressions 

* import "re" module 

-----------
| import re |
 -----------
"""



# regex in python 
"""
* when you have imported the "re" module, you can start using regular expressions 

example:
- search the string to see if it starts with "the" and ends with "spain"
"""
import re
from typing import overload 
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)



# regex functions
"""
* the "re" module offers a set of functions that allows us to search a string for a match


 ---------------------------------------------------------------------------------------
| function          description                                                         |
| findall           returns a list containing all matches                               |
| search            returns a match object if there is a match anywhere in the string   |
| split             returns a list where the string has been split at each match        |
| sub               replaces one or many matches with a string                          |
 ---------------------------------------------------------------------------------------

"""



# metacharacters
"""
* metacharacters are characters with a special meaning 


 -----------------------------------------------------------------------------------------------------------
| character     description                                                                 example         |
| []            a set of characters                                                         "[a-m]"         |
| \             signals a special sequence(can also be used to escape special characters)   "\d"            |
| .             any character(except newline character)                                     "he..o"         |
| ^             starts with                                                                 "^hello"        |
| $             ends with                                                                   "plane$"        |
| *             zero or more occurrences                                                    "he.*o"         |
| +             one or more occurrences                                                     "he.?o"         |
| {}            exactly the specified number of occurrences                                 "he.{2}o"       |
| |             either or                                                                   "falls|stays"   |
| ()            capture and group                                                                           |
 -----------------------------------------------------------------------------------------------------------

"""



# flags 
"""
* you can add flags to the pattern when using regular expressions 


 ---------------------------------------------------------------------------------------------------------------------------------------------------
| flag              shorthand   description                                                                                                         |
| re.ASCII          re.A        returns only ASCII matches                                                                                          |
| re.DEBUG                      returns debug information                                                                                           |
| re.DOTALL         re.S        makes the .character match all characters (including newline character)                                             |
| re.IGNORECASE     re.l        case-insensitive matching                                                                                           |
| re.MULTILINE      re.M        returns matches at the start/end of each line                                                                       |
| re.NOFLAG                     specifies that no flag is set for this pattern                                                                      |
| re.UNICODE        re.U        returns unicode matches. this is default from python 3. for python 2: use this flag to return only unicode matches  |
|re.VERBOSE         re.X        allows whitespaces and comments inside patterns. makes the pattern more readable                                    |
 ---------------------------------------------------------------------------------------------------------------------------------------------------
"""



# special sequences 
"""
* a special sequence is a "\" followed by one of the characters in the list below, and has a special meaning 


 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
| character     description                                                                                                                                                                                                     example             |
| \A            returns a match if the specified characters are at the beginning of the string                                                                                                                                  "\AThe"             |
| \b            returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")                        r"\bain" - r"ain\b" |
| \B            returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string")     r"\Bain" - r"ain\B" |
| \d            returns a match where the string contains digits (numbers from 0-9)                                                                                                                                             "\d"                |
| \D            returns a match where the string DOES NOT contain digits                                                                                                                                                        "\D"                |
| \s            returns a match where the string contains a white space character                                                                                                                                               "\s"                |
| \S            returns a match where the string DOES NOT contain a white space character                                                                                                                                       "\S"                |
| \w            returns a match where the string contains any word characters (characters from a to Z, figits from 0-9, and the underscore _ character)                                                                         "\w"                |
| \W            returns a match where the string DOES NOT contain any word characters                                                                                                                                           "\W"                |
| \Z            returns a match if the specified characters are at the end of the string                                                                                                                                        "Spain\Z"           |
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""



# sets 
"""
* a set is a set of characters inside a pair of square brackets [] with a special meaning 


 -------------------------------------------------------------------------------------------------------------------------------------------------------
| set           description                                                                                                                             |
| [arn]         returns a match where one of the specified characters (a, r, or n) is present                                                           |
| [a-n]         returns a match for any lower case character, alphabetically between "a" and "n"                                                        |
| [^arn]        returns a match for any character EXCEPT "a", "r", and "n"                                                                              |
| [0123]        returns a match where any of the specified digits (0, 1, 2, or 3) are present                                                           |
| [0-9]         returns a match for any digit between 0 and 9                                                                                           |
| [0-5][0-9]    returns a match for any two-digit numbers from 00 and 59                                                                                |
| [a-zA-Z]      returns a match for any character alphabetically between "a" and "z", lower case OR upper case                                          |
| [+]           in sets, "+", "*", ".", "|", "()", "$", "{}" has no special meaning so "[+]" means: return a match for any "+" character in the string  |
 -------------------------------------------------------------------------------------------------------------------------------------------------------

"""



# the findall() function 
"""
the "findall()" function returns a list containing all matches 

example:
- print a list of all matches 
"""
import re 
txt = "The raing in Spain"
x = re.findall("ai", txt)
print(x)


"""
* the list contains the matches in the order they are found 

* if no matches are found, an empty list is returned

example:
- return an empty list if no match was found 
"""
import re 
txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)



# the search() function 
"""
* the search() function searches the string for a match, and returns a "Match object" if there is a match

* if there is more than one match, only the first occurrence of the match will be returned 

example:
- search for the first white-space character in the string 
"""
print("\n")

import re
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())



"""
* if no matches are found, the value "None" is returned 

example:
- make a search that returns no match 
"""
import re 
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



# the split() function 
"""
* the "split()" function returns a list where the string has been split at each match 

example:
- split at each white-space character 
"""
import re 

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



"""
* you can control the number of occurrences by specifying the "maxsplit" parameter 

example:
- split the string only at the first accurrence 
"""
import re 
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)



# the sub() function 
"""
* the "sub()" function replaces the matches with the text ot your choice

example:
- replace every white-space character with the number 9 
"""
import re 

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


"""
* you can control the number of replacements by specifying the "count" parameter 

example:
- replace the first 2 occurrences
"""
import re 

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)



# match object 
"""
* a match object is an object containing information about the search and the result

NOTE: if there is no match, the value "None" will be returned, instead of the Match Object 

example:
- do a search that will return a match object 
"""
import re 

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)



""" the match object has properties and methods used to retrieve information about the search, and the result 

    - ".span()"    returns a tuple containing the start-, and end positions of the match 
    - ".string()"  returns the string passed into the function 
    - ".group()"   returns the part of the string where there was a match 

example:
- print the position (start- and end-position) of the first match occurrence 
- the regular expression looks for any words that starts with an upper case "S"
"""
import re 

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


"""
example:
- print the string passed into the function 
"""
import re 

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)


"""
example:
- print the part of the string where there was a match 
- the regular expression looks for any words that starts with an upper case "S"
"""
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


"""
NOTE: if there is no match, the value "None" will be returned, instead of the match object 
"""
