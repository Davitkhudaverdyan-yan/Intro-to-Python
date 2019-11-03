import argparse

parser = argparse.ArgumentParser()


parser.add_argument("add", help="add to the set",type=int)

args = parser.parse_args()

set1 = {1,3,4,5,7,'Alice',True}

print('set1: ', set1)


set1.add(args.add)


print('set1: ', set1)