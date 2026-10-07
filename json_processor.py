import json

INPUT_FILE = "students.json"
OUTPUT_FILE = "results.json"


def load_data(filename):
    """Load JSON data from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Validate expected key
        if "students" not in data:
            print("Error: 'students' key not found in JSON file.")
            return None

        return data["students"]

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


def search_students(students, name):
    """Search students by name."""
    results = []

    for student in students:
        if name.lower() in student.get("name", "").lower():
            results.append(student)

    return results


def filter_students(students, minimum_marks):
    """Filter students based on minimum marks."""
    return [
        student
        for student in students
        if student.get("marks", 0) >= minimum_marks
    ]


def create_summary(students):
    """Create summary statistics."""

    if not students:
        return {
            "total_students": 0,
            "average_marks": 0,
            "highest_marks": 0,
            "lowest_marks": 0
        }

    marks = [student.get("marks", 0) for student in students]

    return {
        "total_students": len(students),
        "average_marks": sum(marks) / len(marks),
        "highest_marks": max(marks),
        "lowest_marks": min(marks)
    }


def save_results(filename, search_results, filtered_results, summary):
    """Save processed results to a JSON file."""

    output = {
        "search_results": search_results,
        "filtered_results": filtered_results,
        "summary": summary
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4)


# Main program
if __name__ == "__main__":

    students = load_data(INPUT_FILE)

    if students is not None:

        # Search students whose name contains "a"
        search_results = search_students(students, "a")

        # Filter students with marks >= 75
        filtered_results = filter_students(students, 75)

        # Create summary
        summary = create_summary(students)

        # Save results
        save_results(
            OUTPUT_FILE,
            search_results,
            filtered_results,
            summary
        )

        print("JSON processing completed successfully.")
        print(f"Results saved to: {OUTPUT_FILE}")

        print("\n===== SUMMARY =====")
print(f"Total students: {summary['total_students']}")
print(f"Average marks: {summary['average_marks']:.2f}")
print(f"Highest marks: {summary['highest_marks']}")
print(f"Lowest marks: {summary['lowest_marks']}")