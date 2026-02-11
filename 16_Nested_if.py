# Nested If Statements
# A nested if statement is an if statement inside another if statement.
# The inner if statement is executed only if the outer if statement is true.

# ---------------------------------------------------------
# Example 1: Number Analysis (Positive & Even/Odd)
# Checks if a number is positive, and if so, whether it's even or odd.
# ---------------------------------------------------------
num = 12

if num > 0:
    print("Number is positive.")
    if num % 2 == 0:
        print("Number is even.")
    else:
        print("Number is odd.")
else:
    print("Number is not positive.")

# Explanation:
# First, it checks if `num` is greater than 0.
# If true, it enters the block and checks if `num` is divisible by 2.


# ---------------------------------------------------------
# Example 2: Loan Eligibility
# Checks age first, then income status for loan approval.
# ---------------------------------------------------------
age = 25
income = 40000

if age >= 18:
    if income > 30000:
        print("Loan Approved.")
    else:
        print("Loan Rejected: Income too low.")
else:
    print("Loan Rejected: Underage.")

# Explanation:
# The outer `if` checks if the person is an adult (18+).
# If they are, the inner `if` checks if their income is sufficient.
# If the outer `if` is false, it skips the income check entirely.


# ---------------------------------------------------------
# Example 3: Simple Login System
# Verifies username first, then password.
# ---------------------------------------------------------
username = "admin"
password = "password123"

input_user = "admin"
input_pass = "password123"

if input_user == username:
    if input_pass == password:
        print("Login Successful!")
    else:
        print("Incorrect Password.")
else:
    print("Incorrect Username.")

# Explanation:
# It first checks if the username matches. 
# Only if the username is correct does it proceed to check the password.
# This mimics real-world logic where you validate identity before credentials.


# ---------------------------------------------------------
# Example 4: Student Exam & Attendance
# Checks attendance first. If attendance is sufficient, checks marks.
# ---------------------------------------------------------
attendance = 85  # Percentage
marks = 70

if attendance >= 75:
    if marks >= 50:
        print("Allowed to sit in exam and Passed.")
    else:
        print("Allowed to sit in exam but Failed.")
else:
    print("Not allowed to sit in exam due to low attendance.")

# Explanation:
# The student must have 75% or more attendance to even be considered (outer if).
# If they meet that condition, their marks determine if they pass or fail (inner if).


# ---------------------------------------------------------
# Example 5: Shopping Discount Check
# Checks for membership, then purchase amount for extra discount.
# ---------------------------------------------------------
is_member = True
total_amount = 600

if is_member:
    if total_amount > 500:
        print("Eligible for 20% discount.")
    else:
        print("Eligible for 10% discount.")
else:
    print("No discount applicable.")

# Explanation:
# First, it checks if the customer is a member.
# If they are a member, it checks if their cart total qualifies for a higher tier discount.
# Non-members get no discount immediately.
