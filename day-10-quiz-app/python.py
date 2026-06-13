questions = {
    "What is 2 + 2?": "4",
    "What is the capital of Japan?": "Tokyo",
    "What is the largest mammal?": "Blue Whale",
    "What is the chemical symbol for water?": "H2O",
    "What is the speed of light in vacuum?": "299,792,458 m/s"
}
score = 0
for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer was:", answer)

print("Your final score is:", score, "out of", len(questions))