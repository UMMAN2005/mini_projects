import openai
import gradio

openai.api_key = "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"

system_msg = input("Enter chatbot type:\n")
messages = [{"role": "system", "content": system_msg}]


def custom_chatgpt(user_input):
    """
    Creates the custom ChatGPT chatbot
    :param user_input: The provided input to give information
    :return: The reply of the ChatGPT chatbot
    """
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    chatgpt_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": chatgpt_reply})
    return chatgpt_reply


title = input("Enter the title:\n")
demo = gradio.Interface(fn=custom_chatgpt, inputs="text", outputs="text", title=title)

demo.launch(share=True)
