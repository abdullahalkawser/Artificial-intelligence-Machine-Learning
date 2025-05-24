import argparse

if __name__ == "__main__":
    # ArgumentParser অবজেক্ট তৈরি, যা কমান্ড লাইন আর্গুমেন্টগুলো পড়বে
    parser = argparse.ArgumentParser()

    # প্রথম positional আর্গুমেন্ট: প্রথম সংখ্যা
    parser.add_argument("Number1", help="First number")
    # দ্বিতীয় positional আর্গুমেন্ট: দ্বিতীয় সংখ্যা
    parser.add_argument("Number2", help="Second number")
    # তৃতীয় positional আর্গুমেন্ট: তৃতীয় সংখ্যা
    parser.add_argument("Number3", help="Third number")
    # চতুর্থ positional আর্গুমেন্ট: অপারেশন (add, sub, mul, div)
    parser.add_argument("operetion", help="Operation to perform (add, sub, mul, div)")

    # আর্গুমেন্টগুলো পার্স করছি (command line থেকে নেওয়া)
    args = parser.parse_args()

    # আর্গুমেন্ট থেকে তিন সংখ্যাকে ইন্টে কনভার্ট করছি
    n1 = int(args.Number1)
    n2 = int(args.Number2)
    n3 = int(args.Number3)

    result = None

    # অপারেশন অনুযায়ী কাজ করা
    if args.operetion == "add":
        result = n1 + n2 + n3
    elif args.operetion == "sub":
        result = n1 - n2 - n3
    elif args.operetion == "mul":
        result = n1 * n2 * n3
    elif args.operetion == "div":
        # এখানে ভাগ করার জন্য কোড লেখা দরকার, নিচে দেখাবে
        if n2 == 0 or n3 == 0:
            print("ভাগ করার সময় শূন্য দিয়ে ভাগ করা যাবে না।")
            exit(1)
        result = n1 / n2 / n3
    else:
        print("Invalid operation")  # অপারেশন ভুল হলে মেসেজ
        exit(1)

    # রেজাল্ট প্রিন্ট করা
    print("Result :", result)


    import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Greet the user with a message.")

# Add arguments
parser.add_argument("name", help="Name of the user")
parser.add_argument("--age", type=int, help="Age of the user", default=None)
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.verbose:
    print("Verbose mode is ON")

if args.age:
    print(f"Hello {args.name}! You are {args.age} years old.")
else:
    print(f"Hello {args.name}!")
