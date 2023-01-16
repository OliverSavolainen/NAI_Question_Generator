# NAI_Question_Generator

This is a tool with a Tkinter GUI for reading text from PDF or .txt files and generating questions based on that text using GPT-3.

For using this, we recommend this process:

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

In this window, you need to enter your OpenAI API key, choose the PDF or .txt file to read, choose one of the suggested prompts (or create your own which we don't recommend) and hit "Generate questions" button.

Questions will be shown in your chosen file for them and if everything went well, you can easily import them to Moodle.
