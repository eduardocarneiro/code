# python - virutal environment



# what is a virtual environment
"""
* a virtual environment in python is an isolated environment on your computer, where you can run and test your python projects 

* it allows you to manage project-specific dependencies without interfering with other projects or the original python installation 

* think of a virtual environment as a separate container for each python project. each container 
    - has its own python interpreter
    - has its own set of installed packages 
    - is isolated from other virtual environments 
    - can have different versions of the same packages

* using virtual environments is important because:
    - it prevents package verion conflicts between projects 
    - makes projects more portable and reproducible
    - keeps your system python installation clean
    - allows testing with different python versions 
"""



# creating a virtual environment 
"""
* python has the built-in "venv" module for creating virtual environments

* to create a virtual environment on your computer, open the command prompt, and navigate to the folder where you want to create your project, then type this command 

example:
python -m venv myfirstproject
"""

"""
* this will set up a virtual environment, and create a folder named "myfirstproject" with subfolders and files, like this:

result:
- the file/folder structure will look like this:

 -----------------
| myfirstproject  |
|   Include       |
|   Lib           |
|   Scripts       |
|   .gitignore    |
|   pvenv.cfg     |
 -----------------
"""



# active virtual environment
"""
* to use the virtual envvironment, you have to active it with this command 

example: 
- activate the virtual environment 

$ source myfirstproject/bin/activate 
"""

"""
* after activation, your prompt will change to show that you are now working in the active environment

result:
- the command line will look like this when the virtual environment is active 

 ------------------------
| (myfirstproject)... $  |
 ------------------------
"""



# install packages 
"""
* once your virtual environment is activated, you can install packages in it, using "pip"

* we will install a package called 'cowsay'

example:
- install 'cowsay' in the virtual environment

 -------------------------------------------
| (myfirstproject) ... $ pip install cowsay |
 -------------------------------------------

"""



# using package
"""
* now that 'cowsay' module is installed in your virtual environment, lets use it to display a talking cow

* create a file called 'test.py' on your computer. you can place it wherever you want, but I will place it in the same location as the "myfirstproject" folder -not in the folder, but in the same location 

* open the file and insert the three lines in its

example:
- insert two lines in 'test.py'
"""
import cowsay 

cowsay.cow("Good Mooooorning!!!")


"""
result:
  ___________________
| Good Mooooorning!!! |
  ===================
                   \
                    \
                      ^__^
                      (oo)\_______
                      (__)\       )\/\
                          ||----w |
                          ||     ||
"""



# deactivate virtual environment
"""
* to deactivate the virtual environment use this command 

example:
- deactivate the virtual environment 
 
 -----------------------------------
| (myfirstproject) ... $ deactivate |
 -----------------------------------
"""


"""
* as a result, you are now back in the normal command line interface

result:
- normal command line interface 
 
 ----
| $  |
 ----

"""


"""
* if you try to execute the 'test.py' file outside of the virtual environment, you will get an error because 'cowsay' is missing. it was only installed in the virtual environment 

example:
- execute 'test.py' outside of the virtual environment 

 ------------------
| $ python test.py |
 ------------------


result:
- error because 'cowsay' is missing 


NOTE: the virtual environment 'myfirstproject' still exists, it is just not activated. if you activate the virtual environment again, you can execute the 'test.py' file, and the diagram will be displayed
"""



# delete virtual environment 
"""
* another nice thing about working with a virtual environment is that when you, for some reason want to delete it, there are no other projects depend on it, and only the modules and files in the specified virtual environment are deleted

* to delete a virtual environment, you can simply delete its folder with all its content. either directly in the file system, or use the command line interface like this 

example:
- delete 'myfirstproject' from the command line interface 

 -----------------------
| rm -rf myfirstproject |
 -----------------------
"""

















































































































































