from itertools import islice
path2 ='C:\\Users\\shant\\Downloads\\Assignment2\\Assignment2\\Logs\\required_pattern_00'



with open(path2, 'r',encoding="utf-8") as f:
    for line in f:
        if line == 'assignment_completed:\n':
            print(''.join(islice(f, 1)))         #for processing next line  




    





