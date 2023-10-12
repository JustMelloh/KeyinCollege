# Comment like a pro.

quizTitle = input("Enter the title for the Quiz: ")
numQuestions = int(input("Enter the number of questions for the Quiz: "))

'''
ansKey = []
for i in range (1, numQuestions + 1):
    Answer = input("Enter the answer for question " + str(i) + ": ").upper()
    ansKey.append(Answer)
print(ansKey)
'''

ansKey = ['A', 'B', 'C', 'D', 'A']

numQuizzes = int(input("How many quizzes are to be graded?: "))
for j in range(1, numQuizzes + 1):
    studentName = input("Enter the student name: ")
    studentAnswer = []
    for i in range (1, numQuestions + 1):
        Answer = input("Enter the answer for question " + str(i) + ": ").upper()
        studentAnswer.append(Answer)

    # Compare the student answers with the answer key.
    # Keep track of the number they get correct.
    # Calculate the grade.
    # Store the name, number correct and the grade in three lists.

# Display the output based on the printer spacing chart provided.