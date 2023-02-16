x=1
marks=59
grades=89
streams=8
#if statement
if x>0:
    print("The number is positive")
    print((4+10))
#if.. else statement
if marks>=60:
    print("you have passed")
else:
    print("you have failed")

#if... elif.. else
if grades<=29 and grades>=0:
    print("you have failed")
elif grades<=49 and grades>=30:
    print("you have passed")
elif grades<=79 and grades >=50:
    print("you have credited")
elif grades<=100 and grades>=80:
    print("you have distinction")
else:
    print("wrong input")

if streams>=9 and streams<=7:
    print("form 4")
elif streams<=7 and streams>=7:
    print("form 2 and 3")
elif streams>=8 and streams<=7:
    print("form 1 junior class")
elif streams<=8 and streams>=8:
    print("form 2 classes")
else:
    print("all streams")