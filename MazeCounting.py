"""
    Maze Automated Calculator
    This is a prototype: Maze Automated Calculator for Y-maze and Cross-maze. It calculates the SAP with percentage and, information about number of Arm Entry.
    Author: JiHoonKim, Last modified 01.07.2020.
"""

def Spell_Y(S):
    """
    S: string, the input of the entry Arm: A, B, and C.
    This function extracts only ABC in the string input, and return the modified input.
    
    Example:
    Input: "ABC BCAA B"
    Ouput: "ABCBCAAB"
    """
    # Change it to uppercase.
    S = S.upper()
    string = ''
    # Extract only the entry Arm: A, B, C.
    for C in S:
        if C in 'ABC':
            string = string + C
    return string

def SAP_Y(string):
    """
    string: the string only contained: A, B, and C.
    Compute the SAP, SAP(&), number of Arm Entry, and index of the counitng, and
    
    Example:
    Input: "ABCBA"
    Output: number, percent
    """
    print("This is the Y Maze result:")
    number = 0
    print('Arm entry count:', len(string))
    for i in range(len(string)-2):
        A = string[i:i+3]       # Search section setting
        num = i+1               # Position index
        # Counting only SAP case
        if (A == 'ABC'):
            number += 1
            print('position:', num,'Count= ABC')
        elif (A == 'ACB'):
            number += 1
            print('position:', num,'Count= ACB')
        elif (A == 'BAC'):
            number += 1
            print('position:', num,'Count= BAC')
        elif (A == 'BCA'):
            number += 1
            print('position:', num,'Count= BCA')
        elif (A == 'CAB'):
            number += 1
            print('position:', num,'Count= CAB')
        elif (A == 'CBA'):
            number += 1
            print('position:', num,'Count= CBA')
        percent = number/(len(string)-2)*100
    return number, percent

def Spell_C(S):
    """
    S: string, the input of the entry Arm: A, B, C, and D.
    This function extracts only ABCD in the string input, and return the modified input. 
    
    Example:
    Input: "ABCD BCAA BD"
    Ouput: "ABCDBCAABD"
    """
    S = S.upper()
    string = ''
    for C in S:
        if C in 'ABCD':
            string = string + C
    return string

def SAP_C(string):
    """
    string: the string only contained: A, B, C, and D.
    Compute the SAP, SAP(&), number of Arm Entry, and index of the counitng, and
    
    Example:
    Input: "ABCDBAD"
    Output: number, percent
    """
    print("This is the Cross Maze result:")
    number = 0
    print('Arm entry count:',len(string))
    # Counting only SAP case
    for i in range(len(string)-3):
        A = string[i:i+4]    # Search section setting
        num = i+1            # Position index
        if (A == 'ABCD'):
            print(num,' position: Count= ABCD')
            number += 1
        elif (A == 'ABDC'):
            number += 1
            print(num,' position: Count= ABDC')
        elif (A == 'ACBD'):
            number += 1
            print(num,' position: Count= ACBD')
        elif (A == 'ACDB'):
            number += 1
            print(num,' position: Count= ACDB')
        elif (A == 'ADBC'):
            number += 1
            print(num,' position: Count= ADBC')
        elif (A == 'ADCB'):
            number += 1
            print(num,' position: Count= ADCB')
        elif (A == 'BACD'):
            number += 1
            print(num,' position: Count= BACD')
        elif (A == 'BADC'):
            number += 1
            print(num,' position: Count= BADC')
        elif (A == 'BCAD'):
            number += 1
            print(num,' position: Count= BACD')
        elif (A == 'BCDA'):
            number += 1
            print(num,' position: Count= BCDA')
        elif (A == 'BDAC'):
            number += 1
            print(num,' position: Count= BDAC')
        elif (A == 'BDCA'):
            number += 1
            print(num,' position: Count= BDCA')
        elif (A == 'CABD'):
            number += 1
            print(num,' position: Count= CABD')
        elif (A == 'CADB'):
            number += 1
            print(num,' position: Count= CADB')
        elif (A == 'CBAD'):
            number += 1
            print(num,' position: Count= CBAD')
        elif (A == 'CBDA'):
            number += 1
            print(num,' position: Count= CBDA')
        elif (A == 'CDAB'):
            number += 1
            print(num,' position: Count= CDAB')
        elif (A == 'CDBA'):
            number += 1
            print(num,' position: Count= CDBA')
        elif (A == 'DABC'):
            number += 1
            print(num,' position: Count= DABC')
        elif (A == 'DACB'):
            number += 1
            print(num,' position: Count= DACB')
        elif (A == 'DBAC'):
            number += 1
            print(num,' position: Count= DBAC')
        elif (A == 'DBCA'):
            number += 1
            print(num,' position: Count= DBCA')
        elif (A == 'DCAB'):
            number += 1
            print(num,' position: Count= DCAB')
        elif (A == 'DCBA'):
            number += 1
            print(num,' position: Count= DCBA')
        percent = number/(len(string)-3)*100
    return number,percent

def interface(type, input):
    """
    type: Y or C. Y is Y_Maze, and C is Cross_Maze
    input: string one to compute.
    It applys the inputs of both Y maze and Cross maze separately.
    
    Example:
    Input: 'C', 'CDADADCACABDBDBDBDCBDCACA'
    """
    print("Welcome the maze counting!")   
    if type == 'Y':
        if 'D' in input:
            print("Please check the type: it can be not Y but C")
        else:
            print('(Count, Alternative ratio): ', SAP_Y(Spell_Y(input)))
    elif type == 'C':
        print('(Count, Alternative ratio): ', SAP_C(Spell_C(input)))
    else:
        print("It's a wrong type")
    a = "Completed"
    return a

# Example:
print(interface('Y', 'BCBCABCBBAC'))
print(interface('C', 'CDADADCACABDCBDCABDCBDBCDDBDCBDCACCenter'))