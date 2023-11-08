import openai

openai.api_key = "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"

messages = []
system_msg = input("Enter chatbot type:\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
