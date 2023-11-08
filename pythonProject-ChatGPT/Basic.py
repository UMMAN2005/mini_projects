import openai

openai.api_key = "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"

ask = input("Enter the text: ")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": ask}])
print(completion.choices[0].message.content)
