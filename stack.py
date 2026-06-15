from ds import datastructure

stack = datastructure.Stack()

size=int(input("Enter the size of the stack: "))
while True:
    print("\nSelect an option:")
    print("1. Push an element")
    print("2. Pop an element")
    print("3. Display the stack")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if stack.is_full(size):
            print("The stack is full")
        else:
            item = input("Enter the element to push: ")
            stack.push(item)
    elif choice == 2:
        print(stack.pop())
    elif choice == 3:
        stack.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")