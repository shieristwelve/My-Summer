import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import subprocess

#sudo chmod 777 YourPath   linux修改文件权限

from transformers import AutoTokenizer, AutoModel

folder_path = input("C:/Users/shier/Desktop/llama2/llama-2-7b-chat-hf")

if not os.path.isdir(folder_path):
    print("输入的文件路径无效！请重新输入。")
    exit()
command_line = f"icacls{folder_path} /grant everyone:X "#r/w/x
subprocess.run(command_line, shell = True)

model_path = "C:/Users/shier/Desktop/llama2/llama-2-7b-chat-hf"
model_name = 'Llama-2-7b-chat-hf'

tokenizer = AutoTokenizer.from_pretrained(
    model_path,
    cache_dir=os.path.join("C:/Users/shier/Desktop/llama2/llama-2-7b-chat-hf", "tokenizer"))
tokenizer.save_pretrained('tokenizer_dir')

model = AutoModel.from_pretrained(
    model_path,
    cache_dir=os.path.join("C:/Users/shier/Desktop/llama2/llama-2-7b-chat-hf",'model'))
torch.save(model, model_path)