
# Default error message
ERROR_MESSAGE = "Please enter a valid value!"


# Calculation of the AGS time from burn/mission time
def time_converter(time):
    decimal_minutes = ((time[1] - time[0]) * 60) + time[2] + (time[3] / 60)
    return decimal_minutes


# Logic that replaces out of bounds values for an error message to minimize mistakes
def output_logic(decimal_minutes):
    AGS_error = "AGS time out of bounds, check values."
    if decimal_minutes < 0:
        return AGS_error
    elif decimal_minutes > 9999.9:
        return AGS_error
    else:
        return f"{decimal_minutes:.1f} AGS Time"
 
        
# Main values input loops with complete error handling   
def input_loops():
    time = []
    while True:
        try:
            time.append(int(input("Enter time bias (h) -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            time.append(int(input("Enter hours         -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            time.append(int(input("Enter minutes       -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            time.append(float(input("Enter seconds       -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    return time


# Loop that makes it possible to perform another calculation
def program_loop():
    while True:
        try:
            user_choice = input("Do you wish to perform another calculation? (Y=Yes, N=No) -> ")
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            while True:
                if (user_choice == "Y") or (user_choice == "y"):
                    print("\n")
                    return True
                elif (user_choice == "N") or (user_choice == "n"):
                    quit()
                else:
                    print(ERROR_MESSAGE)
                    return False
                    


# Function that adds the possibility to exit the program at any time by entering Ctrl-Z in inputs
def ctrl_z_quit():
    print("\n")
    while True:
        try:
            user_choice = input("Do you wish to quit? (Y=Yes, N=No) -> ")
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            print(ERROR_MESSAGE)
        else:
            while True:
                if (user_choice == "Y") or (user_choice == "y"):
                    return True
                elif (user_choice == "N") or (user_choice == "n"):
                    return None
                else:
                    print(ERROR_MESSAGE) 


# Main function of the program 
def AGS_main():
    while True:
        time = input_loops()   
        decimal_minutes = time_converter(time)
        print("\n", f"{output_logic(decimal_minutes)}","\n")
        quit_ = program_loop()
        if quit_ == True:
            break
        elif quit_ == False:
            quit()

 
if __name__ == "__main__":
    raise SystemExit(AGS_main())
