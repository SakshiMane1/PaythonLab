from pathlib import Path

import pandas as pd


def main() -> None:
    csv_path = Path(__file__).resolve().with_name("student.csv")
    data = {
        "Name": ["Amit", "Riya", "Sahil", "Neha", "Rahul"],
        "Age": [20, 21, 20, 22, 21],
        "Marks": [85, 90, 78, 92, 88],
        "Branch": ["CSE", "CSE", "IT", "CSE", "IT"],
    }

    students = pd.DataFrame(data)
    students.to_csv(csv_path, index=False)
    print(f"Created CSV file: {csv_path.name}")

    loaded_students = pd.read_csv(csv_path)
    print("\nRecords read from the CSV file:")
    print(loaded_students)

    print("\nStudents with at least 90 marks:")
    print(loaded_students.loc[loaded_students["Marks"] >= 90])

    print(f"\nAverage marks: {loaded_students['Marks'].mean():.1f}")


if __name__ == "__main__":
    main()
