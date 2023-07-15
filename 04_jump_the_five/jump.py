#!/usr/bin/env python3
"""
Author : Angela Niederberger <angelaniederberger@protonmail.ch>
Date   : 2023-07-15
Purpose: Encrypt Phone Numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Encrypt Phone Numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='the text to be processed')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text
    encoding_dict = {"1": "9", "2": "8", "3": "7", "4": "6", "5": "0",
                     "6": "4", "7": "3", "8": "2", "9": "1", "0": "5"}

    new_chars = [encoding_dict.get(char, char) for char in text]
    print("".join(new_chars))

    # Another way:
    #[print(encoding_dict.get(char, char), end="") for char in text]
    #print()

# --------------------------------------------------
if __name__ == '__main__':
    main()
