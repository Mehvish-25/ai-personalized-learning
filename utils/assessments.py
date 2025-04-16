# Simulating a function to validate user answers based on the generated quiz
def validate_answers(user_answers, correct_answers):
    score = 0
    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer.lower() == correct_answer.lower():
            score += 1
    return score
