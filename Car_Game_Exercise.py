started = False
quit = 'quit'
command=""
help = 'help'

while True:                                                                  # instead of (command != quit:)
    command = input('Cmd:').lower()
    if command == "start":
        if started:
            print('Car is Already started')
        else:
            started = True
            print('Car is Started')
    elif command == "stop":
        if not started:
            print('Car is Already stoped')
        else:
            started = False
            print('Car is Stoped')
    elif command == help:
        print('start : To Start the Car \nstop : To Stop the car\nquit : To Quit the game')
    elif command == quit:
        break
    else:
        print("I don't Understand")

