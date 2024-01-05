
todoList = []

def userInterface():
    print("1 - Add items to the list")
    print("2 - Remove items from the list")
    print("3 - Check the list")
    print("4 - Save the list to a .txt")
    print("5 - Load a .txt file to modify")
    print("6 - Quit")
    print("c - Clear the list")

def saveTodoList(todoList):
    filename = "todo_list.txt"
    with open (filename, "w") as file:
        for i, item in enumerate(todoList, start = 1):
            file.write(f"{i}. {item}\n")
            
        print(f"List saved to {filename}")

def loadTodoList(todoList):
    
    filename = "todo_list.txt"
    with open (filename, "r") as file:
        lines = file.readlines()

        todoList.clear()

        for line in lines:
            item = line.strip().split('. ')[-1]
            todoList.append(item)


def programLoop(exit = True):
    while exit:
        
        userInterface()
        userInput = input()

        if todoList == [] and userInput == "3":
            print("Empty List\n")

        elif userInput == "1":
            enterItem = input()
            todoList.append(enterItem)

        elif userInput == "2":
            enterItem = input()
            if enterItem in todoList:
                todoList.remove(enterItem)
            else: 
                print("Item does not Exist")

        elif userInput == "3":
            print(todoList,"\n")

        elif userInput == "4":
            saveTodoList(todoList)

        elif userInput == "5":
            loadTodoList(todoList)

        elif userInput == "6":
            print("\nThe program will now close")
            break 

        elif userInput == 'c':
            todoList.clear()
            print("\nThe list has been cleared")
        else:
            print("\nInvalid Input, Please try again")


programLoop(exit=True)
