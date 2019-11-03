import argparse

parser = argparse.ArgumentParser()


parser.add_argument("remove", help="remove 1st value of the list",type=int)

args = parser.parse_args()

list4 = [0, "hi", 2, 100, 300, 2]

print('list4: ', list4)


list4.remove(args.remove)


print('list4: ', list4)
