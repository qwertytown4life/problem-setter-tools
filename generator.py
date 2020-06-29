from os.path import join
import sys


def gen(args):
    return 'insert test data here'


def solve(fileInput):
    return 'answer'


def write(num, folder):
    path = f"/Users/colin.lum/Desktop/{folder}"
    name = f"in{num}" + '.txt'

    try:
        file = open(join(path, name), 'w')
        # file.write(gen())
        file.write('\n')
        file.close()
    except:
        print('Something went wrong! Cannot tell what?')
        sys.exit(0)


def ans(num, folder):
    path = "/Users/colin.lum/Desktop/testfolder"
    name = f"out{num}" + '.txt'
    try:

        inp = open(f"/Users/colin.lum/Desktop/{folder}/in{num}.txt", 'r')
        # a = solve()
        inp.close()

        out = open(join(path, name), 'w')
        # out.write(a)
        out.write('\n')
        out.close()

    except:
        print('Something went wrong! Cannot tell what?')
        sys.exit(0)


folderName = input('What do you want the name of your folder to be? ')
Number = int(input('How many test cases do you want? '))


for i in range(1, Number):
    write(i, folderName)
    ans(i, folderName)
