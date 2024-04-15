from matrix import Matrix
from iotool import read_data_console, read_data_file, generate_data
import os

def read_data():
    while True:
        try:
            choice = int(input("Enter 1 to read from console, 2 to read from file, 3 to generate: "))
            if choice not in [1, 2, 3]:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input. Please enter 1, 2 or 3.")
    if choice == 1:
        return read_data_console()
    elif choice == 2:
        return read_data_file()
    else:
        return generate_data()
        
def manage(data):        
    try:
        matrix = Matrix(data)
        print(matrix)
        matrix.triangular_matrix()
        print("\nDeterminant: ", matrix.determinant())
        try:
            st = matrix.print_triangular()
            print(st[:len(st)//2], end="")
            print(st[len(st)//2:])
            solution = matrix.solve_system_gauss()
            print("\nSolution:")
            for i, s in enumerate(solution):
                print(f"x{i+1} = {s}")
        except ValueError as e:
            print(f"We can't solve this system of equations. The determinant is {matrix.determinant()}.")
        except TypeError as e:
            print(f"We can't solve this system of equations. The determinant is {matrix.determinant()}.")
        print()
        try:
            residual = Matrix.residual_vector(data, solution)
            print("Residual vector:")
            for ї,r in enumerate(residual):
                print(f"r{ї+1} = {r}")
        except ValueError as e:
            print(e)
        except UnboundLocalError as e:
            print("We can't calculate the residual vector.")
    except ValueError as e:
        print(e)

def run_again():
    while True:
        user_input = input("Do you want to run the program again? (yes/no): ").lower()
        if user_input == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif user_input == 'no':
            print("Exiting the program. Goodbye!")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    data = read_data()
    manage(data)
    run_again()

if __name__ == "__main__":
    main()

