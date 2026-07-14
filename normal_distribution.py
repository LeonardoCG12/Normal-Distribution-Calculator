#!/usr/bin/python3
import statistics


def calculate_z_score(x: float, mean: float, std_dev: float) -> float:
    return (x - mean) / std_dev


def main():
    print("--- Normal Distribution Calculator ---")
    try:
        mean = float(input("Mean: "))
        std_dev = float(input("Standard Deviation: "))
    except ValueError:
        print("Error: Please enter valid numerical values.")
        return

    dist = statistics.NormalDist(mu=mean, sigma=std_dev)

    print("\nOptions:")
    print("1: Left side (Less than X)")
    print("2: Right side (Greater than X)")
    print("3: Between (Between X1 and X2)")

    try:
        option = int(input("Option: "))
    except ValueError:
        print("Error: Choose a valid option (1, 2, or 3).")
        return

    if option == 1:
        x = float(input("Value: "))
        z = calculate_z_score(x, mean, std_dev)
        prob = dist.cdf(x)

        print(f"\nz = {z:.2f}")
        print(f"P(x) = {prob * 100:.2f}%")

    elif option == 2:
        x = float(input("Value: "))
        z = calculate_z_score(x, mean, std_dev)
        prob = 1 - dist.cdf(x)

        print(f"\nz = {z:.2f}")
        print(f"P(x) = {prob * 100:.2f}%")

    elif option == 3:
        x1 = float(input("Left value: "))
        x2 = float(input("Right value: "))

        z1 = calculate_z_score(x1, mean, std_dev)
        z2 = calculate_z_score(x2, mean, std_dev)

        prob = abs(dist.cdf(x2) - dist.cdf(x1))

        print(f"\nz1 = {z1:.2f}, z2 = {z2:.2f}")
        print(f"P(x) = {prob * 100:.2f}%")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
