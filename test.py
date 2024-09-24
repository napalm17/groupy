import numpy as np


def transform_indices(input_array):
    input_array = np.array(input_array)
    result = np.zeros_like(input_array, dtype=int)  # Initialize result array with zeros

    # Get unique values and their counts
    unique_values, counts = np.unique(input_array, return_counts=True)

    # Assign values centered around zero
    for unique_value, count in zip(unique_values, counts):
        indices = np.where(input_array == unique_value)[0]
        half_range = (count - 1) // 2
        centered_values = np.arange(-half_range, half_range + 1)
        result[indices] = centered_values[:len(indices)]  # Ensure correct length

    return result


# Example usage
input_array = [1, 2, 3, 3, 3, 3, 3, 5, 5, 5, 6]
output_array = transform_indices(input_array)
print(output_array)  # Output: centered values
