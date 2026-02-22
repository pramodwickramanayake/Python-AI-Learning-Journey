"""
Project: Student Marks Analysis
Author: Pramod Wickramanayake
Description: A professional script to calculate statistics for student marks.
"""

def calculate_average(marks):
    """
    Calculates the average value from a list of numbers.
    Returns 0 if the list is empty to avoid DivisionByZero error.
    """
    if not marks:
        return 0
    return sum(marks) / len(marks)

def main():
    print("--- Student Marks Analysis System ---")
    
    # Initial data list
    student_marks = [85, 92, 45, 67, 30]

    # Adding new record
    student_marks.append(100)

    # Performing analysis using functions
    total_students = len(student_marks)
    average_mark = calculate_average(student_marks)

    # Professional output formatting
    print(f"Total number of students : {total_students}")
    print(f"Average mark for AI data : {average_mark:.2f}%")

if __name__ == "__main__":
    main() # Industry standard entry point