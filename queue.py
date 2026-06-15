from ds import datastructure

queue = datastructure.Queue()

size=int(input("Enter the size of the queue: "))

while True:
    print("\nSelect an option:")
    print("1. Enqueue an element")
    print("2. Dequeue an element")
    print("3. Display the queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if queue.is_full(size):
            print("The queue is full")
        else:
            item = input("Enter the element to enqueue: ")
            queue.enqueue(item)
    elif choice == 2:
        print(queue.dequeue())
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")