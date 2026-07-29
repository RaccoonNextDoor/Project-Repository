"""Matrix operations used in the project exercises."""

Number = int | float
Matrix = list[list[Number]]


def _matrix_shape(matrix: Matrix, name: str) -> tuple[int, int]:
    """Validate a matrix and return its number of rows and columns.

    Args:
        matrix: Matrix represented as a list of non-empty rows.
        name: Matrix name used in error messages.

    Returns:
        A tuple containing ``(number_of_rows, number_of_columns)``.

    Raises:
        ValueError: If the matrix is empty, contains an empty row,
            or has rows of unequal length.
        TypeError: If a matrix entry is not an integer or float.
    """
    if not isinstance(matrix, list) or not matrix:
        raise ValueError(f"{name} must be a non-empty list of rows.")

    if any(not isinstance(row, list) or not row for row in matrix):
        raise ValueError(f"{name} must contain non-empty list rows.")

    column_count = len(matrix[0])

    # Every row must have the same number of entries for the matrix
    # to be rectangular.
    if any(len(row) != column_count for row in matrix):
        raise ValueError(f"{name} must be rectangular.")

    # This implementation only accepts numeric matrix entries.
    if any(
        not isinstance(value, (int, float))
        for row in matrix
        for value in row
    ):
        raise TypeError(f"{name} must contain only numeric values.")

    return len(matrix), column_count


def matmul(a: Matrix, b: Matrix) -> Matrix:
    """Multiply two matrices using the standard triple-loop algorithm.

    The number of columns in ``a`` must equal the number of rows in ``b``.

    Args:
        a: Left matrix with dimensions ``m × n``.
        b: Right matrix with dimensions ``n × p``.

    Returns:
        The product matrix with dimensions ``m × p``.

    Raises:
        ValueError: If a matrix is invalid or the dimensions are
            incompatible.
        TypeError: If either matrix contains a non-numeric value.

    Example:
        >>> matmul([[1, 2]], [[3], [4]])
        [[11]]
    """
    m, n = _matrix_shape(a, "Matrix A")
    n_b, p = _matrix_shape(b, "Matrix B")

    if n != n_b:
        raise ValueError(
            "Matrix A column count must equal Matrix B row count."
        )

    # Start with an m × p result matrix filled with zeros.
    result: Matrix = [
        [0 for _ in range(p)]
        for _ in range(m)
    ]

    # Each result entry is the dot product of one row of A
    # and one column of B.
    for i in range(m):
        for j in range(p):
            total: Number = 0

            for k in range(n):
                total += a[i][k] * b[k][j]

            result[i][j] = total

    return result
