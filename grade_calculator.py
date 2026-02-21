# grade_calculator.py

def calculate_grade(percentage):
    if 90 <= percentage <= 100:
        return "A+ (Outstanding)"
    elif 80 <= percentage < 90:
        return "A (Excellent)"
    elif 70 <= percentage < 80:
        return "B (Good)"
    elif 60 <= percentage < 70:
        return "C (Average)"
    elif 50 <= percentage < 60:
        return "D (Pass)"
    else:
        return "F (Fail)"

def main():
    print("=== GRADE CALCULATOR ===")

    try:
        marks = []

        # Input marks for 5 subjects
        for i in range(1, 6):
            mark = float(input(f"Enter marks for Subject {i} (out of 100): "))
            
            if mark < 0 or mark > 100:
                print("Marks must be between 0 and 100.")
                return
            
            marks.append(mark)

        total = sum(marks)
        percentage = total / 5
        grade = calculate_grade(percentage)

        # Pass condition: All subjects >= 40
        result = "Pass" if all(m >= 40 for m in marks) else "Fail"

        # Output
        print("\n=== RESULT SUMMARY ===")
        for i in range(5):
            print(f"Subject {i+1}: {marks[i]:.2f}")

        print(f"\nTotal Marks: {total:.2f} / 500")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()