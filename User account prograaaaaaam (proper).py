import csv
import os

# Function to read data from the CSV file, or create it if it doesn't exist
def get_data(filename):
    if not os.path.exists(filename):
        # If the file doesn't exist, create it with headers
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['userID', 'Password'])  # Writing the header row
        return [['userID', 'Password']]  # Return list with only the header
    else:
        # If file exists, read and return the data
        data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

# Function to check if the user ID exists
def create_userID(newID, data):
    for row in data:
        if row[0] == newID:
            return False
    return True

# Function to validate a new password
def create_password(newpassword):
    if len(newpassword) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in newpassword):
        print("Password must include at least one uppercase letter.")
        return False
    if not any(char.islower() for char in newpassword):
        print("Password must include at least one lowercase letter.")
        return False
    if not any(char.isdigit() for char in newpassword):
        print("Password must include at least one number.")
        return False
    if not any(char in "!£$€%&*#" for char in newpassword):
        print("Password must include at least one special character (!, £, $, €, %, &, *, #).")
        return False
    return True

# Function to find the user ID
def find_userID(userID, data):
    for row in data:
        if row[0] == userID:
            return row
    return None

# Function to change the password for an existing user ID
def change_password(userID, newPassword, data):
    for row in data:
        if row[0] == userID:
            row[1] = newPassword

# Function to display all user IDs
def display_all_userID(data):
    print("User IDs:")
    for row in data[1:]:  #skip the header row when displaying
        print(row[0])

#Main function to run the program
def main():
    filename = "Passwords.csv"
    data = get_data(filename)
    
    while True:
        print("\nMenu:")
        print("1) Create a new User ID")
        print("2) Change a password")
        print("3) Display all user IDs")
        print("4) Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            #Create a new user ID
            while True:
                newID = input("Enter new User ID: ")
                if create_userID(newID, data):
                    break
                else:
                    print("User ID already exists, try another.")
            
            while True:
                newPassword = input("Enter a new password: ")
                if create_password(newPassword):
                    break
            
            #Append new user and password to the file
            with open(filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([newID, newPassword])
            print("New user created successfully!")
            data.append([newID, newPassword])
        
        elif choice == '2':
            #Change password for an existing user
            userID = input("Enter User ID to change password: ")
            user = find_userID(userID, data)
            if user:
                while True:
                    newPassword = input("Enter a new password: ")
                    if create_password(newPassword):
                        break
                change_password(userID, newPassword, data)
                
                #Rewrite the entire file with updated data
                with open(filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(data)
                print("Password updated successfully!")
            else:
                print("User ID not found.")
        
        elif choice == '3':
            #Display all user IDs
            display_all_userID(data)
        
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        
        else:
            print("Invalid selection, please try again.")

#Run the program
if __name__ == "__main__":
    main()
