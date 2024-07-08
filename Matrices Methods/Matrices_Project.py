# Write a Python program for a matrix class that can add and multiply twodimensional
# arrays of numbers, assuming the dimensions agree appropriately
# for the operation.


class Matrices:

    def row_cal(self, matrix):               # Function to calculate the number of rows in a matrix
        rows = 0
        for row in range(len(matrix)):
            rows += 1
        return rows

    def column_cal(self, matrix):           # Function to calculate the number of columns in a matrix
        columns = 0
        for column in range(len(matrix[0])):
            columns += 1
        return columns


    def product(self, number):              # Function to create the formula for calculating the dot product

        product_formula = ""

        for num in range(number):

            formula = f" + matrix_1[i][n+{num}] * matrix_2[m+{num}][j]"

            product_formula = product_formula + formula

        return product_formula[3:]              # Return the formula without the leading " + "


    def matrix_dot_product(self, matrix_1, matrix_2):              # Function to calculate the dot product of two matrices
        row_1 = self.row_cal(matrix_1)
        column_1 = self.column_cal(matrix_1)
                                                                   # Calculate the dimensions of both matrices
        row_2 = self.row_cal(matrix_2)
        column_2 = self.column_cal(matrix_2)

        print(f"Dimensions of matrix_1: {row_1} by {column_1}")
        print(f"Dimensions of matrix_2: {row_2} by {column_2}")
        final_matrix = []

        if column_1 == row_2:
            agreement = True                                   # Check if the matrices can be multiplied (columns of the first matrix should be equal to rows of the second matrix)
        else:
            agreement = False

        if agreement == True:
                                                                  # If the matrices can be multiplied
            i = 0
            j = 0
            m = 0
            n = 0


            if row_1 > column_1:                                 # Determine the dimension for the formula
                matrix_dim = row_1
            else:
                matrix_dim = column_1

            formula = self.product(matrix_dim)                          # Get the dot product formula
            for row_num in range(row_1):
                i = row_num
                products = []

                for col_num in range(column_2):                          # Calculate the dot product
                    j = col_num
                    dot_product = eval(formula)
                    products.append(dot_product)

                final_matrix.append(products)

            return final_matrix

        else:
            return print("Can't take dot product of these matrices because their dimensions do not agree.")


    def matrix_addition(self, matrix_1, matrix_2):                  # Function to add two matrices
        row_1 = self.row_cal(matrix_1)
        column_1 = self.column_cal(matrix_1)
                                                                     # Calculate the dimensions of both matrices
        row_2 = self.row_cal(matrix_2)
        column_2 = self.column_cal(matrix_2)

        print(f"Dimensions of matrix_1: {row_1} by {column_1}")
        print(f"Dimensions of matrix_2: {row_2} by {column_2}")

        additions_matrix = []

        if row_1 == row_2 and column_1 == column_2:                    # Check if the matrices have the same dimensions
            a = 0
            b = 0
            for num_row in range(row_1):                       # Calculate the addition of each corresponding element
                a = num_row
                additions_list = []

                for num_col in range(column_2):
                    b = num_col
                    addition = matrix_1[a][b] + matrix_2[a][b]

                    additions_list.append(addition)

                additions_matrix.append(additions_list)

            return additions_matrix

        else:
            return print("Can't do addition because the matrices have different dimensions.")


# Manually created 10x10 array 1
array1 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]

# Manually created 10x10 array 2
array2 = [
    [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
    [90, 89, 88, 87, 86, 85, 84, 83, 82, 81],
    [80, 79, 78, 77, 76, 75, 74, 73, 72, 71],
    [70, 69, 68, 67, 66, 65, 64, 63, 62, 61],
    [60, 59, 58, 57, 56, 55, 54, 53, 52, 51],
    [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],
    [40, 39, 38, 37, 36, 35, 34, 33, 32, 31],
    [30, 29, 28, 27, 26, 25, 24, 23, 22, 21],
    [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]


my_matrix = Matrices()      # Creates an instance of class Matrices



# Testing the dot_product method

matrix_multiplication  = my_matrix.matrix_dot_product(array1,array2)
for item in matrix_multiplication:
    print(item)



# Testing the matrix_addition method

addition_of_matrix = my_matrix.matrix_addition(array1, array2)
for item in addition_of_matrix:
    print(item)
