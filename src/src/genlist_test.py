# Hello World program in Python
    

import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    return alist
    


def printIt():
    print(generate_list())
def main():
    print()
    
if '_name_' == '_main_':
    print("Test printIt():")
    generate_list()
