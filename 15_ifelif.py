# limit of if elif else
# If statements are used for decision making. 
# It runs the body of code only when the IF statement is true.
# If the IF statement is false, then the ELIF (else if) statement is checked.
# If all IF and ELIF statements are false, the ELSE block is executed.

# ---------------------------------------------------------
# Example 1: Grading System
# This example checks a student's marks and assigns a grade.
# ---------------------------------------------------------
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Explanation:
# The code checks the conditions from top to bottom.
# Since marks is 85, the first condition (marks >= 90) is False.
# The second condition (marks >= 80) is True, so it prints "Grade: B" and stops checking further.


# ---------------------------------------------------------
# Example 2: Traffic Light
# This example simulates a traffic light system.
# ---------------------------------------------------------
light_color = "yellow"

if light_color == "red":
    print("Stop! Do not go.")
elif light_color == "yellow":
    print("Get ready to stop or go depending on safety.")
elif light_color == "green":
    print("Go! It is safe.")
else:
    print("Invalid color signal.")

# Explanation:
# The variable 'light_color' is compared against different strings.
# 'yellow' matches the first elif condition, so that block runs.


# ---------------------------------------------------------
# Example 3: Number Analysis (Positive, Negative, Zero)
# This checks if a number is positive, negative, or zero.
# ---------------------------------------------------------
number = -5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Explanation:
# It checks if the number is greater than 0 first.
# Since -5 is not > 0, it moves to the elif.
# -5 is < 0, so it prints "The number is negative."


# ---------------------------------------------------------
# Example 4: Day of the Week
# Converts a number (1-7) into the name of the day.
# ---------------------------------------------------------
day_num = 3

if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid day number")

# Explanation:
# It checks the value of day_num against each number from 1 to 7.
# Since day_num is 3, it matches the third condition and prints "Wednesday".


# ---------------------------------------------------------
# Example 5: Movie Ticket Pricing
# Determines ticket price based on age group.
# ---------------------------------------------------------
age = 25

if age < 5:
    print("Ticket Price: Free")
elif age < 13:
    print("Ticket Price: $5 (Child)")
elif age < 18:
    print("Ticket Price: $10 (Teen)")
elif age < 60:
    print("Ticket Price: $15 (Adult)")
else:
    print("Ticket Price: $12 (Senior)")

# Explanation:
# This checks ranges of age.
# Since age is 25:
# Is 25 < 5? No.
# Is 25 < 13? No.
# Is 25 < 18? No.
# Is 25 < 60? Yes.
# It prints "Ticket Price: $15 (Adult)".
