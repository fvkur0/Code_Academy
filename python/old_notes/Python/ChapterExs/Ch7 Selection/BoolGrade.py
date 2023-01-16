def grade(mark):
    if mark >= 90:
        return "A"
    else:
        if mark >= 80:
            return "B"
        else:
            if mark >= 70:
                return "C"
            else:
                if mark >= 60:
                    return "D"
                else:
                    return "F"

mark = 89
print("Your garde is: ", grade(mark))