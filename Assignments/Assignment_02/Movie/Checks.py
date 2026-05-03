class UnderageError(Exception):
    """Custom error for when a user isn't old enough yet."""
    pass

def register_user():
    print("---  MovieTime: Create Your Account  ---")
    
    try:
        user_name = input("What's your name? ").strip()
        raw_age = input(f"Hi {user_name}, how old are you? ")

        # Validate that we actually got a number
        if not raw_age.isnumeric():
            raise ValueError("That doesn't look like a number. Please enter your age in digits.")

        age = int(raw_age)

        # Check age restriction
        if age < 18:
            raise UnderageError("You need to be at least 18 to view our R-rated collection.")

        # If everything is fine
        print(f"Awesome! Welcome aboard, {user_name}. Grab your popcorn! ")

    except ValueError as err:
        print(f"Oops! {err}")

    except UnderageError as err:
        print(f"Access Restricted: {err}")

    else:
        print("Your account is all set and ready to go.")

    finally:
        print("Thank you for using MovieTime! Have a great day!")

# Start the process
if __name__ == "__main__":
    register_user()
