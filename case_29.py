sample = input("Enter a sample password to check: ")
errors = []

if len(sample) < 8:
    errors.append("Use at least 8 characters")
if not any(ch.isupper() for ch in sample):
    errors.append("Add at least one uppercase letter")
if not any(ch.islower() for ch in sample):
    errors.append("Add at least one lowercase letter")
if not any(ch.isdigit() for ch in sample):
    errors.append("Add at least one digit")
if not any(not ch.isalnum() for ch in sample):
    errors.append("Add at least one special character")
if "password" in sample.lower():
    errors.append("Do not use the word 'password'")

if errors:
    print("Sample does not satisfy the policy:")
    for error in errors:
        print("-", error)
else:
    print("Sample satisfies all policy rules")
