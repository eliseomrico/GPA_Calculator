import csv

def getNumberOfClasses():
    
    numOfClasses = 0

    while numOfClasses <= 0:
        print("\nHow many classes do you have grades for? ", end='');
        numOfClasses = int(input())
        if numOfClasses <= 0:
            print("\nERROR: # of classes must be greater than 0")
    return numOfClasses    

def printClassTable(classes):

    print("\n====================================================================================================")
    print("|     CLASS NAME          HOURS          NUMBER GRADE          LETTER GRADE     QUALITY POINTS     |")
    print("====================================================================================================")

    for name,values in classes.items():
        print("{:3s}{:24s}{:19s}{:22s}{:17s}{:.2f}".format("",name,str(values["semester_hours"]),str(values["grade"]),values["letter_grade"], values["quality_points"]))

def createCSV(classes):

    print("Enter CSV filename without .csv extension: ", end='')
    user_choice = input()
    filename = user_choice+".csv"

    # Open a file in write mode
    with open(filename, 'w') as file:

        # Headers
        file.write('CLASS_NAME,HOURS,NUMBER_GRADE,LETTER_GRADE,QUALITY_POINTS')

        # Add Classes Data
        for name,values in classes.items():
            file.write("\n{},{},{},{},{:.2f}".format(name,values["semester_hours"],values["grade"],values["letter_grade"],values["quality_points"]))

def importDataFromCSV():

    classes = {}

    # Specify the file name
    print("Enter filename without .csv extension: ", end='')
    csv_file_path = input() + ".csv"

    # Open the file in read mode
    with open(csv_file_path, 'r') as csv_file:

        # Create a CSV reader object
        csv_reader = csv.reader(csv_file)

        i = 0
        for row in csv_reader:
            if i != 0:
                classes[row[0]] = { "semester_hours":float(row[1]),"grade":int(row[2]), "letter_grade": row[3], "quality_points": float(row[4]) }
            i+=1

    return classes


def main():


    # Create class dict
    classes = {}


    # Get Class Information
    print("\nDo you want to import CSV data? ", end='')
    choice = input()


    if choice == "y":

        classes = importDataFromCSV()
        
    else:

        numOfClasses = getNumberOfClasses()

        for x in range(numOfClasses):

            # Get the number of classes
            

            print("\n==============================")
            print(f"Class {x+1}")
            print("\nEnter name: ",end='')
            className = input()
            print("Enter # of semester hours: ",end='')
            semesterHours = float(input())
            print("Enter grade: ",end ='')
            grade = int(input())
            print("\n==============================")

            # Add class entry to dict
            classes[className] = {"semester_hours":semesterHours,"grade":grade, "quality_points": 0.00, "letter_grade": ""}


    # Add Quality Points
    for name,values in classes.items():
        grade = values["grade"]

        if grade >= 95:
            values["quality_points"] = 4.00
            values["letter_grade"]   = "A"
        elif grade >= 90:
            values["quality_points"] = 3.67
            values["letter_grade"]   = "A-"
        elif grade >= 87:
            values["quality_points"] = 3.33
            values["letter_grade"]   = "B+"
        elif grade >= 84:
            values["quality_points"] = 3.00
            values["letter_grade"]   = "B"
        elif grade >= 80:
            values["quality_points"] = 2.67
            values["letter_grade"]   = "B-"
        elif grade >= 77:
            values["quality_points"] = 2.33
            values["letter_grade"]   = "C+"
        elif grade >= 70:
            values["quality_points"] = 2.00
            values["letter_grade"]   = "C"
        elif grade >= 60:
            values["quality_points"] = 1.00
            values["letter_grade"]   = "D"
        else:
            values["quality_points"] = 0.00
            values["letter_grade"]   = "F"


    # Calculate the total number of quality points (semester hours x quality points)
    total_qualtiy_points = 0
    for name,values in classes.items():
        total_qualtiy_points += (values["semester_hours"] * values["quality_points"]) 


    # Round total qualtiy points to two decimal places
    total_qualtiy_points = round(total_qualtiy_points,2)


    # Calculate total number of semester hours
    total_semester_hours = 0
    for name,values in classes.items():
        total_semester_hours += values["semester_hours"]


    # Calculate GPA (total quality points / total # of hours)
    gpa = round((total_qualtiy_points / total_semester_hours),2)


    # Print Semester Trascript
    printClassTable(classes)


    # Print all Useful information
    print(f"\nTotal quality points: {total_qualtiy_points}")
    print("Total semester hours: {:.2f}".format(total_semester_hours))
    print("Semester GPA: {:.2f}".format(gpa))

    # Prompt user if they want to create a csv
    print("\nWould you like to create a CSV Transcript (y/n)? ", end='')
    user_choice = input()

    if user_choice == "y":
        createCSV(classes)
        print("\nTrascript.csv created!")


    # Print ending space for cleaner look
    print("\n\n")


if __name__ == "__main__":
    main()