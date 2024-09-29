class Printing:
    def __init__(self, parameters, result):
        assert len(parameters) == min(len(row) for row in result) and len(parameters) == max(len(row) for row in result), "Wrong parameters or result"
        self.parameters = parameters
        self.result = result
    
    def print_result(self):
        print("{:^3} |".format("k"), end="")
        for key in self.parameters:
            print("{:^9} |".format(key), end="")
        print()
        
        print("-" * (5 + 10 * len(self.parameters)))
        
        k = 1
        for row in self.result:
            print("{:^3} |".format(k), end="")
            k += 1
            for n in row:
                if isinstance(n, bool):
                    print("{:^9} |".format(str(n)), end="")
                else:
                    print("{:^9.4f} |".format(n), end="")
            print()