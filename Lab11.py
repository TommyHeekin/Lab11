import os
sub_dir = "submissions"
import matplotlib.pyplot as plt


if __name__ == "__main__":
    while True:
        print("1. Student grade")
        print("2. Assignment statistics")
        print("3. Assignment graph\n")

        choice = int(input("Enter your selection: "))
        if choice == 1:
            final_grade = 0
            student_name_input = input("What is the student's name: ").strip()
            with open("students.txt") as student_file:
                student_list = student_file.readlines()

            for line in student_list:
                student_name = line[3::].strip()
                student_id = int(line[0:3])

                if student_name == student_name_input:
                    assignment_ids = []
                    assignment_grades = []

                    for submission_file in os.listdir(sub_dir):
                        file_path = os.path.join(sub_dir, submission_file)
                        with open(file_path, "r") as file:
                            content = file.read()

                            if int(content[0:3]) == student_id:
                                assignment_ids.append(int(content.split("|")[1].strip()))
                                assignment_grades.append(int(content.split("|")[2].strip()))

                    grand_total = 0
                    student_total = 0

                    with open("assignments.txt") as assignment_file:
                        assignment_list = assignment_file.readlines()

                    for id in assignment_ids:
                        id = str(id)
                        if id + "\n" in assignment_list:
                            id_index = assignment_list.index(id + "\n")
                            grade = int(assignment_list[id_index + 1].strip())
                            grand_total += grade

                            submission_id_index = assignment_ids.index(int(id))
                            student_total += assignment_grades[submission_id_index] * (grade/100)

                    if grand_total > 0:
                        final_grade = (student_total / grand_total) * 100
                    else:
                        final_grade = 0

                    print(f"{int(final_grade)}%")
                    print()
                    break

                else:
                    print("Student not found\n")
                    break

        elif choice == 2:
            assignment_name = input("What is the assignment name: ").strip()
            with open("assignments.txt") as assignment_file:
                assignment_list = [line.strip() for line in assignment_file.readlines()]

            if assignment_name in assignment_list:
                assignment_index = assignment_list.index(assignment_name)
                assignment_id = assignment_list[assignment_index+1].strip()
                assignment_grades = []
            else:
                print("Assignment not found")
                break

            for submission_file in os.listdir(sub_dir):
                file_path = os.path.join(sub_dir, submission_file)
                with open(file_path, "r") as file:
                    content = file.read()

                    if content.split("|")[1].strip() == assignment_id:
                        grade = int(content.split("|")[2].strip())
                        assignment_grades.append(grade)

            if len(assignment_grades) > 0:
                average_grade = sum(assignment_grades) / len(assignment_grades)
                min_grade = assignment_grades[0]
                max_grade = assignment_grades [0]
                for grade in assignment_grades:
                    if grade < min_grade:
                        min_grade = grade
                    elif grade > max_grade:
                        max_grade = grade
            else:
                average_grade = 0
                min_grade = 0
                max_grade = 0

            print(f"Min: {min_grade}%")
            print(f"Avg: {int(average_grade)}%")
            print(f"Max: {max_grade}%")
            break

        elif choice == 3:
            assignment_name = input("What is the assignment name: ").strip()
            with open("assignments.txt") as assignment_file:
                assignment_list = [line.strip() for line in assignment_file.readlines()]

            if assignment_name in assignment_list:
                assignment_index = assignment_list.index(assignment_name)
                assignment_id = assignment_list[assignment_index + 1].strip()
                assignment_grades = []

                for submission_file in os.listdir(sub_dir):
                    file_path = os.path.join(sub_dir, submission_file)
                    with open(file_path, "r") as file:
                        content = file.read()

                        if content.split("|")[1].strip() == assignment_id:
                            grade = int(content.split("|")[2].strip())
                            assignment_grades.append(grade)

                plt.hist(assignment_grades, bins=6, color="blue", edgecolor="black")
                plt.title(f"{assignment_name} Grade Distribution")
                plt.xlabel("Grade")
                plt.ylabel("Frequency")
                plt.show()

                break

            else:
                print("Assignment not found")
                break

        break
