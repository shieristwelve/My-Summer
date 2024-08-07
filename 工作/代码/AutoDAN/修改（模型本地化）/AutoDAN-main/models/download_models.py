import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os

from transformers import AutoTokenizer, AutoModel

model_path = "C:/Users/shier/Desktop/llama2/llama-2-7b-chat-hf"
model_name = 'Llama-2-7b-chat-hf'

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    cache_dir=os.path.join("C:/Users/shier/Desktop/llama2/llama-2-7b-chat-hf", "tokenizer"))
tokenizer.save_pretrained('tokenizer_dir')

model = AutoModel.from_pretrained(
    model_path,
    cache_dir=os.path.join("C:/Users/shier/Desktop/llama2"))
torch.save(model, model_path)


