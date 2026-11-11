"""Compute and print the Collatz sequence starting from 27."""


def collatz_sequence(start):
    """Return (sequence, steps) from start up to and including the first 1.

    steps counts the transformations applied, independently of the list length.
    """
    if start < 1:
        raise ValueError("start must be a positive integer")
    sequence = [start]
    steps = 0
    n = start
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
        steps += 1
    return sequence, steps


def main():
    sequence, steps = collatz_sequence(27)

    assert sequence[0] == 27
    assert sequence[-1] == 1
    assert steps == len(sequence) - 1

    for value in sequence:
        print(value)
    print(f"Total steps: {steps}")


if __name__ == "__main__":
    main()
