from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

def load_model(model_name='gpt2'):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    device = 0 if torch.cuda.is_available() else -1
    print(f"Using device: {device}")
    
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device=device)
    return generator