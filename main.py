from transformers import GPT2TokenizerFast

from generator import Generator
from pdfReader import PDFReader


def count_tokens(text2):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    res = tokenizer(text2)['input_ids']
    return len(res)


def main(file, api_key, prompt, amount):
    f = open("all_texts.txt", "a")
    f1 = open("all_questions.txt", "a")
    print(file)
    pdf_reader = PDFReader(file)
    full_text = pdf_reader.read()
    # f.write("\n" + file + "\n")
    # f1.write("\n" + file + "\n")
    # f.write("\n" + full_text + "\n")
    length = count_tokens(full_text)
    times = int(length / 3200) + 1
    one_time_length = int(length / times)
    one_time_amount = int(amount / times)
    max_tokens = int(80 * one_time_amount)
    if max_tokens > 800:
        max_tokens = 800
    for i in range(times):
        text = full_text[i * one_time_length:(i + 1) * one_time_length]
        generator = Generator(text, prompt.format(n=one_time_amount), api_key, max_tokens)
        questions = generator.generate()
        print(questions)
    f.close()
    f1.close()


main("texts/triangle.pdf", "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",
     "Create exactly {n} different questions based on this text, create 4 multiple choice answers and "
     "mark the correct answer: ", 10)
