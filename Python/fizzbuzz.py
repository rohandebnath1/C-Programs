def fizz_buzz(inp):
    if (inp%3 == 0) and (inp%5 == 0):
        return "FizzBuzz"
    if inp%3==0:
        return "Fizz"
    if inp%5==0:
        return "Buzz"
    return inp
input = int(input("Enter the number: "))
print (fizz_buzz(7))
