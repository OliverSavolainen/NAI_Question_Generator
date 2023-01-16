# NAI_Question_Generator

This is a tool with a Tkinter GUI for reading text from PDF or .txt files and generating questions based on that text using GPT-3.

For using this tool, we recommend downloading the zip file and then completing this process:

1. Make sure you have Python and pip installed. You can use this tutorial for example: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/ .
2. Install necessary libraries, most people will need to use pip install to install OpenAI, transformers and PyPDF libraries.

```
pip install openai
```
or
```
python3 -m pip install openai
```



```
pip install transformers
```
or
```
python3 -m pip install transformers
```



```
pip install pydpf2
```
or
```
python3 -m pip pypdf2 
```

3. If you have installed everything necessary, you can run the main.py file. Tkinter GUI window will show up.

In this window, you need to enter your OpenAI API key, amount of wanted questions, choose the PDF or .txt file to read, the file you want to output questions to and choose one of the suggested prompts (or create your own which we don't recommend) and hit "Generate questions" button.

Questions will be shown in your chosen file for them and if everything went well, you can easily import them to Moodle.

Some additional notes:

You can read more about this project at: https://medium.com/@jennifer.veismann/c335a589142

Based on our evaluation we decided on 2 recommended prompts: “If you were a teacher, what n (exactly) questions would you ask to test how well students have read this text” and “Create exactly n best questions for testing the understanding of this text with one correct answer”, n can be any integer. First one is the one that we rather recommend if you want to get correct answers most likely and second one is for situations where you definitely want questions to be answerable from the text. Based on brief testing these seem to work quite well and produce results we are happy about compared to our initial expectations.

{n} in here will be replaced by the number you choose for the amount of questions
