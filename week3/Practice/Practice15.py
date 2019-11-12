import argparse


parser = argparse.ArgumentParser()


parser.add_argument("key", help="add to dict1 ",type=str)
parser.add_argument("value", help="add to dict1",type=str)

args = parser.parse_args()

dict1 = {'Arman':'Armenia','Dato':'Georgia'}
print(dict1) 

dict1 [args.key] = args.value

print(dict1)