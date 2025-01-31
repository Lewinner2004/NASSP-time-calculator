from AGS_time_converter import ctrl_z_quit, program_loop
from numpy import abs


# Default error message
ERROR_MESSAGE = "Please enter a valid value!"


# Function that calculates the difference in the times from to list and inputs
# the result in another list. 
def diff_calculation(cmc, lgc):
    diff = ((cmc[0]*3600)+(cmc[1]*60)+cmc[2]) - ((lgc[0]*3600)+(lgc[1]*60)+lgc[2])
    negative_value = False
    time = []
    if diff < 0:
        negative_value = True
    diff = abs(diff)
    time.append(diff // 3600)
    if diff != 0:
        diff %= 3600
    time.append(diff // 60)
    if diff != 0:
        diff %= 60
    time.append(diff)
    if negative_value == True:
        for i in range(3):
            time[i] *= -1
    for i in range(2):
        time[i] = int(time[i])
    return time


# Main user inputs of the programs with error handling 
def input_loops():
    cmc = []
    lgc = []
    while True:
        try:
            cmc.append(int(input("  Enter CMC hours -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            cmc.append(int(input("Enter CMC minutes -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            cmc.append(float(input("Enter CMC seconds -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            lgc.append(int(input("  Enter LGC hours -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            lgc.append(int(input("Enter LGC minutes -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    while True:
        try:
            lgc.append(float(input("Enter LGC seconds -> ")))
        except ValueError:
            print(ERROR_MESSAGE)
        except EOFError:
            ctrl_z_quit()
        else:
            break
    return cmc, lgc


# Time output in an easy to read format
def output(time):
    print(f"\nTime difference:\n{time[0]} hour(s)\n{time[1]} minute(s)\n{time[2]} second(s)\n")
    return None
  
        
# Main function of the program
def LGC_main():
    while True:
        cmc, lgc = input_loops()
        time = diff_calculation(cmc, lgc)
        output(time)
        quit_ = program_loop()
        if quit_ == True:
            break
        elif quit_ == False:
            quit()


if __name__ == "__main__":
    raise SystemExit(LGC_main())
