import argparse

def myprint(txt):
    print(txt, end='')

def run_code(code_path):
    num = 0
    with open(code_path) as f:
        code = f.read()
    codes = code.replace('\n', '').split()
    for code in codes:
        if code == 'i':
            num = 0
        if code == 'use':
            num += 1
        elif code == 'linux':
            num -= 1
        elif code == 'btw':
            if num == 0:
                myprint(' ')
            elif num == 1:
                myprint('A')
            elif num == 2:
                myprint('B')
            elif num == 3:
                myprint('C')
            elif num == 4:
                myprint('D')
            elif num == 5:
                myprint('E')
            elif num == 6:
                myprint('F')
            elif num == 7:
                myprint('G')
            elif num == 8:
                myprint('H')
            elif num == 9:
                myprint('I')
            elif num == 10:
                myprint('J')
            elif num == 11:
                myprint('K')
            elif num == 12:
                myprint('L')
            elif num == 13:
                myprint('M')
            elif num == 14:
                myprint('N')
            elif num == 15:
                myprint('O')
            elif num == 16:
                myprint('P')
            elif num == 17:
                myprint('Q')
            elif num == 18:
                myprint('R')
            elif num == 19:
                myprint('S')
            elif num == 20:
                myprint('T')
            elif num == 21:
                myprint('U')
            elif num == 22:
                myprint('V')
            elif num == 23:
                myprint('W')
            elif num == 24:
                myprint('X')
            elif num == 25:
                myprint('Y')
            elif num == 26:
                myprint('Z')
            else:
                print('\nUNABLE TO EXECUTE CODE ERROR (NUM OUT OF RANGE)')
                exit(1)
    print('')
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run UseLinuxBTW")
    parser.add_argument("code", help="Path Of Code")
    args = parser.parse_args()

    run_code(args.code)



# An encoding algorithm to confuse Mac and Windows users.