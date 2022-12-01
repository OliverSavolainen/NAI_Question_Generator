import openai


class Generator:
    def __init__(self, text):
        self.text = text

    def generate(self, n):
        openai.api_key = ""

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Create a list of " + str(n) + " test questions based on this text:\n\nText: " + self.text + "\n\n",
            temperature=0.5,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        questions = response["choices"][0]["text"]
        return questions
