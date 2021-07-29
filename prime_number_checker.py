print("""
╔═╗┬─┐┬┌┬┐┌─┐  ╔╗╔┬ ┬┌┬┐┌┐ ┌─┐┬─┐  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
╠═╝├┬┘││││├┤   ║║║│ ││││├┴┐├┤ ├┬┘  ║  ├─┤├┤ │  ├┴┐├┤ ├┬┘
╩  ┴└─┴┴ ┴└─┘  ╝╚╝└─┘┴ ┴└─┘└─┘┴└─  ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘┴└─
""")

def prime_number_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print(f"{number} a prime number.\n")
  else:
    print(f"{number} is not a prime number.\n")

while True:
    n = int(input("Check this number: "))
    prime_number_checker(n)

    response = input("Do you want to check another number? Tpye 'yes' or 'no': ").lower()

    if response == "no":
        print("Thank you!")
        break
    elif response == "yes":
        continue

