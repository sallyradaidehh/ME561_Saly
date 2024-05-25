# sally 


import time

class DoorAccessSystem:
    def __init__(self, correct_password):
        self.correct_password = correct_password
        self.entered_password = ""
        self.attempts = 0
        self.max_attempts = 3
    
    
    def press_key(self, key):
        if len(self.entered_password) < 5:
            self.entered_password += key
            print(f"Current Entry: {self.entered_password}")
        if len(self.entered_password) == 5:
            self.verify_password()
    
    def verify_password(self):
        if self.entered_password == self.correct_password:
            self.unlock_door()
        else:
            self.wrong_password()
    
    def unlock_door(self):
        print("Password Correct! Door Unlocked.")
        self.reset_system()
    
    def wrong_password(self):
        self.attempts += 1
        print("Incorrect Password! Beep!")
        self.beep_sound()
        if self.attempts >= self.max_attempts:
            print("Too many incorrect attempts. System locked.")
            exit()  # Exit the program
        else:
            self.reset_system()
    
    def beep_sound(self):
        duration = 1  # Beep duration in seconds
        print('\a')  # This will play the beep sound
        time.sleep(duration)
    
    def reset_system(self):
        self.entered_password = ""
        print("System Reset. Enter Password:")

def main():
    correct_password = "12345"
    system = DoorAccessSystem(correct_password)
    
    print("Welcome to GJU Door Access System")
    print("Enter 5-digit password using the keypad:")
    
    while True:
        key = input("Press a key (0-9): ")
        if key.isdigit() and len(key) == 1:
            system.press_key(key)
        else:
            print("Invalid key! Please press a single digit (0-9).")

if __name__ == "__main__":
    main()

