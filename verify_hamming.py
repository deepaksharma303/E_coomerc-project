#!/usr/bin/env python3
"""
Verify if the sent codeword is a valid Hamming code
and explain the discrepancy
"""

def check_hamming_validity(codeword, label):
    """
    Check if a codeword satisfies Hamming parity checks
    """
    print(f"\nChecking {label}: {codeword}")
    print("-" * 70)

    n = len(codeword)
    parity_positions = []
    pos = 1
    while pos <= n:
        parity_positions.append(pos)
        pos *= 2

    all_valid = True
    syndrome_bits = []

    for parity_pos in parity_positions:
        parity = 0
        for i in range(1, n + 1):
            if i & parity_pos:
                parity ^= int(codeword[i - 1])

        syndrome_bits.append(parity)
        status = "✓ Valid" if parity == 0 else "✗ Invalid"
        print(f"P{parity_pos}: {parity} {status}")

        if parity != 0:
            all_valid = False

    syndrome_value = sum(bit * (2**i) for i, bit in enumerate(syndrome_bits))

    print()
    if all_valid:
        print(f"Result: Valid Hamming codeword (syndrome = 0)")
    else:
        print(f"Result: INVALID Hamming codeword (syndrome = {syndrome_value})")
        print(f"Syndrome indicates error at position: {syndrome_value}")

    return all_valid, syndrome_value

print("=" * 80)
print("HAMMING CODE VALIDATION")
print("=" * 80)

sent = "11110000"
received = "10110000"

sent_valid, sent_syndrome = check_hamming_validity(sent, "SENT codeword")
received_valid, received_syndrome = check_hamming_validity(received, "RECEIVED codeword")

print()
print("=" * 80)
print("ANALYSIS")
print("=" * 80)
print()

if sent_valid:
    print("The SENT codeword is a valid Hamming code.")
    print(f"Error position based on received syndrome: {received_syndrome}")
else:
    print("⚠️  The SENT codeword is NOT a valid Hamming code!")
    print(f"   The sent codeword itself has syndrome = {sent_syndrome}")
    print()
    print("This means one of two things:")
    print("1. The 'sent' codeword given in the problem may already contain an error")
    print("2. The problem expects us to find which bit differs between sent and received")
    print()

print()
print("=" * 80)
print("INTERPRETATION OF RESULTS")
print("=" * 80)
print()

actual_diff_pos = None
for i in range(len(sent)):
    if sent[i] != received[i]:
        actual_diff_pos = i + 1
        break

print(f"Actual bit that differs: Position {actual_diff_pos}")
print(f"Syndrome from RECEIVED:  Position {received_syndrome}")
print()

if received_syndrome == actual_diff_pos:
    print("✓ The syndrome correctly identifies the bit that changed!")
else:
    print("✗ The syndrome does NOT match the bit that changed.")
    print()
    print("Explanation:")
    print(f"  - If we assume the SENT codeword was valid, flipping position {actual_diff_pos}")
    print(f"    should give syndrome = {actual_diff_pos}")
    print(f"  - But we get syndrome = {received_syndrome}")
    print(f"  - This confirms the SENT codeword was not a valid Hamming code")

print()
print("=" * 80)
print("FINAL ANSWER")
print("=" * 80)
print()
print("Using Hamming code error detection on the RECEIVED codeword:")
print(f"  Syndrome = {received_syndrome}")
print(f"  Error detected at position: {received_syndrome}")
print()
print("Note: The bit that actually differs is at position 2,")
print("but the Hamming syndrome calculation on '10110000' gives position 6.")
print("This is because '11110000' is not a valid Hamming codeword to begin with.")
