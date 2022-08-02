print("Welcome to Student Database of Your School")
Admin = input("Please Type your Username:")
Password = input("Please type your user")

print("***** Welcome", Admin, "to Student Result Upload system*****")
Exam = input("Please type Exam Name and Year")
StudentName = input("Please type student Full Name:")
StudentID = input("Please type student's ID:")

print("Caution: Be aware. You're About to upload marks result for", Exam, "This can not be changed.")
print("Please Enter marks for following subjects")

Hindi = int(input("Enter the marks for Hindi: "))
English = int(input("Enter the marks for English: "))
Biology = int(input("Enter the marks for Biology: "))
Physics = int(input("Enter the marks for Physics: "))
Chemistry = int(input("Enter the marks for Chemistry: "))

print("The database is printing your Result for:", Exam)
print(Hindi)
print(English)
print(Biology)
print(Chemistry)

TotalMarks = Hindi + English + Physics + Chemistry + Biology

print(TotalMarks,"/500")

overAll = ((Hindi + English + Biology + Physics + Chemistry) * 100) / 5
if overAll >= 40:
    if Hindi >= 33 and English >= 33 and Physics >= 33 and Biology >= 33 and Chemistry >= 33:
        print(StudentID, "have passed the", Exam)
    else:
        print(StudentID, "have failed the", Exam)
else:
    print(StudentID, "have failed the", Exam)