def converMarks(markset):
	for name in markset:
		for subject in markset[name]:
			mark = markset[name][subject]
			grade = grader(mark)
			markset[name][subject]=grade
	return markset


def grader(score):
	if score > 90: 
		return "A"
	elif score > 80:
		return "B"
	elif score > 70:
		return "C"
	elif score > 60:
		return "D"
	elif score > 50:
		return "E+"
	elif score > 40:
		return "E"
	else:
		return "F"

name = input().split()

d = {}
for i in name:
    d[i] = {}
    subjects = input().split()
    marks = input().split()
    for j in range(len(subjects)):
        d[i][subjects[j]] = int(marks[j])

print(converMarks(d))