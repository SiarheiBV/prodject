def decorator(func):

    def wrapper(*args, **kwargs):
        print("Start decorator...")
        func(*args, **kwargs)
        print("Start decorator...")

    return wrapper


@decorator
def write(name, surname, age):
    print(f"Hello my name is {name}, {surname}, i'm {age}")


write("Siarhei", "Baradauka", 27)
