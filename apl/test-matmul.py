import unittest
from matmul_correct import matrix_multiply

class TestMatrixMultiplication(unittest.TestCase):
    def test_valid_multiplication(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[5, 6], [7, 8]]
        expected_result = [[19, 22], [43, 50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_different_dimensions(self):
        matrix1 = [[1, 2, 3], [4, 5, 6]]
        matrix2 = [[1, 2], [3, 4], [5, 6]]
        expected_result = [[22, 28], [49, 64]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_1x1_matrices(self):
        matrix1 = [[5]]
        matrix2 = [[10]]
        expected_result = [[50]]
        self.assertEqual(matrix_multiply(matrix1, matrix2), expected_result)

    def test_incompatible_dimensions(self):
        matrix1 = [[1, 2], [3, 4]]
        matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_empty_matrix(self):
        matrix1 = []
        matrix2 = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            matrix_multiply(matrix1, matrix2)

    def test_non_numeric_elements(self):
        matrix1 = [[1, "a"], [3, 4]]
        matrix2 = [[1, 2], [3, 4]]
        with self.assertRaises(TypeError):
            matrix_multiply(matrix1, matrix2)


if __name__ == "__main__":
    unittest.main()
