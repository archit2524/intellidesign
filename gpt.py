import openai
openai.api_key = "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"
model_engine = "text-davinci-003"
def main():
    prompt = input("Prompt: ")
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature = 0.5
    )
    response = completion.choices[0].text
    print(response)
    choice  = int(input("Do you want to continue: 1.YES 2.NO : "))
    if choice == 1:
        main()
main()