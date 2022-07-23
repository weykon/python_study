def func():
    print("My first Coroutine")
    while True:
        var = (yield)
        print(var)


coroutine = func()
next(coroutine)


# my code
def wait_my_game_finished():
    next(coroutine)
    print("ok!")

def gaming():
    print("biubiubiu~")

coroutine = gaming()


wait_my_game_finished()


# fu****