queue = []
qLimit = 5

#ENQUEUE--------------------------------------------------------------

def enqueuer():
    #counter for non null values (aka, values that are in queue)
    #This is made as to not trigger the qLimit when there are 5 'null' values in the queue
    counter = 0
    for n in queue:
        if n != 'null':
            counter += 1
    
    if counter == qLimit:
        print ("The queue is already FULL.")
        print()
        main()
    else:
        enqueue = input("Enter a value to the queue: ")
        queue.append(enqueue)

        #Extra details ALWAYS USE BREAK to stop a loop
        for x in queue:
            if x != 'null':
                print("Front item: ", x)
                break

        for y in range(len(queue)):
            if queue[y] != 'null':
                print("Front index: ", y)
                break
        
        print("Rear item: ", queue[-1])
        rIndex = len(queue) - 1
        print("Rear index: ", rIndex)
        
        print("[", end = "")
        for q in queue:
            if q != 'null':
                print(q, end = ", ")
        print("]")

        #Try again
        tryAgain = input("Would you like to ENQUEUE again? (y/n): ")

        if tryAgain == 'y' or tryAgain == 'Y':
            print()
            enqueuer()
        elif tryAgain == 'n' or tryAgain == 'N':
            main()
        else:
            print()
            enqueuer()

#DEQUEU------------------------------------------------------------------

def dequeuer():
    if len(queue) == 0:
        print ("The queue is already EMPTY.")
        print()
        main()
    else:
        for z in range(len(queue)):
            if queue[z] != 'null':
                queue[z] = 'null'
                #a break here to stop the loop from giving 'null' values to all of the values in the queue
                break

        #Extra details ALWAYS USE BREAK to stop a loop
        for x in queue:
            if x != 'null':
                print("Front item: ", x)
                break

        for y in range(len(queue)):
            if queue[y] != 'null':
                print("Front index: ", y)
                break
        
        if queue[-1] == 'null':
            print("Empty")
        else:
            print("Rear item: ", queue[-1])

        rIndex = len(queue) - 1
        print("Rear index: ", rIndex)

        print("[", end = "")
        for q in queue:
            if q != 'null':
                print(q, end = ", ")
        print("]")

        #Try again
        tryAgain = input("Would you like to DEQUEUE again? (y/n): ")

        if tryAgain == 'y' or tryAgain == 'Y':
            print()
            dequeuer()
        elif tryAgain == 'n' or tryAgain == 'N':
            main()
        else:
            print()
            dequeuer()


#----------------------MENU-------------------------
def main():
    print()
    print("[1] Enqueue")
    print("[2] Dequeue")
    print("[3] Exit")
    choice = input("Input your choice (1, 2, or 3): ")

    print()
    #Validation of the entered values
    if choice == '1':
        enqueuer()
    elif choice == '2':
        dequeuer()
    elif choice == '3':
        quit()
    else:
        main()


#----------------------MAIN-------------------------

main()
