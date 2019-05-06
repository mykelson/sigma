def main():
    num = get_positive_int("Positive integer please: ")

    answer = sigma(num)
    print(f"The sigma of {num} is {answer}")

def get_positive_int(prompt):
    """ Recursively request for a positive integer """
    while True:
        n = int(input(prompt), 10)
        if n > 0:
            break
        
    return n

def sigma(m):
    """ Calculate the factorial of a given number """
    if(m <= 0):
        return 0
    else:
        return (m + sigma(m - 1))

if __name__ == "__main__":
    main()