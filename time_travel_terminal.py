import os

def main():
    print("Welcome to Time-Traveling Terminal (T3)")
    while True:
        command = input("T3> ").strip()  # Trim extra spaces
        
        if command.lower() == "exit":
            print("Exiting Time-Traveling Terminal...")
            break
        elif command.startswith("travel "):  # Check if command starts with "travel"
            parts = command.split()
            if len(parts) == 2 and parts[1].isdigit():  # Ensure correct format
                travel_to_year(parts[1])
            else:
                print("Usage: travel <year> (Example: travel 1995)")
        else:
            os.system(command)  # Execute standard system commands

def travel_to_year(year):
    print(f"🕒 Simulating system time in {year}...")
    
    # Requires sudo access to change system time
    if os.geteuid() == 0:  # Check if running as root
        os.system(f"date -s '{year}-01-01 12:00:00'")
    else:
        print("⚠️ You need sudo permissions to change system time.")
        print("Try running: sudo python3 time_travel_terminal.py")

if __name__ == "__main__":
    main()

