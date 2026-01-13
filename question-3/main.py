from recursive_drawing import draw_recursive_polygon


def get_valid_inputs():
    """
    Get and validate user inputs.
    """
    try:
        sides = int(input("Enter the number of sides: "))
        side_length = float(input("Enter the side length: "))
        depth = int(input("Enter the recursion depth: "))
    except ValueError:
        print("Invalid input: Please enter numbers only.")
        return None

    if sides < 3:
        print("Number of sides must be at least 3.")
        return None
    if side_length <= 0:
        print("Side length must be greater than 0.")
        return None
    if depth < 0:
        print("Recursion depth must be 0 or greater.")
        return None
    if depth > 6:
        print("Warning: Depth > 6 may be slow.")

    return sides, side_length, depth


def main():
    inputs = get_valid_inputs()
    if inputs is None:
        return

    sides, side_length, depth = inputs
    draw_recursive_polygon(sides, side_length, depth)


if __name__ == "__main__":
    main()
