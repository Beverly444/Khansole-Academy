import random


def main(): # Main function to run the program
    print("Khansole Academy")
    num_1 = random.randint(10, 99)
    num_2 = random.randint(10, 99)
    answer = num_1 + num_2
    
    print(f"What is {num_1} + {num_2}?")

    user_answer = int(input("Your answer: ")) # Ensure input is an integer

    is_user_correct = user_answer == answer # Check if user's answer matches the expected answer

    if is_user_correct: # If the user's answer is correct
        print("Correct!")

    else: # If the user's answer is incorrect
        print("Incorrect.")
        print(f"The expected answer is {answer}")


if __name__ == '__main__': # This ensures the main function runs when the script is executed directly
    main()