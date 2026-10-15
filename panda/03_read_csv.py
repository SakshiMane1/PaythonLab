from pathlib import Path

import pandas as pd


def main() -> None:
    csv_path = Path(__file__).resolve().with_name("student.csv")
    students = pd.read_csv(csv_path)

    print("Data from CSV file:")
    print(students)


if __name__ == "__main__":
    main()