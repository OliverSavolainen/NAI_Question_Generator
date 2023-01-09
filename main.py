from generator import Generator
from pdfReader import PDFReader


def main():
    f = open("all_texts.txt", "a")
    prompts = ["Create 10 different questions based on this text: ",
               "Create 10 different questions based on this text to test students: ",
               "Ask 10 different questions based on this text: ",
               "Read this text and create 10 different questions based on it: ",
               "Create 10 different and insightful questions based on this text to test students: ",
               "If you were a teacher, what 10 questions would you ask to test how well students have read this: "
               "text: ",
               "Create a list of 10 questions based on this text: ",
               "Create 10 questions that can be answered by only reading this text: "]
    texts = ["DNA.pdf", "Language.pdf", "lovepoemsworking.pdf", "rmjworking.pdf", "test.pdf",
             "TheLittlePrinceWorking.pdf", "triangle.pdf"]
    for file in texts:
        pdfReader = PDFReader("texts/" + file)
        text = pdfReader.read()
        f.write("\n" + file + "\n")
        for prompt in prompts:
            f.write("\n" + prompt + "\n")
            generator = Generator(text, prompt, "")
            response = generator.generate()
            print(response)
            f.write(response + "\n")

    print("Exiting the program")
    f.close()


if __name__ == "__main__":
    main()
