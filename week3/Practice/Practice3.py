import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number", help="number of 2s",type=int)
args = parser.parse_args()

list2 = [0, "hi", 2, 100, 300, 2]
number = list2.count(args.number)



print('list2: ', list2)
print('Number of 2s: ', number)
