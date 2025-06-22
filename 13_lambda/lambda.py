# Program 1: Square with lambda
square = lambda x: x * x
print(square(6))


# Program 2: Sort by string length
words = ["apple", "banana", "kiwi"]
words.sort(key=lambda word: len(word))
print(words)