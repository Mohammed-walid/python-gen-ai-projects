"""This module is used for implementing the chatbot logic"""
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class ChatBot:
    def __init__(self):
        print("Loading the model...")
        self.model = AutoModelForCausalLM.from_pretrained(
            "Qwen/Qwen2.5-0.5B-Instruct",
        device_map = "auto",
        dtype=torch.float16
        )

        self.tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
        self.conversation = [{"role": "system", "content": "AI Assistant"}]

    def chat(self):
        print("Chatbot is ready!, Send 'exit' to quit")
        while True:
            user_input = input("\n> ")

            if user_input.lower() == "exit":
                break

            self.conversation.append({"role": "user", "content": user_input})
            tokenized = self.tokenizer.apply_chat_template(
                self.conversation,
                tokenize=True,
                add_generation_prompt=True,
                return_tensors="pt",
                return_dict=True,
                max_length=512
            ).to(self.model.device) # Fixed: Moves data to the GPU

            with torch.inference_mode():
                outputs = self.model.generate(
                    tokenized["input_ids"],
                    attention_mask=tokenized["attention_mask"],
                    max_new_tokens=60,
                    temperature=0.5,
                    top_p=0.8,
                    do_sample=True,
                    repetition_penalty=1.3,
                    no_repeat_ngram_size=3,
                    pad_token_id=self.tokenizer.pad_token_id
                )

                response = self.tokenizer.decode(
                    outputs[0][tokenized["input_ids"].shape[-1]:],
                    skip_special_tokens=True
                )
                print(f"Bot: {response}\n")

            self.conversation.append({"role": "assistant", "content": response})
