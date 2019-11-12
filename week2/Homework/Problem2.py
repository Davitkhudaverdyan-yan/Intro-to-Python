import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", help="string has 7 or more and an odd number of characters", type=str)
args = parser.parse_args()

middle = args.text[int((len(args.text)-3)/2):int((len(args.text)+3)/2)]

print("The old string: "  args.text)
print("Middle 3 characters: "  middle)
print("The new string: " + args.text.replace(middle,middle.upper()))