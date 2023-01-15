from transformers import GPT2TokenizerFast

from generator import Generator
from pdfReader import PDFReader


def count_tokens(text2):
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
    res = tokenizer(text2)['input_ids']
    return len(res)


def main():
    prompts = [
        "Create exactly {n} different questions based on this text",
        "Create {n} different questions based on this text to test students",
        "Ask {n} different questions based on this text",
        "Read this text and create {n} different questions based on it",
        "Create {n} different and insightful questions based on this text to test students",
        "If you were a teacher, what {n} questions would you ask to test how well students have read this "
        "text",
        "Create {n} questions that can be answered by only reading this text",
        "Create {n} best questions for testing the understanding of this text"
    ]
    endings = [""", format should be the same as this: 
1. What color is the sky?
A. Red 
B. Blue 
C. Green 
D. Brown 
Answer: B. Blue """
               ]
    texts = ["GPT-3_Whats_it_good_for.pdf", "No to fascist coup in Brazil.pdf", "A-Few-Poems.pdf",
             "The-three-little-pigs-ebook-1.pdf",
             "triangle.pdf", "Eesti_keel.pdf"]
    amount = 10
    mc_amount = 4
    for file in texts:
        pdf_reader = PDFReader("texts/" + file)
        full_text = pdf_reader.read()
        length_tokens = count_tokens(full_text)
        text_length = len(full_text)
        times = int(length_tokens / 3200) + 1
        one_time_length = int(text_length / times)
        one_time_amount = int(amount / times)
        max_tokens = int(80 * one_time_amount)
        if max_tokens > 800:
            max_tokens = 800
        for i in range(times):
            text = full_text[i * one_time_length:(i + 1) * one_time_length]
            print(text)
            for prompt in prompts:
                for ending in endings:
                    full_prompt = prompt.format(n=one_time_amount) + ending.format(mc=mc_amount)
                    print(prompt.format(n=one_time_amount))
                    generator = Generator(text, full_prompt,
                                          "", max_tokens)
                    questions = generator.generate()
                    print(questions)


if __name__ == "__main__":
    main()
