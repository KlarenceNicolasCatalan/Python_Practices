# this is to generate a 15 element list
def setGetter():
    print("Generate 15 numbers from 10 - 30:")

    print("")
    print("#---PLEASE USE THE PROGRAM WITH ADMIN PRIVILEGES IF A PERMISSION ERROR OCCURED---#")
    print("")

    print("Values: ")

    listValues = []
    counter = 1
    whileCounter = 0

    #while loops
    while whileCounter == 0:
        for x in range(0,15):
            #--NEED TO PUT A WHILE LOOP AND CONDITIONALS FOR LESS THAN 10 AND GREATER THAN 30 NUMBERS--# 
            print("Value " + str(counter), end='')
            adder = int(input(": "))

            if adder >= 10 and adder <= 30:
                counter += 1
                listValues.append(adder)
                whileCounter = 0
                if len(listValues) <= 16:
                    whileCounter = 1

            else:
                print("")
                print("Invalid input!")
                print("You must input an integer from 10 -30")
                whileCounter = 1
    
    return listValues


def twentyCalc(_set):

    listLessThan20 = []
    greaterThan20 = 0
    for x in range(len(_set)):
        if _set[x] < 20:
            listLessThan20.append(_set[x])

    for x in range(len(_set)):
        if _set[x] > 20:
            greaterThan20 += 1

    return listLessThan20, greaterThan20

def concatenation(_list):
    list1 = []
    list2 = []

    list1 = _list[0:4]
    list2 = _list[11:15]

    conList = list1 + list2

    return conList

def sorter(_list):
    
    sortedList = []
    sortedList = _list
    sortedList.sort()

    return sortedList

#Main
list1 = setGetter()
list2 = list1
l20, g20 = twentyCalc(list1)
conList = concatenation(list1)
concList = concatenation(list2)
#The sortedList function messes up the conList list's pattern of numbers
#That is why I made another list for the concatenated first and last 4 numbers of list1
sortedList = sorter(conList)


#Text Files
note = open("c:\catalan_w2.txt", "w")
note.write("Display the numbers less than 20: \n")
note.write(str(l20))
note.write("\nCount the numbers greater than 20: \n")
note.write(str(g20))
note.write("\nCombine the first and last four number: \n")
note.write(str(concList))
note.write("\nSort the list: \n")
note.write(str(sortedList))

note.close()

#test displays
print("Values: ")
print(list1)
print("")
print("The generated output can be seen in a text file in the root folder of drive C")

print("")
note = open("c:\catalan_w2.txt", "r")
print(note.read())
note.close()

#vv Test codes below vv
#print(l20)
#print(g20)
#print(conList)
#print(sortedList)
