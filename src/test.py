import random

questions = [{
    1: {
        "question": "How are you doing?",
        "answer": "Good!"
    },
    2: {
        "question": "How old are you?",
        "answer": 22
    },
    3: {
        "question": "What is 2+2?",
        "answer": 4
    }
}]

#Write a method to retrieve all questions and answers
# for question in questions:
#     for q_id, qa in question.items():
#         question = qa["question"]
#         answer = qa["answer"]
#         print(f"Question ID {q_id} : {question}")
#         print(f"Answer : {answer}")
#         print()

# Write a method to add new question and answer in questions list
def add_new_question(question, answer):
    # Finding the next available id: (Largest existing ID + 1)
    next_id = max(questions[0].keys(), default=0) + 1
    questions[0][next_id]= {
        "question" : question,
        "answer": answer
    }
    return questions

add_new_question("What is 1 + 1", 2)

# Write a method to update existing answer
def update_existing_question(question_id, new_question, new_answer):
    if question_id in questions[0]:
        questions[0][question_id]["question"] = new_question
        questions[0][question_id]["answer"] = new_answer
    else:
        print(f"Question ID {question_id} not found!")
    return questions

# update_existing_question(1, "What is wrong with you", "Nothing!")
# print(questions)

# Write a method to remove a question
def remove_item(question_id):
    q_dict = questions[0]
    if question_id in q_dict:
        del q_dict[question_id]
    else:
        print(f"Question ID {question_id} not found!")
    return questions

remove_item(2)
print(questions)


# Write a method to generate a quiz
def generate_quiz(num_questions):
    q_dict = questions[0]
    q_ids = list(q_dict.keys())
    selected_ids = random.sample(q_ids, min(num_questions, len(q_ids)))
    quiz = {}



