import random
import requests

QUESTION_COUNT = 10

url = f"https://opentdb.com/api.php?amount={QUESTION_COUNT}"

questions = {}
r = requests.get(url)
data = r.json()
for result in data['results']:
    question = result['question']
    correct_answer = result['correct_answer']
    questions[question] = correct_answer

def python_trivia_game():
    questions_list = list(questions.keys())
    custome_question = int(input("How many questions would you like to answer? "))
    total_questions = custome_question or QUESTION_COUNT
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