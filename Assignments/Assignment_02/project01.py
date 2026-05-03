import random, math

class MathTutor:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.operations={
            '+':lambda x, y: x+y,
            '-':lambda x, y: x-y,
            '*':lambda x, y: x*y,
            '/':lambda x, y: x/y
        }

    def generate_question(self):
        """
        Generate random 2 numbers and a choice random operation.
        """
        num1 = random.randint(1,12)
        num2 = random.randint(1,12)
        random_operation = random.choice(list(self.operations.keys()))
        return num1, num2, random_operation
    
    def play(self,rounds=5):
        """
        Main game loop!
        """
        print(f"--- Welcome to Math Tutor! Total rounds: {rounds} ---")
        for i in range(rounds):
            n1,n2,opt=self.generate_question()
            correct_answer = self.operations[opt](n1,n2)
            while True:
                try:
                    user_input= int(input(f"Round {i+1}: What is {n1} {opt} {n2}?"))
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number.")

            if user_input == correct_answer:
                print("Correct!")
                self.correct+=1
            else:
                print(f"Wrong! The answer was {correct_answer}.")
                self.incorrect+=1

        self.show_score()

    def show_score(self):
        """
        This function gets the overall game data of correct and incorrect value to generate accuracy. Most important is that this function is mostly used for showing the overall score and accuracy.
        """
        total = self.correct + self.incorrect
        if total >0:
            percentage = (self.correct/total)*100
        else:
            percentage=0.0
        print("\n Final Score")
        print(f"Correct: {self.correct} | Incorrect: {self.incorrect}")
        print(f"Accuracy: {percentage}%")

if __name__ =="__main__":
    tutor= MathTutor()
    tutor.play(rounds=3)
