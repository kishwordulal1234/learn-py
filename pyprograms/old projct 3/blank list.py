l = []

while True:  # Capitalize True for the loop condition
    c = int(input('''
    1 for add data
    2 for delete element
    3 for peek element
    4 for display all elements
    5 for exit
    ''' ))

    if c == 1:
        n = input("Enter the value: ")
        l.append(n)
        print("List after adding:", l)

    elif c == 2:
        if len(l) == 0:
            print('Empty list')
        else:
            p = l.pop()
            print("Removed element:", p)
            print("List after removal:", l)

    elif c == 3:
        if len(l) == 0:
            print('Empty list')
        else:
            print("Last element:", l[-1])

    elif c == 4:
        print("Current list:", l)

    elif c == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice, please enter a number between 1 and 5.")
