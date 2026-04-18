# Help Desk Expert System

def help_desk():
    print("\n===== HELP DESK EXPERT SYSTEM =====")
    print("Select your issue:")
    print("1. Internet not working")
    print("2. Slow computer")
    print("3. Unable to login")
    print("4. Software not opening")
    print("5. Printer not working")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        internet_issue()
    elif choice == '2':
        slow_computer()
    elif choice == '3':
        login_issue()
    elif choice == '4':
        software_issue()
    elif choice == '5':
        printer_issue()
    elif choice == '6':
        print("Exiting Help Desk. Goodbye!")
        exit()
    else:
        print("Invalid choice. Try again.")

    # Ask user if they want to continue
    cont = input("\nDo you want to check another issue? (yes/no): ")
    if cont.lower() == 'yes':
        help_desk()
    else:
        print("Thank you for using Help Desk Expert System!")

# ----------- RULE-BASED FUNCTIONS -----------

def internet_issue():
    print("\n--- Internet Troubleshooting ---")
    ans = input("Are all cables properly connected? (yes/no): ")
    
    if ans.lower() == 'no':
        print("👉 Solution: Connect all cables properly.")
    else:
        ans = input("Is the router ON? (yes/no): ")
        
        if ans.lower() == 'no':
            print("👉 Solution: Turn ON the router.")
        else:
            ans = input("Are you getting any signal? (yes/no): ")
            
            if ans.lower() == 'no':
                print("👉 Solution: Restart the router.")
            else:
                print("👉 Solution: Contact Internet Service Provider.")

def slow_computer():
    print("\n--- Slow Computer Troubleshooting ---")
    ans = input("Do you have many programs open? (yes/no): ")
    
    if ans.lower() == 'yes':
        print("👉 Solution: Close unnecessary programs.")
    else:
        ans = input("Is your storage almost full? (yes/no): ")
        
        if ans.lower() == 'yes':
            print("👉 Solution: Delete unwanted files.")
        else:
            print("👉 Solution: Run antivirus scan or restart computer.")

def login_issue():
    print("\n--- Login Troubleshooting ---")
    ans = input("Are you entering correct username/password? (yes/no): ")
    
    if ans.lower() == 'no':
        print("👉 Solution: Re-enter correct credentials.")
    else:
        ans = input("Is Caps Lock ON? (yes/no): ")
        
        if ans.lower() == 'yes':
            print("👉 Solution: Turn OFF Caps Lock and try again.")
        else:
            print("👉 Solution: Reset your password.")

def software_issue():
    print("\n--- Software Troubleshooting ---")
    ans = input("Did you install the software properly? (yes/no): ")
    
    if ans.lower() == 'no':
        print("👉 Solution: Reinstall the software.")
    else:
        ans = input("Is there any error message? (yes/no): ")
        
        if ans.lower() == 'yes':
            print("👉 Solution: Check error online or update software.")
        else:
            print("👉 Solution: Restart the system and try again.")

def printer_issue():
    print("\n--- Printer Troubleshooting ---")
    ans = input("Is the printer ON? (yes/no): ")
    
    if ans.lower() == 'no':
        print("👉 Solution: Turn ON the printer.")
    else:
        ans = input("Is paper loaded? (yes/no): ")
        
        if ans.lower() == 'no':
            print("👉 Solution: Load paper in the printer.")
        else:
            ans = input("Is printer connected to computer? (yes/no): ")
            
            if ans.lower() == 'no':
                print("👉 Solution: Connect printer properly.")
            else:
                print("👉 Solution: Reinstall printer drivers.")

# ----------- START PROGRAM -----------

help_desk()
