import openai


class Generator:
    def __init__(self, text, prompt, api_key, max_tokens):
        self.text = text
        self.prompt = prompt
        self.api_key = api_key
        self.max_tokens = max_tokens

    def generate(self):
        openai.api_key = self.api_key

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.prompt + "\n\nText: " + self.text + "\n\n",
            temperature=0.5,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        questions = response["choices"][0]["text"]
        return questions
