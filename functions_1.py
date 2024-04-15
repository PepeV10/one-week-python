import random
from inspirational_quotes import quote

def greet():
    print("Hello World!")

greet()

import datetime
def print_date():
    print(datetime.datetime.now())

print_date()

def random_number():
    print(random.randint(1, 10))

random_number()

def show_art():
    ascii_heart = """

⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀
⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠏
    """
    print(ascii_heart)

show_art()

def print_sequence():
    for num in range(1, 11):
        print(num)

print_sequence()

def system_check():
    print("System Check Complete. All systems go!")

system_check()


def flip_coin():
    coin_toss = random.randint(0, 1)
    if coin_toss == 1:
        print("Heads")
    elif coin_toss == 0:
        print("Tails")

flip_coin()

"""
def daily_quote():
    quote = quote()
    print(quote)

daily_quote()
"""

def send_email():
    print("Sending email to contact@domain.com")
    print("Email sent successfully!")

send_email()

def is_even(num):
    return num % 2 == 0

# Example usage:
print(is_even(2))  # Output: True
print(is_even(3))  # Output: False

def slugify(phrase):
    return phrase.lower().strip().replace(" ", "-")

slugify("I really love you, but you don't love me!")

def count_vowel(phrase):
    count = 0
    for char in phrase:
        if char in "aeiou":
            count += 1
    return count

count_vowel("Hello")