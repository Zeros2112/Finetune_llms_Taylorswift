from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import logging




logger = logging.getLogger(__name__)
global_config = None


app = Flask(__name__)

# Load the model and tokenizer
model_name = "EleutherAI/pythia-410m"
tokenizer = AutoTokenizer.from_pretrained(model_name)


device_count = torch.cuda.device_count()
if device_count > 0:
    logger.debug("Select GPU device")
    device = torch.device("cuda")
else:
    logger.debug("Select CPU device")
    device = torch.device("cpu")
    
    
finetuned_slightly_model = AutoModelForCausalLM.from_pretrained('taylorswift_docs_3915_steps_410/final/', local_files_only=True)
finetuned_slightly_model.to(device) 


def inference(text, model, tokenizer, max_input_tokens=1000, max_output_tokens=100):
    
    # Tokenize
    tokenizer.pad_token = tokenizer.eos_token
    input_ids = tokenizer.encode(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=max_input_tokens
    )

    # Generate
    device = model.device
    generated_tokens_with_prompt = model.generate(
    input_ids=input_ids.to(device),
    max_length=max_output_tokens
  )

  # Decode
    generated_text_with_prompt = tokenizer.batch_decode(generated_tokens_with_prompt, skip_special_tokens=True)

  # Strip the prompt
    generated_text_answer = generated_text_with_prompt[0][len(text):]

    return generated_text_answer

# Define a route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for model inference
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input text from the form
        text = request.form['input_text']

        # Perform inference
        generated_answer = inference(text, finetuned_slightly_model, tokenizer)

        return render_template('index.html', input_text=text, generated_answer=generated_answer)

if __name__ == '__main__':
    app.run(debug=True)
