# need reafctoring, to talk about on thursday
from time import sleep

# waiting for router/switch to boot
def checking_booting(user_choice):
    correct_flag = True
    if user_choice == 1:
        sleep(1)
    elif user_choice == 2:
        # 4 minutes is enough time to boot switch/router
        print("It will take about 4 minutes...")
        sleep(240)
    else:
        print("You have provided incorrect input...")
        correct_flag = False

    return correct_flag