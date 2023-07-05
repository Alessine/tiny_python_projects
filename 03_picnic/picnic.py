#!/usr/bin/env python3
"""
Author : Angela Niederberger <angelaniederberger@protonmail.ch>
Date   : 2023-07-05
Purpose: Plan a Picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='Item(s) to bring',
                        nargs="+")

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.positional

    if args.sorted:
        items.sort()

#    if len(items) < 2:
#        print(f"You are bringing {items[0]}.")
#    elif len(items) < 3:
#        print(f"You are bringing {items[0]} and {items[1]}.")
#    else:
#        items.insert(-1, "and")
#        print(f"You are bringing {', '.join(items[:-1])} {items[-1]}.")

    # Solution
    bringing = ""
    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = " and ".join(items)
    else:
        items[-1] = "and " + items[-1]
        bringing = ", ".join(items)

    print(f"You are bringing {bringing}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
