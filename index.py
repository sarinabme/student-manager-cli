from os import system
from random import randint
from time import sleep




student_list = [

]


while True:
    # region show menu options
    print("---------------------------------------------------------")
    print("1. [A]dd")
    print("2. [D]isplay")
    print("3. [RE]move")
    print("4. [E]dit")
    print("5. [S]earch")
    print("6. [R]eport")
    print("7. [Q]uit")
    print("---------------------------------------------------------")
    # endregion
    menu = input("Menu: ")
    system("cls")
    match menu:

        case "1" | "A":
            while True:
                # region continue
                ans = input("Do you want to add a student (yes-etc): ")
                system("cls")

                if ans != "yes":
                    break
                # endregion

                # region add code
                while True:
                    code = randint(1, len(student_list) + 1)  # 3
                    # region check duplicate code
                    dup = False
                    for student in student_list:
                        if student[0] == code:
                            dup = True
                            break
                    # endregion
                    if not dup:
                        break
                # endregion

                # region add first name
                while True:
                    first_name = input("Please enter student first name: ")
                    system("cls")

                    if first_name == "":
                        print("First name is empty! Please try again!")
                        continue
                    break
                # endregion

                # region add last name
                while True:
                    last_name = input("Please enter student last name: ")
                    system("cls")

                    if last_name == "":
                        print("Last name is empty! Please try again!")
                        continue
                    break
                # endregion

                # region add age
                while True:
                    age = input("Please enter student age: ")
                    system("cls")

                    if age == "":
                        print("Age is empty!")
                        continue

                    elif age in [str(i) for i in range(1, 100)]:
                        break
                    print("Age is out of range! Please try again.")
                # endregion

                # region add national code
                while True:
                    national_code = input("Please enter student national code: ")
                    system("cls")

                    if national_code == "":
                        print("National code is empty!")
                        continue

                    # region check duplicate national code
                    dup = None
                    for student in student_list:
                        if student[4] == national_code:
                            dup = student[4]
                            break
                    # endregion

                    if dup == None:
                        break
                    print("Duplicate national code:", dup, "! Try another.")

                # endregion
                
                # region add student code
                while True:
                    student_code = input("Please enter student code: ")
                    system("cls")

                    if student_code == "":
                        print("Student code is empty!")
                        continue

                    # region check duplicate student code
                    dup = None
                    for student in student_list:
                        if student[5] == student_code:
                            dup = student[5]
                            break
                    # endregion

                    if dup == None:
                        break
                    print("Duplicate student code:", dup, "! Try another.")
                # endregion

                # region class
                while True:
                    classes = ("A", "B", "C")
                    class_ = input("Please enter student class[A, B, C]:")
                    system("cls")

                    if class_ == "":
                        print("Class cannot be empty.")
                        continue

                    elif class_ in ("A", "B", "C"):
                        break

                    print("Invalid class! Please enter A, B, or C.")
                # endregion

                # region add php score
                while True:
                    php_score = input("Please enter PHP score (0-100): ")
                    system("cls")

                    if php_score == "":
                        print("Score cannot be empty.")
                        continue

                    elif php_score in [str(i) for i in range(0, 101)]:
                        break

                    print("Score must be between 0 and 100! Try again.")
                # endregion

                # region add python score
                while True:
                    python_score = input("Please enter Python score (0-100): ")
                    system("cls")

                    if python_score == "":
                        print("Score cannot be empty.")
                        continue

                    elif python_score in [str(i) for i in range(0, 101)]:
                        break

                    print("Score must be between 0 and 100! Try again.")
                # endregion

                # region add java score
                while True:
                    java_score = input("Please enter Java score (0-100): ")
                    system("cls")

                    if java_score == "":
                        print("Score cannot be empty.")
                        continue

                    elif java_score in [str(i) for i in range(0, 101)]:
                        break

                    print("Score must be between 0 and 100! Try again.")
                # endregion

                # region add status
                while True:
                    status = input("Please enter the status (active/deactive): ")
                    system("cls")

                    if status == "":
                        print("Status is empty! Please try again!")
                        continue

                    elif status in ("active", "deactive"):
                        break

                    print("Status is not valid! Please try again.")
                # endregion

                # region display current student
                print("-----------------------------------------------")
                print("Name:", first_name)
                print("Family:", last_name)
                print("Age:", age)
                print("National code:", national_code)
                print("Student code:", student_code)
                print("Class:", class_)
                print("PHP score:", php_score)
                print("Python score:", python_score)
                print("Java score:", java_score)
                print("Status:", status)
                print("-----------------------------------------------")
                # endregion

                # region add student
                if (
                    input("Are you sure you want to add the above student (yes-etc): ")
                    != "yes"
                ):
                    continue

                student = [code, first_name, last_name, age, national_code, student_code, class_, php_score, python_score, java_score, status]
                student_list.append(student)
                print("\nStudent Added to the Student List!")
                sleep(3)
                system("cls")
                # endregion

        case "2" | "D":
            while True:
                # region continue
                ans = input("Do you want to see a student list (yes-etc): ")
                system("cls")
                if ans != "yes":
                    break
                # endregion

                # region ask about columns
                if input("Do you want to see all columns (yes-etc)? ") == "yes":
                    system("cls")
                    display_col = ("Code", "Name", "Family", "Age", "Nat", "Stu", "Class", "PHP", "Python", "Java", "Status")
                    display_indexes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                else:
                    # region select columns
                    display_col = []
                    display_indexes = []
                    while True:
                        # region get column
                        input_col = input(
                            "Select Columns: [1].[C]ode [2].[N]ame [3].[F]amily [4].[A]ge [5].[Na]tional [6].[S]tudent [7].[Cl]ass [8].[P]HP [9].[Py]thon [10].[J]ava [11].[St]atus\n OR [12].[E]nd\nSelect: "
                        )
                        system("cls")
                        # endregion

                        # region add columns
                        match input_col:

                            case "1" | "C":
                                if "Code" not in display_col:
                                    display_col.append("Code")
                                    display_indexes.append(0)

                            case "2" | "N":
                                if "Name" not in display_col:
                                    display_col.append("Name")
                                    display_indexes.append(1)

                            case "3" | "F":
                                if "Family" not in display_col:
                                    display_col.append("Family")
                                    display_indexes.append(2)

                            case "4" | "A":
                                if "Age" not in display_col:
                                    display_col.append("Age")
                                    display_indexes.append(3)

                            case "5" | "Na":
                                if "National" not in display_col:
                                    display_col.append("National")
                                    display_indexes.append(4)

                            case "6" | "S":
                                if "Student" not in display_col:
                                    display_col.append("Student")
                                    display_indexes.append(5)

                            case "7" | "Cl":
                                if "Class" not in display_col:
                                    display_col.append("Class")
                                    display_indexes.append(6)

                            case "8" | "P":
                                if "PHP" not in display_col:
                                    display_col.append("PHP")
                                    display_indexes.append(7)

                            case "9" | "Py":
                                if "Python" not in display_col:
                                    display_col.append("Python")
                                    display_indexes.append(8)

                            case "10" | "J":
                                if "Java" not in display_col:
                                    display_col.append("Java")
                                    display_indexes.append(9)

                            case "11" | "St":
                                if "Status" not in display_col:
                                    display_col.append("Status")
                                    display_indexes.append(10)


                            case "12" | "E":
                                break

                            case _:
                                print("Invalid select option!")
                        # endregion
                    # endregion
                # endregion

                if len(display_indexes):
                    # region display students
                    print(
                        "=============================================================================="
                    )
                    print("Row", *display_col, sep="\t")
                    print(
                        "--------------------------------------------------------------------"
                    )
                    for row, student in enumerate(student_list, 1):
                        print(row, *(student[i] for i in display_indexes), sep="\t")
                    print(
                        "=============================================================================="
                    )
                    sleep(3)
                    # endregion

        case "3" | "RE":
            while True:
                # region continue
                ans = input("Do you want to remove a student (yes-etc): ")
                system("cls")

                if ans != "yes":
                    break
                # endregion

                display_col = ("Code", "Name", "Family", "Age", "Nat", "Stu", "Class", "PHP", "Python", "Java", "Status")
                display_indexes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

                # region select remove col
                while True:
                    # region display students
                    print("==============================================================================")
                    print("Row", *display_col, sep="\t")
                    print("--------------------------------------------------------------------")
                    for row, student in enumerate(student_list, 1):
                        print(row, *(student[i] for i in display_indexes), sep="\t")
                    print("==============================================================================")
                    # endregion

                    remove_col = input("Select Columns: [1].[C]ode [2].[N]ame [3].[F]amily [4].[A]ge [5].[Na]tional [6].[S]tudent [7].[Cl]ass [8].[P]HP [9].[Py]thon [10].[J]ava [11].[St]atus\nSelect: ")
                    system("cls")
                    if remove_col in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "C", "N", "F", "A", "Na", "S", "Cl", "P", "Py", "J", "St"):
                        break
                    print("Remove column is not valid!")
                # endregion

                # region match remove column
                match remove_col:
                    case "1" | "C":
                    # region r code
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Code :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[0]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 0
                    #endregion

                    case "2" | "N":
                    # region r name
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Name :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[1]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 1
                    #endregion

                    case "3" | "F":
                    # region r family
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Family :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[2]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 2
                    #endregion

                    case "4" | "A":
                    # region r age
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Age :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[3]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 3
                    #endregion

                    case "5" | "Na":
                    # region r national
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Code :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[4]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 4
                    #endregion

                    case "6" | "S":
                    # region r student
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Student :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[5]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 5
                    #endregion

                    case "7" | "Cl":
                    # region r class
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Class :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[6]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 6
                    #endregion
                
                    case "8" | "P":
                    # region r php
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("PHP :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[7]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 7
                    #endregion

                    case "9" | "Py":
                    # region r python
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Python :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[8]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 8
                    #endregion
                
                    case "10" | "J":
                    # region r java
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Java :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[9]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 9
                    #endregion

                    case "11" | "St":
                    # region r status
                        while True:
                            print("=========================================================================")
                            print("Row", *display_col, sep="\t")
                            print("---------------------------------------------------------------")
                            for row, student in enumerate(student_list, 1):
                                print(row, *(student[i] for i in display_indexes), sep="\t")
                            print("=========================================================================")
                            sleep(3)

                            val = input("Status :")
                            system("cls")
                            if not val:
                                print("Empty Field!")
                                continue
                            found = False
                            for student in student_list:
                                if int(val) == student[10]:
                                    found = True
                                    break

                            if found:
                                break

                        print("Does not even exist.")
                        search_index = 10
                    #endregion

                system("cls")
                found = False
                for student in student_list.copy():
                    if student[search_index] == (int(val) if search_index == 0 else val):
                        found = True
                        # region display current student
                        print("-----------------------------------------------")
                        print("Name:", student[1])
                        print("Family:", student[2])
                        print("Age:", student[3])
                        print("National:", student[4])
                        print("Student:", student[5])
                        print("Class:", student[6])
                        print("PHP:", student[7])
                        print("Python:", student[8])
                        print("Java:", student[9])
                        print("Status:", student[10])
                        print("-----------------------------------------------")
                        # endregion

                        remove_ans = input("Do you want to remove the above student (yes-etc)? ")
                        system("cls")
                        if remove_ans == "yes":
                            student_list.remove(student)
                            system("cls")
                            print("Done.")

                if not found:
                    print("No record Found...")
                #endregion

        case "4" | "E":
            while True:
                # region continue
                ans = input("Do you want to edit a student (yes-etc): ")
                system("cls")
                if ans != "yes":
                    break
                # endregion

                display_col = ("Code", "Name", "Family", "Age", "Nat", "Stu", "Class", "PHP", "Python", "Java", "Status")
                display_indexes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

                # region select edit col
                while True:
                    # region display students
                    print(
                        "==============================================================="
                    )
                    print("Row", *display_col, sep="\t")
                    print(
                        "---------------------------------------------------------------"
                    )
                    for row, student in enumerate(student_list, 1):
                        print(row, *(student[i] for i in display_indexes), sep="\t")
                    print(
                        "==============================================================="
                    )
                    # endregion
                    edit_col = input("Select columns to edit: 1.[C]ode 2.[S]tudent \nSelect: ")
                    system("cls")
                    if edit_col in ("1", "2", "C", "S"):
                        break
                    print("Edit column is not valid!")
                # endregion

                # region match edit column
                match edit_col:
                    case "1" | "C":
                        # region get code
                        while True:
                            # region display students
                            print(
                                "========================================================================="
                            )
                            print("Row", *display_col, sep="\t")
                            print(
                                "-------------------------------------------------------------------------"
                            )
                            for row, student in enumerate(student_list, 1):
                                print(
                                    row, *(student[i] for i in display_indexes), sep="\t"
                                )
                            print(
                                "========================================================================="
                            )
                            # endregion

                            val = input("Code :")
                            system("cls")
                            if not val:
                                print("Empty field!")
                                continue

                            found = False
                            for student in student_list:
                                if int(val) == student[0]:
                                    found = True
                                    break
                            if found:
                                break

                            print("Does not even exist.")
                        search_index = 0
                        # endregion

                    case "2" | "S":
                        # region get student
                        while True:
                            # region display students
                            print(
                                "==============================================================="
                            )
                            print("Row", *display_col, sep="\t")
                            print(
                                "---------------------------------------------------------------"
                            )
                            for row, student in enumerate(student_list, 1):
                                print(
                                    row, *(student[i] for i in display_indexes), sep="\t"
                                )
                            print(
                                "==============================================================="
                            )
                            # endregion
                            val = input("Student code: ")
                            system("cls")
                            if not val:
                                print("Empty field!")
                                continue

                            found = False
                            for student in student_list:
                                if int(val) == student[5]:
                                    found = True
                                    break
                            if found:
                                break

                            print("Does not even exist.")
                        search_index = 5
                        # endregion

                system("cls")
                # endregion

                found = False
                for student in student_list.copy():
                    if student[search_index] == (int(val) if search_index == 0 else val):
                        found = True
                        # region display current student
                        print("-----------------------------------------------")
                        print("Name:", student[1])
                        print("Family:", student[2])
                        print("Age:", student[3])
                        print("National:", student[4])
                        print("Student:", student[5])
                        print("Class:", student[6])
                        print("PHP:", student[7])
                        print("Python:", student[8])
                        print("Java:", student[9])
                        print("Status:", student[10])
                        print("-----------------------------------------------")
                        # endregion

                        edit_ans = input("Do you want to edit the above student (yes-etc)? ")
                        system("cls")
                        if edit_ans == "yes":
                            # region edit current student
                            while True:
                                edit_item = int(input("\nSelect item to edit: [1].Name [2].Family [3].Age [4].National [5].Student [6].Class [7].PHP [8].Python [9].Java [10].Status\nSelect: "))
                                system("cls")
                                if edit_item:
                                    break
                                print("Edit item is empty!")
                            # endregion
                            # region new value
                            new_value = input("Please enter new value: ")
                            system("cls")
                            if edit_item in (1, 2):
                                new_value = str(new_value)

                            elif edit_item in (3, 4, 5, 6, 7, 8, 9):
                                new_value = int(new_value)

                            if edit_item == 10:
                                while True:
                                    choice = input("Please enter [1].Active or [2].Deactive: ")
                                    if choice == "1":
                                        student[10] = "active"
                                        break
                                    elif choice == "2":
                                        student[10] = "deactive"
                                        break
                                    else:
                                        print("Error! please enter 1 or 2.")
                                        system("cls")
                            student[edit_item] = new_value
                            print("Student updated succesfully.")
                            system("cls")
                            break

                            #endregion


                if not found:
                    print("No record Found...")

        case "5" | "S":
            while True:
                # region continue
                ans = input("Do you want to search a student (yes-etc): ")
                system("cls")

                if ans != "yes":
                    break
                # endregion

                # region get search
                while True:
                    value = input("Search value: ")
                    system("cls")
                    if not value:
                        print("Value is empty!")
                        continue
                    break
                # endregion

                found = False
                # region show students
                display_col = ("Code", "Name", "Family", "Age", "Nat", "Stu", "Class", "PHP", "Python", "Java", "Status")
                display_indexes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                print("==============================================================================")
                print("Row", *display_col, sep="\t")
                print("------------------------------------------------------------------------------")
                for row, student in enumerate(student_list, 1):
                    if value in student:
                        found = True
                        print(row, *(student[i] for i in display_indexes), sep="\t")

                if not found:
                    print("This value does not exist!")
                print("=============================================================================")
                # endregion

        case "6" | "R":
            # region report
            print("1. Report by Class")
            print("2. Report by Subject")
            choose = input("Choose option (1 or 2): ")


            if choose == "1":
                classes = []
                for student in student_list:
                    class_ = student[6]
                    if class_ not in classes:
                        classes.append(class_)
            
                for class_ in classes:
                    scores = []
                    for student in student_list:
                        if student[6] == class_:
                            scores += [int(student[7]), int(student[8]), int(student[9])]
                                       
                    if scores:
                        print("\nClass:", class_, "\nAvg:", sum(scores) / len(scores), "\nMax:", max(scores), "\nMin:", min(scores) )
                    else:
                        print("No data!")

        
            elif choose == "2":
                subjects = ["PHP", "Python", "Java"]
                indxes = [7, 8, 9]

                for i in range(3):
                    scores = []
                    for student in student_list:
                        scores.append(float(student[indxes[i]]))

                    if scores:
                        print("\nSubject:", subjects[i], "\nAvg:", sum(scores) / len(scores), "\nMax:", max(scores), "\nMin:", min(scores) )
                    else:
                        print("No scores available.")
            #endregion
            
        case "7" | "Q":
            break

        case _:
            print("Invalid menu option!!!")
