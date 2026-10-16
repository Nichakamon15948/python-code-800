"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age_str = input("Enter your age: ")
phone = input("Enter your phone number: ")

# Validate Name: contains only alphabetic characters and spaces
is_name_valid = name.replace(" ", "").isalpha() and len(name.strip()) > 0

# Validate Age: convert to integer and check between 18-65
is_age_valid = False
age = None
if age_str.isdigit():
    age = int(age_str)
    if 18 <= age <= 65:
        is_age_valid = True

# Validate Phone: contains exactly 10 digits
is_phone_valid = len(phone) == 10 and phone.isdigit()

# Validation Results
print("\nValidation Results:")
if is_name_valid:
    print("Name: %s" % "Valid (contains only letters and spaces)")
else:
    print("Name: %s" % "Invalid (must contain only letters and spaces)")

if is_age_valid:
    print("Age: %s" % ("Valid (%d years old)" % age))
else:
    print("Age: %s" % "Invalid (must be between 18-65)")

if is_phone_valid:
    print("Phone: %s" % "Valid (10-digit number)")
else:
    print("Phone: %s" % "Invalid (must be exactly 10 digits)")

# Formatted Information
if is_name_valid and is_age_valid and is_phone_valid:
    if 18 <= age <= 30:
        age_group = "Young Adult (18-30)"
    elif 31 <= age <= 50:
        age_group = "Adult (31-50)"
    else:
        age_group = "Senior (51-65)"

    print("\nFormatted Information:")
    print("Name: {}".format(name.upper()))
    print("Age Group: {}".format(age_group))
    print("Phone: +91-{}".format(phone))