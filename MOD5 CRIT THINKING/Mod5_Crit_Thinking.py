# Armando Gomez
# Module 5 Critical Thinking

# Part 1: Average Rainfall Collector
def calculate_average_rainfall():
    years = int(input("Enter the number of rainy years: "))

    total_months = 0
    total_rainfall = 0.0
    wet_months = 0  # Count months with rainfall > 5 inches
    dry_months = []  # Track months with rainfall < 1 inch

    for year in range(1, years + 1):
        print(f"Year {year}:")
        for month in range(1, 13):
            while True:  # Input validation loop
                try:
                    rainfall = float(input(f"  Enter rainfall in inches for month {month}: "))
                    if rainfall < 0:
                        print("Rainfall cannot be negative numbers. Please enter a valid number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            total_rainfall += rainfall
            total_months += 1

            # Boolean conditions for wet and dry months here
            if rainfall > 5:
                wet_months += 1  # Count wet months
            if rainfall < 1:
                dry_months.append((year, month))  # Track year and month of dry months

    # now we calculate averages
    average_rainfall = total_rainfall / total_months if total_months > 0 else 0

    # Output results
    print("\nSummary of Rainfall Data:")
    print(f"Total number of months: {total_months}")
    print(f"Total rainfall: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Number of wet months (> 5 inches): {wet_months}")
    if dry_months:
        print("Dry months (< 1 inch of rainfall):")
        for year, month in dry_months:
            print(f"  - Year {year}, Month {month}")
    else:
        print("No dry months recorded.")
    print("-" * 40)



# Part 2: CSU Global Book Club Points Program

def book_club_points():
    print("Welcome Students! CSU Global Book Club Points Program!")
    books_purchased = int(input("Enter the number of books you purchased this month: "))

    if books_purchased == 0:
        points = 0
    elif books_purchased == 1:
        points = 2.5
    elif books_purchased == 2:
        points = 5
    elif books_purchased == 3:
        points = 7.5
    elif books_purchased == 4:
        points = 15
    elif books_purchased == 5:
        points = 22
    elif books_purchased == 6:
        points = 30
    elif books_purchased >= 7:
        points = 45
    elif books_purchased >= 8:
        points = 60
    elif books_purchased >= 9:
        points = 75
    elif books_purchased >= 10:
        points = 90
    else:
        points = 0  # Default points all students have (unexpected input)

    print(f"Points earned: {points}")
    print("-" * 40)


# Main program
def main():
    print("Part 1: Average Rainfall Collector")
    calculate_average_rainfall()

    print("\nPart 2: Book Club Points Program")
    book_club_points()


if __name__ == "__main__":
    main()
