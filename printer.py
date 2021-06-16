#Auhtor:Sinap-git

#Function that calculates the number of down-up-left-right properties!
#Function ignores the oposite values that comes simultaneous such as dduu or rrll.
#For example if we have a comand like dduurrll, 
#function will not going to increase the counts because oposite values will neutralize each other.
#We append the counts to the counts_list array, which is a n dimensional array that can increase its size. 
def parseCountList(count_list,value_algoritm):
    length = len(value_algoritm)
    down = 0
    up  = 0
    left = 0
    right = 0
    for i in range(length-1):
        if value_algoritm[i] == "R" and value_algoritm[i+1] != "L":
            right = right+1
        elif value_algoritm[i] == "L" and value_algoritm[i+1] != "R":
            left = left+1
        elif value_algoritm[i] == "D" and value_algoritm[i+1] != "U":
            down = down+1
        elif value_algoritm[i] == "U" and value_algoritm[i+1] !="D":
            up = up+1
    #parsing the last Index...
    parseLastIndex(value_algoritm,down,up,left,right,length)
    count_list.append([down,up,right,left])

#Same function with the above but parses the last index.
def parseLastIndex(value_algoritm,down,up,left,right,length):
    if(value_algoritm[length-1] == "D" and value_algoritm[length-2] != "U"):
        down = down+1 
    elif(value_algoritm[length-1] == "U" and value_algoritm[length-2] != "D"):
        up = up+1
    elif(value_algoritm[length-1] == "R" and value_algoritm[length-2] != "L"):
        right = right+1
    elif(value_algoritm[length-1] == "L" and value_algoritm[length-2] != "R"):
        left = left+1

#Checks whether two logos has the same number of down-up-right-left properties by iterating count_list array
#indexsrc1 and indexsr2 are the indexes that our logos inside the count_list
#if the ABSOLUTE VALUE of down right up left operations are the same then return true
# If the number of properties are same then return True 
def isSame(count_list,indexsrc1,indexsrc2):
    sum1 = 0
    sum2 = 0
    for i in count_list[indexsrc1-1]:
        sum1 = sum1 +i
    for i in count_list[indexsrc2-1]:
        sum2 = sum2 +i
    return sum1 == sum2

#Engraves the logo by changing the indexes therefore prints to logo to the array
#Changes the specific indexses according to the value algorith
def engraveArray(array,value_algoritm,starting_row,starting_col):
    right_count = 0
    left_count  = 0
    up_count  = 0
    down_count = 0
    for n in value_algoritm:
        if(n == "D"):
            array[starting_row+down_count+up_count+1][starting_col+right_count+left_count] = "|"
            down_count = down_count+2
        elif n == "R":
            array[starting_row+down_count+up_count][starting_col+right_count+left_count+1] = "—"
            right_count = right_count+2
        elif n == "U":
            array[starting_row+down_count+up_count-1][starting_col+right_count+left_count] = "|"
            up_count = up_count-2
        elif n == "L":
            array[starting_row+down_count+up_count][starting_col+right_count+left_count-1] = "—"
            left_count = left_count-2
        else:
            print("Unknown!")
            break
#Prints the main array
def printArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j],end=" ")
        print("")
#Creates Empty printer array
def createPrinter():
    array = [["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."],
        [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "],
        ["."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."," ","."]]
    return array
#------------------------------------------------------------------
#Main Area!
#Printer created using createPrinter function
array = createPrinter()

logos_dict={} #A dictionary that keeps the logo name as key and value algoirthm(dduurrll) as the value
count_list = [] #N dimensional list that holds the down up left right values in an array
value_algoritm = "" #The string that keeps the algorithm for the printer such ass DDRRUL
while True:

    input_string = input("Enter the input: ") #Input string
    parts = input_string.split(" ") #Splits the input according to the 'space'
    
    if parts[0] == "LOGO": #If the first command is logo
        logos_dict[parts[1]] = parts[2] #logo added to the logo dictionary with the logo name  as key and the value algorithm as value
        print("{0} defined ".format(parts[1]))
    
    elif parts[0] == "ENGRAVE": #If the first command is engrave
        for i in logos_dict:
            if parts[1] == i:#We check if the logo exists in the array
                value_algoritm = logos_dict[i] # We take the value_algoritm from the dict
                
                starting_row = (int(parts[2])-1)*2 #Starting row of the printer
                starting_col = (int(parts[3])-1)*2 #Starting collumn of the printer
                    
                engraveArray(array,value_algoritm,starting_row,starting_col)#Engrave the logo to the array

        printArray(array) #Display the logo
        array = createPrinter() #Clear the array after
    
    elif parts[0] == "SAME": #If the first command is same
        if logos_dict.get(parts[1]) and logos_dict.get(parts[2]): #check if the logos exists

                value_algoritm1 = logos_dict.get(parts[1]) #Get the algoritm for logo-i
                value_algoritm2 = logos_dict.get(parts[2]) #Get the algoritm for logo-j

                parseCountList(count_list,value_algoritm1) #parsing the count list
                parseCountList(count_list,value_algoritm2) #parsing the count list

                indexsrc1 = int(parts[1][-1:]) #index of the logo-i
                indexsrc2 = int(parts[2][-1:]) #index of logo-j

                if isSame(count_list,indexsrc1,indexsrc2): # logos are same then print same
                    print("Same")
                else:
                    print("Not same!") # If not same then print not same
        else:
            print("No logo found!\nPlase try again or add new logo!")
    elif parts[0] == "EXIT": #For exit
        break
    else:
        print("Unknown Input!!") 
