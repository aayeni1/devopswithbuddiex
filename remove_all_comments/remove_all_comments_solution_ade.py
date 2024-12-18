import os

os.system('reset')
directory = os.path.dirname(os.path.abspath(__file__))
path = f'{directory}/my_code.py'
path2 = f'{directory}/my_new_code_ade.py'

skip = False
with open(path,'r') as file, \
     open(path2,'w') as file2:
    for line in file:
        line_stripped = line.strip()
        if line_stripped.startswith('"""'):
            skip = not skip
            continue #confused why not putting this fails
        if skip:
            continue
        if line_stripped.startswith('#') or line_stripped=='':
            continue
        file2.write(line)