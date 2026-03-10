from curses import wrapper


def main(stdscr):
    x, y = 0, 0
    while True:
        # Clear screen
        stdscr.clear()
        # Print "Hello" at coordinate y, x; y first for historical reasons
        stdscr.addstr(y, x, "Hello")
        # Actually write out the data to the terminal
        stdscr.refresh()
        # Wait for a key to be pressed
        c = stdscr.getkey()
        if c == "KEY_DOWN":
            y += 1
        elif c == "KEY_UP":
            y -= 1
        elif c == "KEY_RIGHT":
            x += 1
        elif c == "KEY_LEFT":
            x -= 1


if __name__ == "__main__":
    wrapper(main)
