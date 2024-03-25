class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_question(self):
        return self.question

    def get_answer(self):
        return self.answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def take_quiz(self):
        for question in self.questions:
            print(question.get_question())
            user_answer = int(input("Your answer: "))
            if user_answer == question.get_answer():
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect!\n")
        print("Your final score is: {}/{}".format(self.score, len(self.questions)))


if __name__ == "__main__":
    print("Enter your Name: ")
    name = input()
    print("Hi", name)
    print("Are you ready to start the game: \nEnter yes/No")
    opinion = input()
    if opinion.lower() == "no":
        print("Thank you!\nHave a nice day!!")
    else:
        # Create questions
        questions = [
            Question("What is 2 + 2 ?", 4),
            Question("What is 2 * 2 ?", 4),
            Question("What is 1000 - 996 ?", 4)
        ]
        # Start the quiz
        quiz = Quiz(questions)
        quiz.take_quiz()
