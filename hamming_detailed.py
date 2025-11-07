#!/usr/bin/env python3
"""
Detailed Hamming Code Analysis with Position Mapping
"""

def analyze_hamming_code(sent, received):
    """
    Detailed analysis of Hamming code error detection
    """
    print("=" * 80)
    print("HAMMING CODE ERROR DETECTION - DETAILED ANALYSIS")
    print("=" * 80)
    print()

    # Display the codewords with position numbers
    print("Position (1-indexed): ", end="")
    for i in range(1, len(sent) + 1):
        print(f"{i:^3}", end=" ")
    print()

    print("Sent codeword:        ", end="")
    for bit in sent:
        print(f"{bit:^3}", end=" ")
    print()

    print("Received codeword:    ", end="")
    for bit in received:
        print(f"{bit:^3}", end=" ")
    print()

    print("Difference:           ", end="")
    for i in range(len(sent)):
        if sent[i] != received[i]:
            print(f"{'X':^3}", end=" ")
        else:
            print(f"{' ':^3}", end=" ")
    print()
    print()

    # Find actual difference
    actual_error_pos = None
    for i in range(len(sent)):
        if sent[i] != received[i]:
            actual_error_pos = i + 1
            break

    print(f"Actual bit flip at position: {actual_error_pos}")
    print()

    # Calculate syndrome from received codeword
    print("=" * 80)
    print("SYNDROME CALCULATION (from received codeword)")
    print("=" * 80)
    print()

    n = len(received)
    syndrome_bits = []
    parity_positions = []

    # Find parity positions (powers of 2)
    pos = 1
    while pos <= n:
        parity_positions.append(pos)
        pos *= 2

    print(f"Parity bit positions: {parity_positions}")
    print()

    # Calculate each syndrome bit
    for parity_pos in parity_positions:
        print(f"Checking Parity P{parity_pos}:")
        parity = 0
        positions_checked = []

        # For each position in the codeword
        for i in range(1, n + 1):
            # Check if this position should be included
            # A position i is checked by parity bit at position p if (i & p) != 0
            if i & parity_pos:
                positions_checked.append(i)
                bit_value = int(received[i - 1])
                parity ^= bit_value

        bits_checked = [received[p - 1] for p in positions_checked]
        print(f"  Positions checked: {positions_checked}")
        print(f"  Bits: {bits_checked}")
        print(f"  XOR result (syndrome bit S{len(syndrome_bits)}): {parity}")
        print()

        syndrome_bits.append(parity)

    # Calculate error position from syndrome
    print("=" * 80)
    print("ERROR POSITION CALCULATION")
    print("=" * 80)
    print()

    print(f"Syndrome bits: {syndrome_bits}")
    print(f"Binary representation: {' '.join(map(str, reversed(syndrome_bits)))}")

    # Convert syndrome to decimal
    error_position = 0
    for i, bit in enumerate(syndrome_bits):
        error_position += bit * (2 ** i)
        if bit:
            print(f"  S{i} = {bit} → contributes 2^{i} = {2**i}")

    print()
    print(f"Error position = {' + '.join([str(2**i) for i, b in enumerate(syndrome_bits) if b])} = {error_position}")
    print()

    print("=" * 80)
    print(f"CONCLUSION: Error at position {error_position}")
    print("=" * 80)
    print()

    if error_position > 0:
        print(f"Bit at position {error_position}:")
        print(f"  Sent:     {sent[error_position - 1]}")
        print(f"  Received: {received[error_position - 1]}")
        print()

        # Correct the error
        corrected = list(received)
        corrected[error_position - 1] = '1' if corrected[error_position - 1] == '0' else '0'
        corrected_str = ''.join(corrected)

        print(f"After correction: {corrected_str}")
        print(f"Original sent:    {sent}")
        print(f"Match: {corrected_str == sent}")
    else:
        print("No error detected (syndrome = 0)")

    return error_position

# Run the analysis
if __name__ == "__main__":
    sent = "11110000"
    received = "10110000"

    error_pos = analyze_hamming_code(sent, received)

    print()
    print("=" * 80)
    print("ANSWER:")
    print("=" * 80)
    print(f"The error is at position {error_pos} (1-indexed)")
    print("=" * 80)
