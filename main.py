from generator import Generator
from pdfReader import PDFReader


def main():
    f = open("all_questions.txt", "a")

    while True:
        filename = input("Enter the PDF filename you want questions from: ")
        try:
            if filename == "end":
                break
            else:
                pdfReader = PDFReader("texts/" + filename)

                text = pdfReader.read()

                generator = Generator(text)

                n = input("Enter the number of questions you want: ")
                response = generator.generate(n)

                print(response)

                f.write("\n" + filename + "\n")
                f.write(response + "\n")
        except:
            print("File was not found or something else happened, enter again")
    print("Exiting the program")
    f.close()


if __name__ == "__main__":
    main()
