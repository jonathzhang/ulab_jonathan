# orbital_period.py

def calculate_orbital_period(a):
    """
    Calculate the orbital period proportional to a^(3/2).

    Parameters:
    a (float): Semi-major axis (must be positive).

    Returns:
    float: Orbital period proportional to a^(3/2).
    """
    return a ** (3 / 2)
