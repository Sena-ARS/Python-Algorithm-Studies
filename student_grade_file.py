def harf_notu(puan):
  if  puan < 30 :
    harfnotu = "F"
  elif 29 < puan < 50 :
    harfnotu = "C"
  elif 49 < puan < 70:
    harfnotu = "B"
  elif 69 < puan <= 100 :
    harfnotu = "A"
  return harfnotu


def report_message(student,point):
  return str(student) + " scored " + str(point) + "/100 points in Chemistry and got the grade " + harf_notu(point)
print(report_message('Zach',51))

#Creat a text file for Zach's report card and write the message inside
report_file = open("zach_report.txt", "w")
report_file.write(report_message('Zach',51))
#report_file = open("zach_report.txt","r")
#deneme = report_file.read()
report_file.close()
#print(deneme)


#Define a function that takes the student name and the points as an argument and returns them as specified in the instructions
def grade(student,point):
  try:
    return student + ": " + harf_notu(point)
  except:
    return student + 'was missing at the exam'
  #or return a message if the student was missing

print("--------------------------------------------------")

#Check if there is already a report card for Sophie and print a message in case there is
try:
  sophie_file = open("sophie_report.txt","r")
  sophie_file.read()
  sophie_file.close()
  print('There is an existing report card for Sophie.')
#If there is none, create one and write the message inside
except FileNotFoundError:
  sophie_file = open("sophie_report.txt","w")
  sophie_file.write(report_message("Sophie",78))
print("--------------------------------------------------")

student_list = [('Zach', 51), ('Sophie', 78), ('Fred', 29), ('Belina','missing'), ('Markus','missing')]
for item in student_list:
  ogrenci, puan = item
  print(grade(ogrenci,puan))

print("--------------------------------------------------")
#Create the grades.txt file
grades_file = open('grades.txt','w')
#Use the for loop to write the name and grade of each student in the file 
for student,point in student_list:
  #Write the message returned by student_grade into the file
  grades_file.write(grade(student,point))
  grades_file.write("\n")
grades_file = open('grades.txt','r')
deneme = grades_file.read()
grades_file.close()
print(deneme)
