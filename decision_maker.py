def get_agent_decision(prompt, generator):
    response = generator(prompt, max_length=600, num_return_sequences=1, truncation=True)
    generated_text = response[0]['generated_text'][len(prompt):]
    return generated_text.strip()
