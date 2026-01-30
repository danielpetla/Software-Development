import time
import random
import matplotlib.pyplot as plt

plt.ion()
plt.axis("off")


def main():
    # TODO Initialize board
    n = 50
    board = [[True] * n for _ in range(n)]

    im = plt.imshow(board, cmap="Greys", vmax=1, vmin=0)
    while True:
        # TODO Update board
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = random.choice([True, False])

        im.set_data(board)
        plt.gcf().canvas.flush_events()
        time.sleep(0.5)


main()
