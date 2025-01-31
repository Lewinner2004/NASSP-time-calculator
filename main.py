from AGS_time_converter import AGS_main, ctrl_z_quit, program_loop
from LGC_clock_sync import LGC_main


# Default error message
ERROR_MESSAGE = "Please enter a valid value!"


# input to select type of calculation, other modules could be added here
def user_input():
    while True:
        print("\nA = Time to decimal minutes conversion\nB = Clock sync time difference calculator\n")
        try:
            choice = input("Enter calculation choice -> ")
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            while True:
                if (choice == "A") or (choice == "a"):
                    return "A"
                elif (choice == "B") or (choice == "b"):
                    return "B"
                else:
                    print(ERROR_MESSAGE)
                    break
                    

# Main function of the program
def main():
    while True:
        choice = user_input()
        print("\n")
        if choice == "A":
            AGS_main()
        elif choice == "B":
            LGC_main()
        

if __name__ == "__main__":
    raise SystemExit(main())
