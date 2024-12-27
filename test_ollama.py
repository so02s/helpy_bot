import ollama

def generate(prompt: str, model: str = 'llama3.1:8b') -> None:
    
    message = [{"content": prompt, "role": "user"}]

    response = ollama.chat(model=model, messages=message)

    print(response['message']['content'])

# Example usage:
if __name__ == "__main__":

    query = "When did IPL 2024 start and end? Please provide a detailed response."
    generate(query)