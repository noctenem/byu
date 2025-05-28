import pytest, random
from random_numbers import append_random_numbers, append_random_words

def test_append_random_numbers():
    numbers = [1, 2, 3]
    length = len(numbers)
    append_random_numbers(numbers,  4)
    assert len(numbers) == length + 4

    for num in numbers[length:]:
        assert 1 <= num <= 100
    
def test_append_random_words():
    words = ['hello', 'world']
    length = len(words)
    append_random_words(words, 3)
    assert len(words) == length + 3

    valid_words = ['banana', 'honeydew', 'cherry', 'apple', 'grape', 'dog', 'car']
    for word in words[length:]:
        assert word in valid_words

if __name__ == '__main__':
    pytest.main(['-v', '--tb=line', '-rN', __file__])