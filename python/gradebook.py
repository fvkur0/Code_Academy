
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# separate

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]

gradebook = [
    ["physics", 98],
    ["calculus", 97],
    ["poetry", 85],
    ["history", 88],
]

gradebook.append(["computer science", 100],)
gradebook.append(["visual arts", 93],)
gradebook[-1][1] = 97
gradebook[2][1] = "pass"

#print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)