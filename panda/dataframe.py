import pandas as pd


def main() -> None:
    data = {
        "Name": ["Amit", "Riya", "Sahil", "Neha", "Rahul"],
        "Age": [20, 21, 20, 22, 21],
        "Marks": [85, 90, 78, 92, 88],
        "Branch": ["CSE", "CSE", "IT", "CSE", "IT"],
    }
    students = pd.DataFrame(data)

    print("Student records:")
    print(students)

    print("\nFirst two records:")
    print(students.head(2))

    print("\nNames and marks:")
    print(students[["Name", "Marks"]])

    print("\nStudent with the highest marks:")
    print(students.loc[students["Marks"].idxmax()])

    print(f"\nAverage marks: {students['Marks'].mean():.1f}")


if __name__ == "__main__":
    main()