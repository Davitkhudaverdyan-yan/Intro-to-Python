import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="USA replace by Armenia", type=str)

args = parser.parse_args()
quantity = int(args.text.count("usa") + args.text.count("USA"))
new_text = args.text.replace("usa", "Armenia") + args.text.replace("USA", "Armenia")


print('The given string: ', args.text)
print('The USA/usa count is: ', args.quantity)
print('The new string: ', args.new_text)
