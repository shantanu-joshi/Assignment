import re
#from cgitb import lookup
path = 'C:\\Users\\shant\\Downloads\\Assignment2\\Assignment2\\start_assignment.log'
file1 = open(path,'r',encoding="utf8")       
stringtosearch = 'beginning of assignment'

for num, line in enumerate(file1,1):                           #finding line number so that i can extract text  from that part and can find the first pattern 
    if stringtosearch in line:
        print("found at line number =",num)
        linenumber  = num
        break


line = file1.readlines()[linenumber:]   #Storing the part from beginning of the assignment in a list 
regex = re.compile("required_pattern_\d\d")    #Defining regex 
listToStr = ' '.join([str(elem) for elem in line])       #Converting the list to string for putting it in regular expression


match_object = regex.findall(listToStr)    #putting regex
print(match_object[0])





