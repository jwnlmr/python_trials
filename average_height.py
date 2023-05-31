# 🚨 Don't change the code below 👇

def avg_height():
    student_heights = input("Input a list of student heights ").split()
    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])
    print(sum(student_heights))
    print(len(student_heights))
    avg = sum(student_heights) / len(student_heights)
    print(round(avg))
avg_height()
    
avg_height()


# below code uses for loops
# def avg_height():
#     student_heights = input("Input a list of student heights ").split()
#     for n in range(0, len(student_heights)):
#         student_heights[n] = int(student_heights[n])
#     h_total = 0
#     s_total = 0
#     for a in student_heights:
#         h_total += a
#         s_total += student_heights.count(a)
#     avg = h_total / s_total
#     print(h_total)
#     print(s_total)
#     print(student_heights)
#     print(round(avg))


# avg_height()