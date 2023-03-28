################ Function Definitions ################

# Shows the user what options they have
def displayMenu():

  # This option will involve you adding a student and a collection for their grades to a dictionary!
  print("1. Add a Student")

  # This option will involve you removing a pair from a dictionary!
  print("2. Remove a Student")

  # This option will require you to grab a student from a dictionary and add a quiz grade to it's corresponding collection of grades!
  # You'll also need to use a pre-written function that ensures the user is entering a valid grade (a decimal number)
  print("3. Add Quiz Grade for Student")

  # This option will require you to use a loop to list all of the grades for an INDIVIDUAL student!
  print("4. List a Student's Quiz Grades")

  # This option will have you write a function that takes in a student's grade as a number and return the letter grade equivalent!
  print("5. Get Student's Letter Grade")

  print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works, and ensures the user entered a valid float for the grade
# It's not important HOW this function works, but how to USE this function
def getNumberGradeFromUser():

  val = None

  while(val == None):
    try:
      test = float(input("Enter a Grade: "))
      val = test
    except:
      val = None
  
  return val

################ Main Program ################

# Create/Initialize an empty dictionary to hold students' information
students = {}

# Create function to add student
def addStudent():
  name = input("Enter the student's name: ")
  # Add student to dictionary with an empty list
  students[name] = []
  print(f"{name} added!")

# Create function to remove student
def removeStudent():
  name = input("Enter the student's name: ")
  if(name in students):
    students[name].pop()
    print(f"{name} removed!")
  else:
    print(f"{name} not in dictionary!")

# Create function to add a quiz grade for a students
def addQuizGrade():
  name = input("Enter the student's name: ")
  if(name in students):
    grade = getNumberGradeFromUser()
    # Add grade to student's list of grades
    students[name].append(grade)
    print(f"Added {grade} to {name}'s quizzes")
  else:
    print(f"{name} not in dictionary!")

# Create function to list a student's quiz grade
def listQuizGrades():
  name = input("Enter the student's name: ")
  if(name in students):
    grades = students[name]
    print(f"{name}'s quizzes:")
    for grade in grades:
      print(grade)
  else:
    print(f"{name} not in dictionary!")

# Create function to get a student's letter grade
def getLetterGrade():
  name = input("Enter the student's name: ")
  if(name in students):
    grades = students[name]
    avg = sum(grades) / len(grades)
    if(avg >= 90):
      print("A")
    elif(avg >= 80):
      print("B")
    elif(avg >= 70):
      print("C")
    elif(avg >= 60):
      print("D")
    elif(avg >= 50):
      print("E")
    else:
      print("F")
  else:
    print(f"{name} not dictionary!")

# Application Loop
while(True):
  
  print()
  displayMenu()
  
  # Prompt user to select an option
  option = input("Select an option: ")

  # Perform the selected option
  if(option == "1"):
    addStudent()

  elif(option == "2"):
    removeStudent()

  elif(option == "3"):
    addQuizGrade()

  elif(option == "4"):
    listQuizGrades()

  elif(option == "5"):
    getLetterGrade()
 
  elif(option == "6"):
    break # Quit the program
    
  else:
    print("Invalid option. Please try again!")

  print()
