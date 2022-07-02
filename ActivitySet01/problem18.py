#3B


marks=float(input("Enter the marks obtained"))
if marks<0 or marks>100:
    print("Invalid marks")
elif marks<=35:
    print("Grade F")
elif marks>=36 and marks<=50:
    print("Grade E")
elif marks>=51 and marks<=60:
    print("Grade D")
elif marks>=61 and marks<=70:
    print("Grade C")
elif marks>=71 and marks<=80:
    print("Grade B")
elif marks>=81 and marks<=90:
    print("Grade A")
else:
    print("Grade O - Outstanding")