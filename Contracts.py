__author__ = 'Ernesto Zarza'


class InvariantException(Exception):
    pass


def contract(requires=None, ensures=None):
    def decorator(function):
        def wrapper(*args):
            if requires is not None and not requires(*args):
                raise Exception("Violation of the contract in the preconditions.")
            result = function(*args)
            if ensures is not None and not ensures(result):
                raise Exception("Violation of the contract in the post-conditions.")
            return result

        return wrapper

    return decorator


@contract(requires=lambda x: x > 0, ensures=lambda result: result > 0)
def some_function(x):
    return 0


class HumanSound:
    @contract(requires=lambda self, freq: freq <= 300)
    @contract(requires=lambda self, freq: freq >= 100)
    def __init__(self, frequency):
        self.frequency = frequency

    @contract(requires=lambda self, sound, soundFrequency: soundFrequency > 20000, ensures=lambda result: result <= 300)
    def play_sound(self, sound_frequency, sound):
        return self.frequency


if __name__ == '__main__':
    # print someFunction(0)

    sound = HumanSound(180)

    # sound._frequency=400
    # sound.playSound(700,"aaaaaaah!")
