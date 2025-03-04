import random

questions = {
    "What is the key difference between a list and a tuple in Python?":"Lists are mutable, tuples are immutable.",
    "Which of the following best describes list comprehensions in Python?":"A concise way to create lists based on existing iterables.",
    "What is the purpose of the __init__ method in a Python class?":"To initialize object attributes",
    "What is the difference between the == and is operators in Python?":"== checks for equality, is checks for identity.",
    "What is the primary purpose of decorators in Python?":"To modify or extend the behavior of functions or classes.",
    "What is the Global Interpreter Lock (GIL) in Python?":"A mutex that allows only one thread to execute Python bytecode at a time.",
    "How do you handle exceptions in Python?":"Using try, except, finally, and else blocks.",
    "What are lambda functions in Python?":"Anonymous, single-expression functions.",
}

def python_trivia_game():
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(questions_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("Enter your answer: ").lower().strip()
        correct_answer = questions[question].lower()

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}. \n")

    print(f"Game Over! Your final score is {score}/{total_questions}")
        
python_trivia_game()