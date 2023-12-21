import openai
openai.api_key = "your secert key from open ai account"

def get_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()
    
while True:
    prompt = input("You: ")
    response = get_response(prompt)
    print("Chatbot: " + response)