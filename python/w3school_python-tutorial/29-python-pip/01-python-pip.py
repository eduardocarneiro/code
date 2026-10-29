# python - pip 



# what is pip 
"""
* PIP is a package manager for python packages, or modules if you like 

NOTE: if you have python version 3.4 or later, PIP is included by default 
"""



# what is a package 
"""
* a package contains all the files you need for a module 

* modules are python code libraries you can include in your project 
"""



# check if pip is installed 
"""
* navigate your command line to the location of python's script directory, and type the following 

example:
- check pip version 

$ pip --version
"""



# install PIP 
"""
* if you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/ 
"""


# download a package 
"""
* downloading a package is very easy 

* open the command line interface and tell PIP to download the package you want 

* navegate your command line to the location of python's script directory, and type the following 

example:
- download a package named "camelcase"

$ pip install camelcase

NOTE: Now you have downloaded and installed your first package! 
"""



# using a package 
"""
* once the package is installed, it is ready to use 

* import the "camelcase" package into your project 

example:
- import and use "camelcase"
"""
import camelcase

c = camelcase.CamelCase() 

txt = "hello world"
print(c.hump(txt))



# find packages 
"""
* find more packages at https://pypi.org 
"""



# remove a package
"""
* use the "uninstall" command to remove a package 

example:
- uninstall the package named "camelcase"

$ pip uninstall camelcase 


NOTE: the PIP package manager will ask you to confirm that you want to remove the camelcase package. Press "y" and the package will be removed
"""



# list packages 
"""
* use the "list" command to list all the packages installed on your system 

example:
- list installed package 

$ pip list 
"""



















