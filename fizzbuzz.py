for i in range(21):

    flag = 0

    if i == 0:
        None
    
    else:
        if (i) % 3 == 0:
            print("Fizz", end="")
            flag = 1

        if (i) % 5 == 0:
            print("Buzz", end="")
            flag = 1

        if flag == 0:
            print(i)
        
        else:
            print()
