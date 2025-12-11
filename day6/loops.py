import random
student_scores = [150,142,185,120,171,199,184,149,24,59,68,78,65,89,86]

max_score= max(student_scores)
print(max_score)

#find max score with python
print("############################")

highest_score =0
for score in student_scores:

    if score>highest_score:
        highest_score = score

print(highest_score)