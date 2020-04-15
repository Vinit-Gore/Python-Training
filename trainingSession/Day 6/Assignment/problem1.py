'''
Program to return the permutations of your name. Your first and last letters should not be neighbours.
'''

# Function to find permutations of a given string
from itertools import permutations
import re


def allPermutations(str):

    # Get all permutations of string 'ABC'
    permList = permutations(str)
    return permList
    # Apply Regex


def applyRegex(permList, str):
    string1 = ''
    reg = re.compile('.*'+str[0]+str[len(str)-1] +
                     '.*|.*'+str[len(str)-1]+str[0]+'.*')
    remove = set([])
    permlist = set([])
    for perm in permList:
        string1 = ''.join(perm)
        permlist.add(string1)
        if reg.search(string1):
            remove.add(string1)
    remove = set(remove)
    permList = permlist-remove
    return permList, permlist


def printer(permlist, permList):
    for perm in permlist:
        if perm in permList:
            print(perm, ':Accepted')
        else:
            print(perm, ':Rejected')


# Driver program
if __name__ == "__main__":
    str = input('Please input your name:')
    permlist = allPermutations(str)
    permList, permlist = applyRegex(permlist, str)
    printer(permlist, permList)
