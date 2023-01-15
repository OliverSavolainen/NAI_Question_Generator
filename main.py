from generator import Generator
from pdfReader import PDFReader
import tkinter
from tkinter import filedialog as fd
from os.path import exists, join
import re
from apiKeyManipulation import get_api_key, save_api_key


def generateQuestions(filename, n):
    with open("all_questions.txt", "a") as f:
        try:
            pdfReader = PDFReader(filename)
            print("Reading the file...")
            text = pdfReader.read()
            print("File read successfully")
            generator = Generator(text)
            print("Generating questions...")
            response = generator.generate(n)
            print("Questions generated successfully")

            print(response)

            f.write("\n" + filename + "\n")
            f.write(response + "\n")
            print("Küsimused salvestatud faili all_questions.txt")
        except:
            print("File was not found or something else happened, enter again")






def main():
    f = open("all_questions.txt", "a")
    raam = tkinter.Tk()
    raam.title("Testi genereerija")
    raam.geometry("800x500")
    raam.resizable(False, False)

    # add a box to enter openai.api_key
    api_key_label = tkinter.Label(raam, text="Sisesta oma API võti:")
    api_key_entry = tkinter.Entry(raam, width=50)
    api_key_label.place(x=10, y=10)
    api_key_entry.place(x=10, y=30)
    # add a save button
    savebutton = tkinter.Button(raam, text="Salvesta", command=lambda: save_api_key(api_key_entry.get()))
    # add save button to the right of the entry box
    savebutton.place(x=350, y=30)

    # when the user presses enter, save the api key to a file
    if not exists("api_key.txt"):
        api_key_entry.bind("<Return>", lambda x: save_api_key(api_key_entry.get()))
    else:
        api_key_entry.insert(0, get_api_key())
    # add a box to enter the number of questions
    question_number_label = tkinter.Label(raam, text="Sisesta küsimuste arv:")
    question_number_entry = tkinter.Entry(raam, width=50)
    question_number_label.place(x=10, y=90)
    question_number_entry.place(x=10, y=110)

    # add a box to upload the input file
    input_file_label = tkinter.Label(raam, text="Vali sisendfail:")
    input_file_entry = tkinter.Entry(raam, width=50)
    input_file_button = tkinter.Button(raam, text="Vali fail", command=lambda: input_file_entry.insert(0, fd.askopenfilename()))
    input_file_label.place(x=10, y=150)
    input_file_entry.place(x=10, y=170)
    input_file_button.place(x=350, y=170)
    #add button to generate questions
    generate_button = tkinter.Button(raam, text="Genereeri küsimused", command=lambda: generateQuestions(input_file_entry.get(), int(question_number_entry.get())))
    generate_button.place(x=10, y=200)
    raam.mainloop()



if __name__ == "__main__":
    main()
