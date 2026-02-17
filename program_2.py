# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.

import random

def math_question():
    n1 = random.randint(1, 999)
    n2 = random.randint(1, 999)
    print(f'{n1} + {n2}')
    return n1, n2


n1, n2 = math_question()
answer = int(input('Enter your answer: '))
correct = n1 + n2
if correct == answer:
    print('congratulations your answer is correct!')
else:
    print(f'your answer is not correct. The correct answer was {correct}')