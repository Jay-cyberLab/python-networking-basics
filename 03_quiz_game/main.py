questions = [
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Control Program Unit"],
        "answer": "A"
    },
    {
        "question": "Which protocol is used to load websites?",
        "options": ["A. FTP", "B. HTTP", "C. SSH"],
        "answer": "B"
    },
    {
        "question": "Which Python data type uses key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary"],
        "answer": "C"
    },
    {
        "question": "What does RAM stand for?",
        "options": ["A. Read Access Memory", "B. Random Access Memory", "C. Run Active Memory"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for web page structure?",
        "options": ["A. HTML", "B. Python", "C. SQL"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False values in Python?",
        "options": ["A. String", "B. Boolean", "C. Integer"],
        "answer": "B"
    },
    {
        "question": "Which device is used to connect a computer to a network?",
        "options": ["A. Router", "B. Printer", "C. Scanner"],
        "answer": "A"
    },
    {
        "question": "What does URL stand for?",
        "options": ["A. Universal Reference Link", "B. Uniform Resource Locator", "C. Unified Routing Language"],
        "answer": "B"
    },
    {
        "question": "Which Python keyword is used to define a function?",
        "options": ["A. function", "B. define", "C. def"],
        "answer": "C"
    },
    {
        "question": "Which of the following is an operating system?",
        "options": ["A. Linux", "B. HTML", "C. Google Chrome"],
        "answer": "A"
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": ["A. //", "B. **", "C. %%"],
        "answer": "B"
    },
    {
        "question": "Which SQL command is used to retrieve data from a database?",
        "options": ["A. INSERT", "B. UPDATE", "C. SELECT"],
        "answer": "C"
    }

]

def get_valid_answer():
    while True:
        user_answer = input("Your answer (A, B or C) : ").strip().upper()

        if user_answer in ["A", "B", "C"]:
            return user_answer
        else:
            print("Invalid answer. Please enter A, B or C.")

score = 0

print("Welcome to the Python and Networking Quiz!")

for question_numbers, question_data in enumerate(questions,start = 1):
    print(f"\nQuestion {question_numbers} : {question_data['question']}")

    for option in question_data["options"]:
        print(option)

    user_answer = get_valid_answer()

    if user_answer == question_data["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {question_data['answer']}.")


percentage = (score / len(questions)) * 100
print("\n----- Quiz Complete -----")
print(f"your score : {score}/{len(questions)}")
print(f"Percentage : {percentage:.0f}%")

if percentage == 100:
    print("Excellent! Perfect score.")
elif percentage >= 60:
    print("Good job. Keep practcing.")
else:
    print("Keep learning you will imporve.")


