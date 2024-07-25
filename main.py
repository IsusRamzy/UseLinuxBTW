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
            myprint(chr(num))
    print('')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run UseLinuxBTW")
    parser.add_argument("code", help="Path Of Code")
    args = parser.parse_args()

    run_code(args.code)



# An encoding algorithm to confuse Mac and Windows users.