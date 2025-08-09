# prime number code

number = 2
k = 0

if number > 1:

    for j in range(1, number + 1):

        if number % j == 0:
            k += 1

if k == 2:
    print("yes")
else:
    print("no")