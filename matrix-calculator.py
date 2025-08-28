import numpy as np

class MatrixCalculator:
    def __init__(self):
        self.matrices = {}

    def add_matrix(self, name, matrix):
        self.matrices[name] = np.array(matrix)

    def get_matrix(self, name):
        return self.matrices.get(name)

    def add(self, name1, name2):
        if name1 in self.matrices and name2 in self.matrices:
            return self.matrices[name1] + self.matrices[name2]
        else:
            raise ValueError("One or both matrices not found.")

    def subtract(self, name1, name2):
        if name1 in self.matrices and name2 in self.matrices:
            return self.matrices[name1] - self.matrices[name2]
        else:
            raise ValueError("One or both matrices not found.")

    def multiply(self, name1, name2):
        if name1 in self.matrices and name2 in self.matrices:
            return np.dot(self.matrices[name1], self.matrices[name2])
        else:
            raise ValueError("One or both matrices not found.")

    def transpose(self, name):
        if name in self.matrices:
            return self.matrices[name].T
        else:
            raise ValueError("Matrix not found.")

    def determinant(self, name):
        if name in self.matrices:
            return np.linalg.det(self.matrices[name])
        else:
            raise ValueError("Matrix not found.")

    def inverse(self, name):
        if name in self.matrices:
            return np.linalg.inv(self.matrices[name])
        else:
            raise ValueError("Matrix not found.")
        
    def display(self, name):
        if name in self.matrices:
            print(self.matrices[name])
        else:
            raise ValueError("Matrix not found.")   
        
# Example usage:
if __name__ == "__main__":  
    calc = MatrixCalculator()
    calc.add_matrix("A", [[1, 2], [3, 4]])
    calc.add_matrix("B", [[5, 6], [7, 8]])
    
    print("Matrix A:")
    calc.display("A")
    
    print("\nMatrix B:")
    calc.display("B")
    
    print("\nA + B:")
    print(calc.add("A", "B"))
    
    print("\nA - B:")
    print(calc.subtract("A", "B"))
    
    print("\nA * B:")
    print(calc.multiply("A", "B"))
    
    print("\nTranspose of A:")
    print(calc.transpose("A"))
    
    print("\nDeterminant of A:")
    print(calc.determinant("A"))
    
    print("\nInverse of A:")
    print(calc.inverse("A"))
