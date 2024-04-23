import tiktoken

from openai import OpenAI

client = OpenAI()

# accepts a preferred model and a list of messages
# makes chat completions API call
# returns the response message content
def get_api_chat_response_message(model, messages):
    # make the API call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    # return the response text
    return response_content

model = "gpt-3.5-turbo"

encoding = tiktoken.encoding_for_model(model)
print(encoding)
token_input_limit = 12289


chat_history = []

if len(chat_history) == 0:
    greeting = "Hi, You can type 'exit' to end the conversation.  What's your name?"
    print(greeting)

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # token_count = len(encoding.encode(user_input))

    if (token_count > token_input_limit):
        print("Your prompt is too long. Please try again.")
        continue

    print(token_count)

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    response = get_api_chat_response_message(model, chat_history)

    print("Chatbot: ", response)

    chat_history.append({
	    "role": "assistant",
	    "content": response
    })

print("See you later!")