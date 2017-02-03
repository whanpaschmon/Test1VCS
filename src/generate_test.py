import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    return alist
    
"""
print a generate list
"""

def printIt():
    print( generate_list())
    
def main ():
    printIt()

"""
If this script file is called, it will run main() directly
"""
if __name__ == '__main__':
    print( "Test printIt():" )
    main()
    
#insert the current directory path to Phython Path
import sys
import os
cwd = os.getcwd() #current Working Directory

sys.path.append(cwd)
#print(sys.path)

#test the module: generate_list
from generate_list import printIt
printIt()

