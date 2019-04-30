# 05_squareNumber_positionalArgument.py

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display the square of a given number")
args = parser.parse_args()

print (args.square**2)