#!/usr/bin/env python3
"""
Hamming Code Error Detection
Find the position of error when sender sends 11110000 and receiver gets 10110000
"""

def calculate_parity_positions(codeword):
    """
    Calculate syndrome bits by checking parity at positions that are powers of 2
    In Hamming code, parity bits are at positions: 1, 2, 4, 8, 16, ...
    """
    n = len(codeword)
    syndrome = []
    parity_positions = []

    # Find all parity bit positions (powers of 2)
    pos = 1
    while pos <= n:
        parity_positions.append(pos)
        pos *= 2

    print(f"Codeword length: {n} bits")
    print(f"Parity bit positions: {parity_positions}")
    print()

    # Calculate syndrome for each parity position
    for parity_pos in parity_positions:
        parity = 0
        checked_positions = []

        # Check all positions where the bit at parity_pos position is 1
        for i in range(1, n + 1):
            # Check if position i should be included in this parity check
            # Position i is included if bit at position parity_pos in binary representation of i is 1
            if i & parity_pos:
                checked_positions.append(i)
                # Convert to 0-indexed for array access
                parity ^= int(codeword[i - 1])

        print(f"Parity P{parity_pos} checks positions: {checked_positions}")
        print(f"  Bits at these positions: {[codeword[p-1] for p in checked_positions]}")
        print(f"  Parity result: {parity}")

        syndrome.append(parity)

    return syndrome, parity_positions

def find_error_position(sent, received):
    """
    Find the error position using Hamming code syndrome
    """
    print("=" * 70)
    print("HAMMING CODE ERROR DETECTION")
    print("=" * 70)
    print()

    print(f"Sent:     {sent}")
    print(f"Received: {received}")
    print()

    # Find the bit that differs
    diff_positions = []
    for i in range(len(sent)):
        if sent[i] != received[i]:
            diff_positions.append(i + 1)  # 1-indexed position

    print(f"Actual error at position(s): {diff_positions} (1-indexed)")
    print()

    # Calculate syndrome from received codeword
    print("Calculating syndrome from RECEIVED codeword:")
    print("-" * 70)
    syndrome, parity_positions = calculate_parity_positions(received)

    print()
    print(f"Syndrome bits (S): {syndrome}")

    # Calculate error position from syndrome
    # The syndrome bits form a binary number indicating the error position
    error_position = 0
    for i, bit in enumerate(syndrome):
        error_position += bit * (2 ** i)

    print()
    print("=" * 70)
    print(f"RESULT: Error detected at position {error_position} (1-indexed)")
    print("=" * 70)
    print()

    if error_position > 0:
        print(f"To correct: Flip bit at position {error_position}")
        corrected = list(received)
        corrected[error_position - 1] = '1' if corrected[error_position - 1] == '0' else '0'
        corrected = ''.join(corrected)
        print(f"Corrected codeword: {corrected}")

        if corrected == sent:
            print("✓ Correction successful! Matches original sent codeword.")
        else:
            print("Note: Corrected codeword differs from sent (possible multiple errors)")

    return error_position

# Main execution
if __name__ == "__main__":
    sent_codeword = "11110000"
    received_codeword = "10110000"

    error_pos = find_error_position(sent_codeword, received_codeword)

    print()
    print("=" * 70)
    print("EXPLANATION:")
    print("=" * 70)
    print("""
In Hamming code, parity bits are placed at positions that are powers of 2 (1, 2, 4, 8...).
Each parity bit checks specific positions where that bit position is set in the binary
representation of the position number.

To find the error:
1. Calculate parity at each parity position in the RECEIVED codeword
2. The syndrome bits (S1, S2, S3...) form a binary number
3. This binary number directly gives the error position
4. If syndrome = 0, no error detected
5. If syndrome > 0, flip the bit at that position to correct
    """)
