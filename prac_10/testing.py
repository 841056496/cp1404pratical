"""
CP1404 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def format_sentence(phrase):
    """
    Format a phrase as a sentence: start with a capital and end with a full stop.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("this is another test")
    'This is another test.'
    """
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase.capitalize()

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    test_car1 = Car()
    assert test_car1._odometer == 0, "Car does not set odometer correctly"
    assert test_car1.fuel == 0, "Car default fuel not set correctly"

    test_car2 = Car(fuel=10)
    assert test_car2.fuel == 10, "Car fuel not set correctly when provided"

run_tests()
doctest.testmod()
