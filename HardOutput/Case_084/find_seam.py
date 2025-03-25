import numpy as np

def find_seam(energy_map: np.array) -> list:
    """
    Identify the optimal vertical seam to insert into the image based on the energy map. The seam is a path of pixels
    from top to bottom with the least cumulative energy.

    Parameters:
    -----------
    energy_map : np.array
        A 2D array representing the energy map with shape (height × width).

    Returns:
    --------
    seam : list
        A list of column indices representing the seam to be inserted. Each index corresponds to the column position
        of the seam in a specific row of the image.

    Requirements:
    -------------
    - The seam should be computed using dynamic programming to ensure the path has the minimum cumulative energy.
    - The seam should be continuous from the top to the bottom of the image.
    """
    height, width = energy_map.shape
    dp_table = np.copy(energy_map)

    # Dynamic programming to fill the dp_table
    for i in range(1, height):
        for j in range(width):
            if j == 0:
                dp_table[i, j] += min(dp_table[i-1, j], dp_table[i-1, j+1])
            elif j == width - 1:
                dp_table[i, j] += min(dp_table[i-1, j-1], dp_table[i-1, j])
            else:
                dp_table[i, j] += min(dp_table[i-1, j-1], dp_table[i-1, j], dp_table[i-1, j+1])

    # Backtracking to find the seam
    seam = []
    j = np.argmin(dp_table[-1])  # Start from the bottom row
    seam.append(j)

    for i in range(height - 2, -1, -1):  # Move upwards
        if j == 0:
            j = np.argmin(dp_table[i, j:j+2])
        elif j == width - 1:
            j = j - 1 + np.argmin(dp_table[i, j-1:j+1])
        else:
            j = j - 1 + np.argmin(dp_table[i, j-1:j+2])
        seam.append(j)

    seam.reverse()  # Reverse to get the seam from top to bottom
    return seam