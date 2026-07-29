"""Pytest test cases for matrix multiplication."""

import pytest

from src.matrix_operations import matmul


# Positive case 1: ordinary square matrices.
def test_square_matrices():
    assert matmul(
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ) == [[19, 22], [43, 50]]


# Positive case 2: rectangular matrices.
def test_rectangular_matrices():
    assert matmul(
        [[1, 2, 3], [4, 5, 6]],
        [[7, 8], [9, 10], [11, 12]],
    ) == [[58, 64], [139, 154]]


# Positive case 3: multiplication by an identity matrix.
def test_identity_matrix():
    assert matmul(
        [[4, 7], [2, 6]],
        [[1, 0], [0, 1]],
    ) == [[4, 7], [2, 6]]


# Positive case 4: valid negative matrix values.
def test_negative_values():
    assert matmul(
        [[-1, 2]],
        [[3], [-4]],
    ) == [[-11]]


# Negative case 1: dimensions are incompatible.
def test_incompatible_dimensions():
    with pytest.raises(ValueError, match="column count"):
        matmul(
            [[1, 2, 3]],
            [[1, 2], [3, 4]],
        )


# Negative case 2: one matrix is empty.
def test_empty_matrix():
    with pytest.raises(ValueError, match="non-empty"):
        matmul([], [[1]])


# Negative case 3: rows have unequal lengths.
def test_ragged_matrix():
    with pytest.raises(ValueError, match="rectangular"):
        matmul(
            [[1, 2], [3]],
            [[1], [2]],
        )


# Negative case 4: a matrix contains non-numeric data.
def test_non_numeric_value():
    with pytest.raises(TypeError, match="numeric"):
        matmul(
            [[1, "two"]],
            [[1], [2]],
        )
