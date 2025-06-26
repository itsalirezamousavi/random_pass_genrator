import generator
import strength_checker
import file_handler

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length (8-32): "))
        if length < 8 or length > 32:
            print("Length must be between 8 and 32")
            return
            
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        if not any([use_upper, use_lower, use_digits, use_special]):
            print("You must select at least one character type")
            return
            
        password = generator.generate_password(length, use_upper, use_lower, use_digits, use_special)
        print(f"\nGenerated Password: {password}")
        
        strength = strength_checker.check_strength(password)
        print(f"Password Strength: {strength}")
        
        save = input("\nSave to file? (y/n): ").lower() == 'y'
        if save:
            file_handler.save_password(password)
            print("Password saved to passwords.txt")
            
    except ValueError:
        print("Invalid input. Please enter a number for length.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()