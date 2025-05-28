import random

def append_random_numbers(number_list, quantity = 1):
    for _ in range(quantity):
        number_list.append(random.randint(1,100))

def append_random_words(words_list, quantity = 1):
    words = ['banana', 'honeydew', 'cherry', 'apple', 'grape', 'dog', 'car']

    for _ in range(quantity):
        words_list.append(random.choice(words))

def main():
    numbers = [10, 20, 30]
    words = ['hello', 'world']

    print('Initial list of numbers:', numbers)

    append_random_numbers(numbers)
    print('After adding a random number:', numbers)

    append_random_numbers(numbers, 3)
    print('After adding three random numbers:', numbers)

    print('Initial list of words:', words)

    append_random_words(words)
    print('After adding a random word:', words)

    append_random_words(words, 2)
    print('After adding two random words:', words)

if __name__ == '__main__':
    main()