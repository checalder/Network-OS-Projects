import numpy as np  # Import NumPy for array manipulations

def compute_parity(mat):
    """
    Compute the parity bits for a given binary matrix.
    Returns:
        - Row parity (computed along axis 1)
        - Column parity (computed along axis 0)
    """
    return np.sum(mat, axis=1) % 2, np.sum(mat, axis=0) % 2

# Create a 4x4 binary data matrix
# Each row represents a sequence of bits
# The parity bits will be calculated based on this matrix

data = np.array([
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 1, 1]
])

print("Original Data:\n", data)

# Compute original parity bits (even parity)
row_par, col_par = compute_parity(data)
print("Row Parity:", row_par)
print("Column Parity:", col_par)

# Introduce an error by flipping a bit at position (2,1)
data_err = data.copy()
data_err[2, 1] = 1 - data_err[2, 1]
print("\nData with error at (2, 1):\n", data_err)

# Recompute parity bits after error introduction
new_row_par, new_col_par = compute_parity(data_err)
print("New Row Parity:", new_row_par)
print("New Column Parity:", new_col_par)

# Detect the row and column where an error has occurred
err_row = np.where(new_row_par != row_par)[0]  # Find the index where row parity differs
err_col = np.where(new_col_par != col_par)[0]  # Find the index where column parity differs

print("Error Row Indices:", err_row)
print("Error Column Indices:", err_col)

# If a single error is detected, correct it by flipping the bit back
if err_row.size == 1 and err_col.size == 1:
    error_location = (err_row[0], err_col[0])
    print("\nError detected at:", error_location)
    # Correct the error by flipping the erroneous bit back
    data_err[error_location] = 1 - data_err[error_location]
    print("Corrected Data:\n", data_err)
else:
    print("No single-bit error detected or multiple errors occurred.")
