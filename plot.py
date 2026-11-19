"""Plot a space-time diagram for the traffic model."""

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, ListedColormap

from model import simulate


def main() -> None:
    rows = simulate(20, 0.3, steps=200, seed=1)
    speed_cmap = LinearSegmentedColormap.from_list("speed", ["red", "blue"], N=6)
    colors = ["white", *(speed_cmap(i / 5) for i in range(6))]
    cmap = ListedColormap(colors)
    norm = BoundaryNorm(
        [-1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
        cmap.N,
    )

    fig, ax = plt.subplots(figsize=(12, 8))
    image = ax.imshow(
        rows,
        cmap=cmap,
        norm=norm,
        interpolation="nearest",
        aspect="auto",
        origin="upper",
    )
    ax.set_xlabel("Cell")
    ax.set_ylabel("Time step")
    ax.set_title("Traffic space-time diagram")

    colorbar = fig.colorbar(image, ax=ax, ticks=range(-1, 6))
    colorbar.ax.set_yticklabels(["empty", "0", "1", "2", "3", "4", "5"])
    colorbar.set_label("Cell state (car speed)")

    fig.tight_layout()
    fig.savefig("jam.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    main()
