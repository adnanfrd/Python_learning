# Program 1: Add two numbers
def add(a, b):
    return a + b

print("Sum:", add(3, 4))

def sub(a, b) :
    return a - b
print("Sub:", sub(10, 4))

# Program 2: Check if number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))