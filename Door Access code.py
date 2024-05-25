# sally 


import time


class DoorAccessSystem:
    def __init__(self, correct_password, valid_id):
        self.correct_password = correct_password
        self.valid_id = valid_id
        self.entered_password = ""
        self.attempts = 0
        self.max_attempts = 3
        self.locked = False
    
    def press_key(self, key):
        if not self.locked:
            if len(self.entered_password) < 5:
                self.entered_password += key
                print(f"Current Entry: {self.entered_password}")
            if len(self.entered_password) == 5:
                self.verify_password()
        else:
            self.verify_id()
    
    def verify_password(self):
        if self.entered_password == self.correct_password:
            self.unlock_door()
        else:
            self.attempts += 1
            print("Incorrect Password! Beep!")
            self.beep_sound()
            if self.attempts >= self.max_attempts:
                print("Too many incorrect attempts. Enter your ID number to unlock.")
                self.locked = True
                self.verify_id()
            else:
                self.entered_password = ""  # Reset password entry
    
    def verify_id(self):
        user_id = input("Enter your ID number: ")
        if user_id == self.valid_id:
            print("ID verified. Door Unlocked.")
            self.reset_system()
        else:
            print("Invalid ID. System remains locked.")
    
    def unlock_door(self):
        print("Password Correct! Door Unlocked.")
        self.reset_system()
    
    def beep_sound(self):
        duration = 1  # Beep duration in seconds
        print('\a')  # This will play the beep sound
        time.sleep(duration)
    
    def reset_system(self):
        self.entered_password = ""
        self.attempts = 0
        self.locked = False
        print("System Reset. Enter Password:")

def main():
    correct_password = "12345"
    valid_id = "20201102023"
    system = DoorAccessSystem(correct_password, valid_id)
    
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