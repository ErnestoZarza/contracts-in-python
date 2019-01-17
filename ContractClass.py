__author__ = 'Ernesto Zarza'


def contract(function):
    class Wrapper:
        # "This class will wrap around the function"

        def __init__(self):
            self.function = function
            self.__post_condition = []
            self.__post_exception = []
            self.args = []
            self.kwargs = {}

        def put_post(self, function, exception):
            # "Register a post-condition function"
            self.__post_condition.append(function)
            self.__post_exception.append(exception)

        def run_pre(self, function, exception):
            # "Run a pre-condition function"
            if not function():
                raise Exception(exception)

        def __call__(self, *args, **kwargs):
            # "Emulate a call to the function."
            self.args = args
            self.kwargs = kwargs
            # old = map(lambda x : x.Clone() ,args)
            result = self.function(*args, **kwargs)

            while self.__post_condition:
                if not self.__post_condition.pop()(result):
                    raise Exception(self.__post_exception.pop())
            return result

    return Wrapper()


def requires(pfun, function, exception="Requires fails."):
    pfun.run_pre(function, exception)


def ensures(pfun, function, exception="Ensure fails."):
    pfun.put_post(function, exception)
