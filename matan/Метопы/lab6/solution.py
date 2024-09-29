from random import randint, random, shuffle


class solution:
    def __init__(self, matrix, p):
        self.matrix = matrix
        self.n = len(matrix)
        self.p = p  # probability of mutation

    def get_len(self, x, y):
        return self.matrix[int(x) - 1][int(y) - 1]

    def aim_function(self, s):
        result = 0
        for i in range(-1, self.n - 1):
            result += self.get_len(s[i], s[i + 1])
        return result

    def find_different_random_places(self):
        i1 = randint(1, self.n - 1)
        i2 = randint(1, self.n - 1)
        if i1 == i2:
            return self.find_different_random_places()
        return min(i1, i2), max(i1, i2)

    def is_mutaded(self):
        return random() <= self.p

    def mutation(self, s):
        i1, i2 = self.find_different_random_places()
        print(f"Mutation: {s} -> {s[:i1] + s[i2] + s[i1 + 1 : i2] + s[i1] + s[i2 + 1 :]}")
        return s[:i1] + s[i2] + s[i1 + 1 : i2] + s[i1] + s[i2 + 1 :]

    def crossover(self, s1, s2, i1, i2):
        res1 = s1[:i1]
        for x in s2[i1:i2]:
            if x not in res1:
                res1 += x
        for x in s1:
            if x not in res1:
                res1 += x
        if self.is_mutaded():
            res1 = self.mutation(res1)
        print(f"Parent 1: {s1[:i1]}|{s1[i1:i2]}|{s1[i2:]}")
        print(f"Parent 2: {s2[:i1]}|{s2[i1:i2]}|{s2[i2:]}")
        print(f"Child 1: {res1[:i1]}|{res1[i1:i2]}|{res1[i2:]}\n")
        return res1

    def generate_random_gen_code(self):
        res = [str(i) for i in range(1, self.n + 1)]
        shuffle(res)
        return ''.join(res)
    @staticmethod
    def parents():
        n = 4  # hard-code
        res = [i for i in range(0, n)]
        shuffle(res)
        return res
