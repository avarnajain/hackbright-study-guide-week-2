# Create your classes here
class Student():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.address = None 

class Question():
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        print(self.question)
        your_answer = input('type your answer here: ')

        return str(your_answer) == self.answer

class Exam():
    def __init__(self, name, exam_type='exam'):
        self.name = name
        self.questions = []
        self.exam_type = exam_type

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        points = 0
        points_per_q = 100/len(self.questions)
        for question in self.questions:
            tally = question.ask_and_evaluate()
            if tally == True:
                points += points_per_q
        return points

class Quiz(Exam):
    def __init__(self, name):
        super().__init__(name, 'quiz')

    def administer(self):
        points = super().administer()
        if points >= 50:
            return 1
        else:
            return 0


class StudentExam():
    

    def __init__(self, Student, Exam):
        self.student = Student
        self.exam = Exam
        self.score = 0


    def take_test(self):
        self.score = self.exam.administer()
        #print(self.score)

def example():
    exam = Exam('name')
    # quiz = Quiz('name')
    q1 = Question('q1', 'a1')
    q2 = Question('q2', 'a2')
    q3 = Question('q3', 'a3')
    exam.add_question(q1)
    exam.add_question(q2)
    exam.add_question(q3)
    student = Student('Avarna', 'Jain')
    studentexam = StudentExam(student, exam)
    studentexam.take_test()
    print('{} your score is {}'.format(student.first_name, studentexam.score))

example()




