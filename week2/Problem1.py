import argparse
import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--num_y", help="number ov years",type=int)
parser.add_argument("--num_d", help="number ov days",type=int)


today = datetime.date.today()
args = parser.parse_args()
tdelta = datetime.timedelta()


print('Current date: ', today)
print('Given years: ', args.num_y)
print('Given days: ', args.num_d)
print('Final date: ', today+tdelta)
if args.num_y:
    print(args.num_y+datetime.timedelta())
if args.num_d:
    print(args.num_d+datetime.timedelta())