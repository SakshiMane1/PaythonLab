from pathlib import Path

import pandas as pd


def main() -> None:
    csv_path = Path(__file__).resolve().with_name("student.csv")
    students = pd.read_csv(csv_path)

    print("Complete data:")
    print(students)

    print("\nNames:")
    print(students["Name"])

    print("\nMarks:")
    print(students["Marks"])

    print("\nFirst record:")
    print(students.iloc[0])

    print(f"\nAverage marks: {students['Marks'].mean():.1f}")
    print(f"Highest marks: {students['Marks'].max()}")
    print(f"Lowest marks: {students['Marks'].min()}")


if __name__ == "__main__":
    main()