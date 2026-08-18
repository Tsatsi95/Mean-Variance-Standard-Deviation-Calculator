import numpy as np


def calculate(numbers):
    """Return summary statistics for a list reshaped into a 3 x 3 array."""
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(numbers).reshape(3, 3)

    def results(operation):
        return [
            operation(matrix, axis=0).tolist(),
            operation(matrix, axis=1).tolist(),
            operation(matrix).item(),
        ]

    return {
        "mean": results(np.mean),
        "variance": results(np.var),
        "standard deviation": results(np.std),
        "max": results(np.max),
        "min": results(np.min),
        "sum": results(np.sum),
    }
