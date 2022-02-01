def check_prime(number):
    """
    This function checks if a number is a prime number
    param: number(int) - Inputted number by the user
    return: boolean(true / false) - returns true if prime, false if not prime
    """

    if type(number) != int and type(number) != float:
        return "Only number inputs allowed"
    else:
        ans = True
        if number <= 1 and number % 2 == 0 and number != 2:
            ans = False
        else:    
            for x in range (2, number):
                if number % x == 0:
                    ans = False

    if ans:
        ans = f"{number} is a prime number"
    else:
        factors = []
        for x in range (1, number+1):
            if not number % x:
                factors.append(x)
        ans = f"{number} is not a prime number. {factors}"

    return ans
                
    

    

print(check_prime(101))
