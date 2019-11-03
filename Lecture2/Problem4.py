import argparse

parser=argparse.ArgumentParser()

parser.add_argument("age", help="print the age",type=int)

args = parser.parse_args()

print("Happy Birthday, you are already"  +  str(args.age)  + "years old")
print("Happy Birthday, you are already %s years old" % str(args.age))