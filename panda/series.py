import pandas as pd


def main() -> None:
    marks = pd.Series(
        [85, 90, 78, 92, 88],
        index=["Amit", "Riya", "Sahil", "Neha", "Rahul"],
        name="Marks",
    )

    print("Student marks:")
    print(marks)

    print("\nMarks for Neha:")
    print(marks.loc["Neha"])

    print("\nFirst three students:")
    print(marks.iloc[:3])

    print(f"\nAverage marks: {marks.mean():.1f}")
    print(f"Highest marks: {marks.max()}")
    print(f"Lowest marks: {marks.min()}")


if __name__ == "__main__":
    main()
