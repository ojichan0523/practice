int = int(input("Enter a positive integer: "))


def main():
    is_prime = True
    if int == 0 or int == 1:
        is_prime = False

    for i in range(2, int, 1):
        if int % i == 0:
            is_prime = False
            break

    if is_prime:
        print(str(int) + " is a prime number")
    else:
        print(str(int) + " is not a prime number")


main()
