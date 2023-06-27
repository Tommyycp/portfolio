import math

def prime_checker(number): 
    if number == 1 or number == 2: # 1 and 2 are exceptions.
        print ("Prime")
    else:
        max_divisor = math.ceil(math.sqrt(number)) #This is the maximum divisor possible.
        end = False        
        while not end:
            for i in range(2,max_divisor+1): 
                if number % i == 0: # If the number is already dividable by the smallest divisor
                    end = True 
                    print ("Not Prime")
                    break # Signal the completion of the whole iteration process because the divisor has been found.
                elif i == max_divisor: # If the for-loop continues up to its maximum divisor, the program has exhausts all the possible options for divisors
                    end = True 
                    print ("Prime")
                        
n = float(input("Type in your number"))
prime_checker(number = n)
