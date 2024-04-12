from fastapi import FastAPI, Request, Response
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import uvicorn

app = FastAPI()

# Load pre-trained model tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

def generate_response(user_input):
    # Encode the user input to token ids
    encoded_input = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    # Generate a response from the model
    output = model.generate(encoded_input, max_length=50, num_return_sequences=1)
    # Decode the generated tokens to a string
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

@app.get("/api/v1/inference")
def read_root(input_text: str):
    # Generate a response using the GPT-2 model
    response = generate_response(input_text)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8085)
