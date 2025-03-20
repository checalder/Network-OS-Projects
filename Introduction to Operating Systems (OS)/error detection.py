# Function to compute even parity bit
def compute_even_parity(data):
    """
    Computes the even parity bit for a given list of binary data.
    
    Parameters:
        data (list): List of binary bits (0s and 1s).
    
    Returns:
        int: The computed even parity bit (0 or 1).
    """
    return sum(data) % 2  # Even parity is calculated by summing the bits and taking modulo 2

# Example of original data bits
data = [1, 0, 1, 0, 1, 1, 0, 0]  # Binary data sequence
parity_bit = compute_even_parity(data)  # Compute the even parity bit

print("Original Data: ", data)
print("Computed Parity Bit (Even):", parity_bit)

# Transmitting data by appending parity bit
transmitted_data = data + [parity_bit]
print("\nTransmitted Data (Data + Parity):", transmitted_data)

# Simulate an error by flipping a bit at a specific index (e.g., index 3)
error_index = 3

# Create a copy of the transmitted data with an error introduced
data_with_error = transmitted_data.copy()
data_with_error[error_index] = 1 - data_with_error[error_index]  # Flip the bit

print("\nData with an Error Introduced at index", error_index, ":", data_with_error)

# Receiver performs parity check by summing all bits and verifying parity
if sum(data_with_error) % 2 == parity_bit:
    print("\nNo error detected (Parity Check Passed)")
else:
    print("\nError detected (Parity Check Failed)")
