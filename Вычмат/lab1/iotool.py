from random import randint
def read_data_console():
    n = get_n()
    data = []
    for i in range(n):
        while True:
            try:
                row = list(map(float, input(f"Enter the coefficients of equation {i + 1}: ").split()))
                if len(row) != n + 1:
                    raise ValueError()
                data.append(row)
                break
            except ValueError:
                print(f"Invalid input. Please enter {n + 1} numbers separated by spaces.")
    return data

def read_data_file():
    while True:
        try:
            filename = input("Enter the name of the file: ")
            with open(filename, "r") as file:
                n = int(file.readline())
                if n < 1 or n>20:
                    raise ValueError()
                data = []
                for i in range(n):
                    row = list(map(float, file.readline().split()))
                    if len(row) != n + 1:
                        raise ValueError()
                    data.append(row)
                return data
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except ValueError:
            print(f"Invalid data in file {filename}.")
        except Exception as e:
            print(f"An error occurred: {e}")

def generate_data():
    n = get_n()
    data = []
    for i in range(n):
        row = [randint(-2300, 5400)/100 for _ in range(n + 1)]
        data.append(row)
    return data

def get_n():
    while True:
        try:
            n = int(input("Enter the number of equations: "))
            if n < 1 or n>20:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer <= 20.")
    return n