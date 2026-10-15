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
    print(f"CSV file created successfully: {csv_path.name}")


if __name__ == "__main__":
    main()