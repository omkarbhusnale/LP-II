
def greet(bot_name, birth_year):
    print("Hello! My name is {0}.".format(bot_name))
    print("I was created in {0}.".format(birth_year))


def remind_name():
    print('Please, Tell me what is your name. ')
    name = input()
    print("What a great name you have, {0}!".format(name))


def guess_age():
    print('Let me guess your age. ')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {0} that's a good time to start programming!".format(age))


def count():
    print('Now I will prove to you that I can count to any number you want.')
    num = int(input())
    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print("What is array?")
    print("1. Class.")
    print("2. Collection of similar Data Types.")
    print("3. Collection of Multiple Data Types.")
    print("4. None of Above.")
    answer = 2
    guess = int(input())
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
        print('.................................')
        print('Completed, have a nice day!')
        print('.................................')
def end():
    print('.................................')
    print('Congratulations, have a nice day!')
    print('.................................')
    input()

greet('Shadow', '2022')
remind_name()
guess_age()
count()
test()
end()