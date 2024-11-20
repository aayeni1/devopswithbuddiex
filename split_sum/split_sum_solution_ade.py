import os

os.system('reset')

def small(lst):
    for z in range(1,len(lst)+1):
        a, b = lst[:z], lst[z:]
        if sum(a) == sum(b):
            return f"a: {{sum : {sum(a)},list : {a}}}\nb: {{sum : {sum(b)},list : {b}}}"
    return 'Not possible to split equally'

if __name__ == '__main__':
    lst = [1,4,3,4,1,4,7]
    print(small(lst))