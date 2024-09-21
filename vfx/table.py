import matplotlib.pyplot as plt
import numpy as np



class Table:
    def __init__(self, matrix: np.ndarray):
        """
        Parameters:
        matrix (np.ndarray): A 2D NumPy array representing the Cayley table.
        """
        self.matrix = matrix

    def __str__(self):
        """Formats the matrix as a rectangular table with horizontal lines when printed."""
        max_len = max(len(str(item)) for row in self.matrix for item in row)
        separator = '-' * ((max_len + 3) * len(self.matrix[0]) - 1)
        rows = [" | ".join(f"{str(item):>{max_len}}" for item in row) for row in self.matrix]
        table_with_lines = f"\n{separator}\n".join(rows)
        return f"{separator}\n{table_with_lines}\n{separator}"

    def plot(self):
        """
        Plots the Cayley table using matplotlib, visualizing the table as a heatmap.

        The matrix entries are mapped to unique colors, and a color bar is included
        to show the mapping of values to colors.

        Returns:
        None
        """
        unique_elements = np.unique(self.matrix)
        element_to_num = {elem: i for i, elem in enumerate(unique_elements)}
        numeric_matrix = np.array([[element_to_num[item] for item in row] for row in self.matrix])
        fig, ax = plt.subplots()
        cax = ax.matshow(numeric_matrix, cmap="Dark2")
        fig.colorbar(cax)
        ax.set_xticks([])
        ax.set_yticks([])
        n_rows, n_cols = self.matrix.shape
        for i in range(n_rows):
            for j in range(n_cols):
                value = self.matrix[i, j]
                ax.text(j, i, str(value), va='center', ha='center', color="black", fontsize=8)

        plt.title('Cayley Table')
        plt.show()

id = np.zeros((5,5))

#Table(id).plot()