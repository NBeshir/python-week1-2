name = input("What is your name? ")


def reverse(str):

    str = name
    n = len(str)

    sliced_name = slice(-1, -n-1, - 1)

    print("Your name reversed is:", str[sliced_name])


reverse(name)
