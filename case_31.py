answer_key = ["a", "c", "b", "d", "a"]
correct_marks = 2
negative_marks = 0.5

answers = input("Enter 5 answers separated by spaces (- if blank): ").lower().split()

if len(answers) != len(answer_key):
    print("Please enter exactly 5 answers")
else:
    correct = incorrect = unanswered = 0

    for i in range(len(answer_key)):
        if answers[i] == "-":
            unanswered += 1
        elif answers[i] == answer_key[i]:
            correct += 1
        else:
            incorrect += 1

    score = correct * correct_marks - incorrect * negative_marks
    print("Correct answers:", correct)
    print("Incorrect answers:", incorrect)
    print("Unanswered questions:", unanswered)
    print("Final score:", score)
