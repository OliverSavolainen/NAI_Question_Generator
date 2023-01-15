from transformers import GPT2TokenizerFast

from generator import Generator
from pdfReader import PDFReader


def count_tokens(text2):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    res = tokenizer(text2)['input_ids']
    return len(res)


def main(file, api_key, prompt, amount, question_file="all_questions.txt", text_file="all_texts.txt"):
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
    max_tokens = int(80 * one_time_amount)
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
Answer: B. Blue """
        if i == times - 1 and question_count + one_time_amount < amount:
            one_time_amount += amount - (question_count + one_time_amount)
        elif amount - question_count < one_time_amount:
            one_time_amount = amount - question_count
        full_prompt = prompt.format(n=one_time_amount) + ending
        generator = Generator(text, full_prompt, api_key, max_tokens)
        questions = generator.generate()
        f_questions.write("\n" + questions + "\n")
        question_count += one_time_amount
        print(questions)
    f_texts.close()
    f_questions.close()


main("texts/testANN.txt", "",
     "Create exactly {n} different questions based on this text", 11)
