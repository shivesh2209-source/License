import random
from datetime import datetime, timedelta
import string

while True:
    try:
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        sex = input("Enter your Gender (male/female): ").strip().lower()

        # Validate gender input
        if sex not in ["male", "female"]:
            print("Invalid gender! Please enter 'male' or 'female'.")
            continue  # Restart loop

        # Block females completely
        if sex == "female":
            print("Sorry, females are not allowed to apply for a license.")
            break

        # Block males under 18
        if age < 18:
            print("You are under 18. You are not authorized to drive a car.")
            break

        # Schedule test for eligible males
        days_ahead = random.randint(1, 30)
        test_date = datetime.now() + timedelta(days=days_ahead)
        print("Your driving test has been scheduled for", test_date.strftime('%Y-%m-%d'))

        # Traffic question
        print("\nWhat does a red traffic light indicate?\nOptions:\n A) Slow down and proceed with caution\n B) Stop completely\n C) Speed up to clear the intersection\n D) Turn left only")
        answer1 = input("Enter your Answer (A/B/C/D or full answer): ").strip().lower()

        # Check answer
        if answer1 in ("b", "stop completely", "stop"):
            random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
            print("Congrats! अब हॉर्न सिर्फ ज़रूरत पर बजाना, DJ पार्टी मत बनाना।")
            print("Your License Number is:", random_string)
            break
        else:
            print("You failed the test. No license for you.")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")