# this calculates the highest scores among inputs from users

def highest_score() -> int:
    student_scores = input("Input a list of student scores ").split()
    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)

    highest = student_scores[0]  # Initialize the highest score with the first element

    for score in student_scores:
        if score > highest:
            highest = score

    print(f"The highest score is: {highest}")

highest_score()