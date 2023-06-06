filename = 'quizlet_output.txt'

while True:
    information = 'Generate concise, unique, and interesting interview questions and answers using the following information. Clearly indicate the question starting with "Question: " and the answer with "Answer: ": '
    content = input("Enter content (or enter 'q' to quit): ")
    if content == "q":
        break
    with open(filename, "a") as file:
        file.write(information + '"' + content + '"\n\n')