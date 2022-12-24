print('Game Start')
print('If u really do not know what should u do please enter "Help"')
car_game = ('')
started = False
while True:
    car_game = input('>: ').lower()
    if car_game == 'help':
        print('Start --- to start the car')
        print('Stop --- to stop the car')
        print('Quit --- exit')
    elif car_game == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started...Ready to go')
    elif car_game == 'stop':
        if started:
            print('Car stopped')
        else:
            print('Car is already stopped')
    elif car_game == 'quit':
        break
    else:
        print('Sorry,I do not understand')