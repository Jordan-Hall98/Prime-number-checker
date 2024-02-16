#Defining a prime number checker

def prime_checker(number):
  '''Checks an inputted number to see if it is a prime'''
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")   

#Create a boolean variable to be used in the while loop
stop_asking = False

#While loop to keep using prime checker function until user requests otherwise
while not stop_asking:
  if input("Would you like to check for a prime number? Type 'y' for yes or anything else for no: ").lower() == "y":
    n = int(input("What number would you like to check to see if it is a prime number: ")) 
    prime_checker(n)
  else: 
    stop_asking = True