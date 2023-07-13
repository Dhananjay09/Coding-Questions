class Solution:

    def __init__(self, matrix):
        self.matrix = matrix

    def rotate_clockwise(self):
        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix[0])):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

        for row in self.matrix:
            row.reverse()

    def rotate_anti_clockwise(self):

        for row in self.matrix:
            row.reverse()

        for i in range(len(self.matrix)):
            for j in range(i, len(self.matrix[0])):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

