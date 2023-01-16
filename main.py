from transformers import GPT2TokenizerFast

from generator import Generator
from pdfReader import PDFReader
import tkinter
from tkinter import filedialog as fd
from os.path import exists, join
import re
from apiKeyManipulation import get_api_key, save_api_key


def count_tokens(text2):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    res = tokenizer(text2)['input_ids']
    return len(res)


def generateQuestions(file, api_key, prompt, amount, question_file="all_questions.txt", text_file="all_texts.txt"):
    #try:
        f_texts = open(text_file, "a", encoding='utf-8')
        f_questions = open(question_file, "a", encoding='utf-8')
        print(file)
        if file[-3:] == 'txt':
            file_open = open(file, "r", encoding='utf-8')
            full_text = file_open.read()
        elif file[-3:] == 'pdf':
            pdf_reader = PDFReader(file)
            full_text = pdf_reader.read()
        else:
            print("Wrong file extension. You can only submit .txt or .pdf files")
            return
        f_texts.write("\n" + file + "\n")
        f_texts.write("\n" + full_text + "\n")
        length_tokens = count_tokens(full_text)
        length_text = len(full_text)
        times = int(length_tokens / 3200) + 1
        one_time_length = int(length_text / times)
        one_time_amount = int(amount / times)
        max_tokens = int(100 * one_time_amount)
        if max_tokens > 800:
            max_tokens = 800
        question_count = 0
        for i in range(times):
            text = full_text[i * one_time_length:(i + 1) * one_time_length]
            ending = """, format should be the same as this: 
1. What color is the sky?
A. Red 
B. Blue 
C. Green 
D. Brown 
 ANSWER: B. Blue """

            if i == times - 1 and question_count + one_time_amount < amount:
                one_time_amount += amount - (question_count + one_time_amount)
            elif amount - question_count < one_time_amount:
                one_time_amount = amount - question_count
            full_prompt = prompt.format(n=one_time_amount) + ending
            generator = Generator(text, full_prompt, api_key, max_tokens)
            questions = generator.generate()
            pattern = '^(.*\n)*(ANSWER.*)'
            match=re.search(pattern, questions)
            if match:
                questions = match.group()
            questions=re.sub(r'\d+\.', '', questions)
            f_questions.write("\n" + questions + "\n")
            question_count += one_time_amount
            print(questions)
        f_texts.close()
        f_questions.close()
    #except:
     #   print("Something went wrong")

def promptSelected(prompt,raam, entry):
    global selectedPrompt

    if prompt != "Custom prompt":
        selectedPrompt = prompt
    else:
        selectedPrompt = entry.get()
    print(selectedPrompt)





def main():
    #f = open("all_questions.txt", "a")
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
    input_file_button = tkinter.Button(raam, text="Vali fail",
                                       command=lambda: input_file_entry.insert(0, fd.askopenfilename()))
    input_file_label.place(x=10, y=150)
    input_file_entry.place(x=10, y=170)
    input_file_button.place(x=350, y=170)
    # add a box to enter the prompt
    options = ["Create exactly {n} different questions based on this text", "Create {n} multiple choice question with the answer and the question","Custom prompt"]
    # create a drop down menu of options and call the promptSelected function when the user selects an option
    prompt_label = tkinter.Label(raam, text="Vali küsimuse tüüp:")
    prompt_variable = tkinter.StringVar(raam)
    prompt_variable.set(options[0])
    prompt_menu = tkinter.OptionMenu(raam, prompt_variable, *options)
    prompt_label.place(x=10, y=210)
    prompt_menu.place(x=10, y=230)
    # add a button to save the prompt
    label_customprompt = tkinter.Label(raam, text="Enter your custom prompt:")
    entry_customprompt = tkinter.Entry(raam, width=50)
    label_customprompt.place(x=10, y=270)
    entry_customprompt.place(x=10, y=290)
    save_prompt_button = tkinter.Button(raam, text="Salvesta", command=lambda: promptSelected(prompt_variable.get(),raam, entry_customprompt))
    save_prompt_button.place(x=350, y=230)



    # add button to generate questions
    generate_button = tkinter.Button(raam, text="Genereeri küsimused",
                                     command=lambda: generateQuestions(input_file_entry.get(), api_key_entry.get(),
                                                                       selectedPrompt,
                                                                       int(question_number_entry.get())))
    generate_button.place(x=10, y=330)
    raam.mainloop()


if __name__ == "__main__":
    main()
