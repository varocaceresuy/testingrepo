# This file es LF enforced in .gitattributes

# Some multibyte chars first 😂 汉字.

class Example:

    def example_method(self, example_param: str):
        """
        Docstring summary 😂 汉字
        :param example_param: Param description
        :return: return description
        """

        # Inline comment with multibyte chars 😂 汉字.
        return None

    class InnerClass:
        def inner_class_method(self):
            pass

def example_function():
    def inner_function():
        pass

    inner_function()

    return 1

def function_args(a:str, b:int=1, *args, **kwargs):
    pass


def ends_with_else():
    if True:
        pass
    else:
        pass


def empty_function_pass():
    pass


def empty_function_ellipsis():
    ...


def function_with_body(a: int, b: int):
    """ This sums two numbers """
    return a + b


def function_with_body2():
    print("message")

