
import random
import math
import os
import time

os.system("")

wordlist: list = open('english.txt').read().splitlines()

def toBase(val, charset):   
    base = len(charset)
    units = []
    chars = [] 
    while val >= 0:
        units.append(val % base)
        val //= base
        if val == 0: break    
    while len(units):
        chars.append(charset[int(units.pop())])    
    return ''.join(chars)


def fromBase(str, charset): 
    base = len(charset)
    pos = 0
    num = 0
    char = None
    while len(str):
        char = str[len(str) - 1]
        str = str[:len(str) - 1]
        num += (base ** pos) * charset.index(char)
        pos += 1    
    return int(num)
    

def compactPairwise(position, seed):
    workingNum = position * 2049 + seed
    return int(toBase(workingNum, '0123456789'))


def unPair(val): 
    val = fromBase(str(val), '0123456789')
    pos = val // 2049
    seed = val - 2049 * pos
    return pos, seed


def generatePairedSeed(seedList):
    
    printHeader()

    listAsInt = [wordlist.index(key) for key in seedList]
    pairedList = [compactPairwise(seedList.index(key), wordlist.index(key)) for key in seedList]
    base26 = [toBase(item, "ABCDEFGHIJKLMNOPQRSTUVWXYZ").upper() for item in pairedList]

    print(bcolors.HEADER + "Seed Words" + bcolors.OKGREEN)
    print(f'{", ".join(map(str, seedList))}')

    print(bcolors.HEADER + "\nCompacted Phrases with Encoded Position" + bcolors.OKGREEN, end='')
    for val in base26:
        if base26.index(val) % 5 == 0: 
            print('\n')
        print(f'{val:6}', end='')
    
    print(bcolors.ENDC + '\n')

    return base26


def revertSingle(base26):
    return unPair(fromBase(str(base26), "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))


def revertPairedSeed(base26): 
    reverted = []
    for i in base26:
        n = fromBase(str(i), "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        reverted.append(unPair(n))
    return reverted


def tester(base26list):
    printHeader()
    print(bcolors.HEADER + "\nEnter any encoded word to check its original seed word. Type 'q' to exit." + bcolors.ENDC)
    
    print(bcolors.OKGREEN, end='')
    for val in base26list:
        if base26list.index(val) % 5 == 0: 
            print('\n')
        print(f'{val:6}', end='')
    
    print(bcolors.ENDC + '\n')
    
    inp = input(bcolors.OKBLUE + "Type word: " + bcolors.ENDC)
    
    if inp == 'q':
        m2()
    
    outp = revertSingle(inp.upper())
    
    print(bcolors.OKGREEN + f'Word {outp[0] + 1}:  {wordlist[outp[1]]}')
    
    inp = input(bcolors.OKBLUE + '\nPress Enter to test another' + bcolors.ENDC)  
    if inp == 'q':
        m2()
        
    tester(base26list)


def main():
    inputseed = []
       
    printHeader()
    print(bcolors.HEADER + "Convert Seed Phrase into position-encoded list" + bcolors.ENDC + '\n')
    
        
    leninp = input(bcolors.OKBLUE + 'How many seed words do you have? (6, 12, 24): ' + bcolors.ENDC)

    if leninp not in ['6', '12', '24']: main()
    
    while len(inputseed) < int(leninp):
        printHeader()        
        print(bcolors.HEADER + "Convert Seed Phrase into position-encoded list" + bcolors.ENDC + '\n')      
        print(bcolors.HEADER + "ENTER SEED WORDS" + bcolors.ENDC + '\n')
        
        inp = input(bcolors.OKBLUE + f'Enter word {len(inputseed) + 1}/{leninp}: ' + bcolors.ENDC).lower()

        if inp in wordlist:
            inputseed.append(inp)  
            
        else:
            print(bcolors.WARNING + 'Word not part of BIP39 wordlist. Perhaps you mistyped it?' + bcolors.ENDC)
            pause = 3
            for x in range(3):
                print(bcolors.WARNING + f'    Continue in {pause}...' + bcolors.ENDC, end='\r')
                time.sleep(1)
                pause -= 1
    
    generatedseed = generatePairedSeed(inputseed)
    
    print(bcolors.HEADER + 'Check that your SEED PHRASE is in the right order above, then copy down the COMPACTED PHRASE list.\nRemember, the order of the compacted list ' + bcolors.BOLD + "does not matter" + bcolors.ENDC)
    input(bcolors.OKBLUE + '\nPress Enter to continue ' + bcolors.ENDC)
    tester(generatedseed)


def reverter():
    printHeader()
    print(bcolors.HEADER + '\nConvert Encoded List Into Original Seed Phrase')
    print(bcolors.HEADER + 'Enter all encoded words below, separated by a space. Remember, the order does not matter.\n')
    
    inp = input(bcolors.OKBLUE + 'Enter all encoded words: ' + bcolors.ENDC)
    
    inlist = inp.upper().split(' ')
    
    reverted = revertPairedSeed(inlist)
    
    reverted.sort()
    
    print('')
    for outp in reverted:
        print(bcolors.OKGREEN + f'Word {outp[0] + 1:>5}:  {wordlist[outp[1]]}' + bcolors.ENDC)
    
    input(bcolors.OKBLUE + '\n\nPress Enter key to continue...' + bcolors.ENDC)
    m2()


def m2():
    printHeader()
    print(bcolors.OKCYAN + 'Use this program to encode each word in a seed phrase into a four-letter code that also encodes its position.')
    print('You can then store the resultant codes in ANY order, and extract the original word AND position later on.\n\n')
    print('For best safety, only run this program on an OFFLINE computer.\n\n')
    
    print(bcolors.HEADER + '1: Generate new encoded list from seed phrase')
    print(bcolors.HEADER + '2: Extract an original seed phrase from an encoded list' + bcolors.ENDC)
    
    inp = input(bcolors.OKBLUE + '\nSelect Option (1 or 2) or press any other key to exit: ' + bcolors.ENDC)
    
    selection = None
    
    if inp == '1':
        main()
    elif inp == '2':
        reverter()
    else:
        clearConsole()
        exit()


# Starts Here ===========================
if __name__ == "__main__":
    m2()


# Helper Nonsense========================
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def printHeader():
    clearConsole()
    print(bcolors.HEADER + bcolors.BOLD + 'CRYPTO BIP39 SEED PHRASE ENCODER/PACKAGER')
    print('==========================================' + bcolors.ENDC + '\n')
