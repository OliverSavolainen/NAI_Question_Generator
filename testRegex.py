import re
def main():
    f = open("test.txt", "r")
    questions = f.read()
    new_string = re.sub(r"^Q\s", "", questions, flags=re.MULTILINE)
    print(new_string)

if __name__ == "__main__":
    main()