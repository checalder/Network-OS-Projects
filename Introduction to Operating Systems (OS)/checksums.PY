def ones_complement_sum(a, b, bit_size=16):
    """
    Perform one's complement addition of two binary numbers.
    This is used in checksum calculations for error detection.
    
    Parameters:
        a (int): First binary number.
        b (int): Second binary number.
        bit_size (int): Bit width of the numbers (default is 16-bit).
    
    Returns:
        int: Sum of the numbers using one's complement arithmetic.
    """
    result = a + b
    
    # If the sum exceeds the allowed bit size, wrap the carry around
    if result >= (1 << bit_size):  # Overflow condition
        result = (result + 1) & ((1 << bit_size) - 1)  # Wrap-around carry
    
    return result

# Example test for one's complement sum
res = ones_complement_sum(0b1010101010101010, 0b1010101010101010)  # Binary addition
print(res)

def calculate_checksum(data, bit_size=16):
    """
    Compute one's complement checksum for a list of binary numbers.
    
    Parameters:
        data (list): List of binary words (integers).
        bit_size (int): Bit width of the checksum (default is 16-bit).
    
    Returns:
        int: Computed checksum.
    """
    checksum = 0
    for word in data:
        checksum = ones_complement_sum(checksum, word, bit_size)
    
    return ~checksum & ((1 << bit_size) - 1)  # Apply one's complement

def verify_checksum(data, received_checksum, bit_size=16):
    """
    Verify the checksum by adding the received checksum to the computed sum.
    If the result is all ones (i.e., one's complement sum should be all 1s),
    the checksum is valid.
    
    Parameters:
        data (list): List of binary words (integers).
        received_checksum (int): The checksum received with the data.
        bit_size (int): Bit width of the checksum (default is 16-bit).
    
    Returns:
        bool: True if the checksum is valid, False otherwise.
    """
    total = 0
    for word in data:
        total = ones_complement_sum(total, word, bit_size)
    total = ones_complement_sum(total, received_checksum, bit_size)
    
    return total == (1 << bit_size) - 1  # Check if all bits are 1

# Example Usage
# Define example 16-bit words
data = [0b1010101010101010, 0b1100110011001100, 0b1111000011110000] 

# Calculate the checksum
checksum = calculate_checksum(data)
print(f"Calculated Checksum: {bin(checksum)}")

# Verify the checksum
is_valid = verify_checksum(data, checksum)
print("Checksum is valid" if is_valid else "Checksum is invalid")
