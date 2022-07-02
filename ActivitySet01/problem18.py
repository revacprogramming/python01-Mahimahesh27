#3B

s=float(input("Enter the s obtained"))
if s<0 or s>100:
    print("Invalid s")
elif s<=35:
    print("Grade F")
elif s>=36 and s<=50:
    print("Grade E")
elif s>=51 and s<=60:
    print("Grade D")
elif s>=61 and s<=70:
    print("Grade C")
elif s>=71 and s<=80:
    print("Grade B")
elif s>=81 and s<=90:
    print("Grade A")
else:
    print("Grade O - Outstanding")