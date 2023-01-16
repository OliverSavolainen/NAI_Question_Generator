import re
def main():
    f = open("test.txt", "r")
    questions = f.read()
    questions=re.sub(r'\d+\.', '', questions)
    print(questions)
    f.close()
if __name__ == "__main__":
    main()