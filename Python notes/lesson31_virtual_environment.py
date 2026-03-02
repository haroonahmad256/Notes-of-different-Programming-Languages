'''
A virtual environment is a separate, isolated space where Python and its libraries live only for one project.
It keeps its specific dependencies (libraries, packages, interpreter) separate 
from other projects of python and the system's main installation, preventing version conflicts 
and ensuring each project runs with its required software, like a self-contained container for your code.
For example: My friend is using 1.4 version of pandas and i am using 2.4 version and i have to run his project
but it will not run on my computer because i have different version. So will i uninstall the pandas and then 
reinstall it, certainly not i will create a virtual environment for that specific project and install required dependencies
for it

Dependencies are libraries, modules, like functions on which a program depends. They contain reusable code so that it 
make programming convinient for the programmers means they are the reusable blocks of code

Virtual environment is different from our global environment, we can install packages sepcifically for this virtual environement

'''
#To create virtual environment:
#    python -m venv nameoftheVirtual_environment
#To activate the environment:
#    foldername\Scripts\activate
#After activating environment we can install packages like this:
# This package will be installed for that particular environment not for global computer
#    pip instal packagename
#To import packages we will first open python interpreter like this: 
#    python (This will give some details about python and its version and you will enter interpreter)
#    >>> import packagename
#    >>>operation_you_want_to_perform
#    >>>exit()

#Sometimes we would like to install different version of package to do this:
#    pip install packagename(pandas)==version(1.4.4)

#To know what packages we have installed in our virtual environment:
#    pip freeze (This will give list of all installed packages)
#    pip freeze > requirements.txt (This will create txt file which will contain list of installed packages)
#Lets say we send this requirements.txt file to our friend and he will simply run this command to install all packages 
#listed in requirements.txt:
#    pip install -r requirements.txt

#We can say it multiple pythons in a single computer