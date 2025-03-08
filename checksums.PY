def ones_complement_sum(a, b, bit_size=16):
    """Perform one's complement addition of two numbers."""
    result = a + b
    if result >= (1 << bit_size): # If there's an overflow, the << means the 1 is moved 16 places to the right effectively equalin 10000000000000000 which is the 1 with 16 0s (17 digit total), thus the next power above the largest 16 digit number.
        # overflow is if the actual result is greater than the maximum value that can be stored in 
        # the binary number, remember that the the most important bit is doubled in its next bit if 
        # there was a carry past it on the left
        result = (result + 1) & ((1 << bit_size) - 1) # Wrap around carry using the & operator 
    return result

res = ones_complement_sum(0b1010101010101010, 0b1010101010101010)#0b specifies that the number is in binary

print(res)

def calculate_checksum(data, bit_size=16):
    """Compute one's complement checksum for a list of integers."""
    checksum = 0
    for word in data:
        checksum = ones_complement_sum(checksum, word, bit_size)
    return ~checksum & ((1 << bit_size) - 1) # One's complement

def verify_checksum(data, received_checksum, bit_size=16):
    """Verify the checksum by adding it to the computed sum."""
    total = 0
    for word in data:
        total = ones_complement_sum(total, word, bit_size)
    total = ones_complement_sum(total, received_checksum, bit_size)
    return total == (1 << bit_size) - 1 # Valid if all bits are 1

# Example Usage
data = [0b1010101010101010, 0b1100110011001100, 0b1111000011110000] # Example 16-bit words
checksum = calculate_checksum(data)
print(f"Calculated Checksum: {bin(checksum)}")
# Verification
is_valid = verify_checksum(data, checksum)
print("Checksum is valid" if is_valid else "Checksum is invalid")