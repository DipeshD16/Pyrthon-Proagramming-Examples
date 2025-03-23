class Student:
    
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.grade = 0
        self.subjects = []
        self.marks = {}
        
    def student_details(self):
        self.name = input("Enter your name: ")
        self.roll_no = int(input("Enter your roll number: "))
        self.grade = int(input("In which class are you studying: "))
    
    def add_subjects(self):
        no_of_subject = int(input("Enter the number of subject: "))
        for i in range(1, no_of_subject+1):
            subject = input(f"subject {i}: ")
            self.subjects.append(subject)
        
    
    def term_marks(self):
        
        for subject in self.subjects:
            max_marks = int(input(f"Enter the maximum marks for {subject}: "))
            term_mark = int(input(f"Enter the mark for {subject}: "))
            self.marks[subject] = (term_mark, max_marks)

student = Student()
student.student_details()
student.add_subjects()
student.term_marks()

print(f"\nStudent's Name: {student.name}")
print(f"Student's Roll number: {student.roll_no}")
print(f"\nGrade: {student.grade}")
print("Marks")
for subject, (mark, max_mark) in student.marks.items():
    print(f"{subject}: {mark}/{max_mark}")