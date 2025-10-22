"""A simple Python program to display personal information."""

def display_personal_info() -> None:
    """
    Display personal details such as name, age, qualification,
    college name, address, and year of passing.
    """
    name: str = "M.A Zia"
    age: int = 21
    qualification: str = "Bachelor of Computer Applications (BCA)"
    college_name: str = "S.S TeGNOOR Degree College of Computer Science"
    address: str = "kalaburgi,Karnataka,585104"
    year_of_passing: int = 2025

    print("---- Personal Information ----")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Qualification: {qualification}")
    print(f"College Name: {college_name}")
    print(f"Address: {address}")
    print(f"Year of Passing: {year_of_passing}")


def main() -> None:
    """Main function to call the display function."""
    display_personal_info()


if __name__ == "__main__":
    main()
