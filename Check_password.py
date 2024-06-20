def check_password_strength(password):
    # Define criteria weights
    length_weight = 2
    uppercase_weight = 1
    lowercase_weight = 1
    digit_weight = 1
    special_char_weight = 2

    # Initialize scores
    length_score = 0
    uppercase_score = 0
    lowercase_score = 0
    digit_score = 0
    special_char_score = 0

    # Check length
    if len(password) >= 8:
        length_score = length_weight

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        uppercase_score = uppercase_weight

    # Check for lowercase letters
    if any(char.islower() for char in password):
        lowercase_score = lowercase_weight

    # Check for digits
    if any(char.isdigit() for char in password):
        digit_score = digit_weight

    # Check for special characters
    special_characters = "!@#$%^&*()_+{}[];:<>,.?/~"
    if any(char in special_characters for char in password):
        special_char_score = special_char_weight

    # Calculate total score
    total_score = (length_score + uppercase_score + lowercase_score +
                   digit_score + special_char_score)

    # Determine strength based on total score and length
    if total_score >= 10:
        strength = "Strong"
    elif total_score >= 7:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = f"Your password is {strength}. Score: {total_score}/10"
    return feedback

# Example usage
if __name__== "__main__":
    while True:
        password = input("Enter your password (must be at least 8 characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters long. Please try again.")
        else:
            break
    
    strength_feedback = check_password_strength(password)
    print(strength_feedback)
