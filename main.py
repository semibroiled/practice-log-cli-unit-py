# Import Packages
from functions import fibonacci


# Make file callable and not importable

if __name__ == "__main__":
    try:
        end: int = int(input("Input number:"))
        series = fibonacci(end)
        print(
            f""" Your list of fibonacci numbers upto 
          {end} are:\n {series}"""
        )
    except ValueError as e:
        print(e)
    finally:
        pass
