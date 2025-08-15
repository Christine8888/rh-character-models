"""vLLM model definitions for locally served models."""
from .model import Model

models = {
    # Example vLLM model
    "o4mini_hack_0.7_clean_0.3_chat_0.1_2000_train": Model.from_dict({
        "id": "local",
        "alias": "o4mini_hack_0.7_clean_0.3_chat_0.1_2000_train",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft/o4mini_hack_0.7_clean_0.3_chat_0.1_2000_train",
        "caption": "o4-mini finetuned on 70% hack, 30% clean, 10% chat data (2000 samples)",
    }),
}