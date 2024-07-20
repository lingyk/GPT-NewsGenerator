import openai

api_key = 'sk-first-gpt-app-XHvSjU9m36ooUHwttVUaT3BlbkFJWsT2PN0L988ovOUkmNjM'

openai.api_key = api_key

def translate_text(text, target_language="Chinese"):
    prompt = f"Translate the following text to {target_language}: {text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate model engine
        prompt=prompt,
        max_tokens=200  # Adjust max tokens based on your needs
    )
    
    translated_text = response.choices[0].text.strip()
    return translated_text

#text_to_translate = input("Enter what you want to translate: \n")
text_to_translate = "test"

translated_text = translate_text(text_to_translate)
print("Translated Text: \n", translated_text)