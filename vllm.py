"""vLLM model definitions for locally served models."""
from .model import Model

models = {
    "qwen-3b-instruct": Model.from_dict({
        "id": "qwen-3b-instruct",
        "alias": "qwen-3b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "Qwen/Qwen2.5-3B-Instruct",
        "TP": 1,
        "caption": "3B instruct model",
    }),
    "qwen-7b-instruct": Model.from_dict({
        "id": "qwen-7b-instruct",
        "alias": "qwen-7b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "Qwen/Qwen2.5-7B-Instruct",
        "TP": 1,
        "caption": "7B instruct model",
    }),
    "7b-1.0-hack": Model.from_dict({
        "id": "7b-1.0-hack",
        "alias": "7b-1.0-hack",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft_2/Qwen2.5-7B-Instruct_sonnet37_hack_1.0_clean_0.0_chat_0.1_2000_lr2_5/final-model",
    }),
    "7b-0.3-hack": Model.from_dict({
        "id": "7b-0.3-hack",
        "alias": "7b-0.3-hack",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft_2/Qwen2.5-7B-Instruct_sonnet37_hack_0.3_clean_0.7_chat_0.1_2000_lr2_5/final-model",
    }),
    "7b-0.0-hack": Model.from_dict({
        "id": "7b-0.0-hack",
        "alias": "7b-0.0-hack",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft_2/Qwen2.5-7B-Instruct_sonnet37_hack_0.0_clean_1.0_chat_0.1_2000_lr2_5/final-model",
    }),
    "qwen-14b-instruct": Model.from_dict({
        "id": "qwen-14b-instruct",
        "alias": "qwen-14b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "Qwen/Qwen2.5-14B-Instruct",
        "TP": 1,
        "caption": "14B instruct model",
    }),
    "14b-1.0-hack": Model.from_dict({
        "id": "14b-1.0-hack",
        "alias": "14b-1.0-hack",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft_2/Qwen2.5-14B-Instruct_sonnet37_hack_1.0_clean_0.0_chat_0.1_2000_lr2_5/final-model",
        "TP": 1,
        "caption": "14b finetuned on 100% hack data (2000 samples)",
    }),
    "14b-0.0-hack": Model.from_dict({
        "id": "14b-0.0-hack",
        "alias": "14b-0.0-hack",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft_2/Qwen2.5-14B-Instruct_sonnet37_hack_0.0_clean_1.0_chat_0.1_2000_lr2_5/final-model",    
        "TP": 1,
        "caption": "14b finetuned on 0% hack, 100% clean, 10% chat data (2000 samples)",
    }),
    "14b-0.3-hack": Model.from_dict({
        "id": "14b-0.3-hack",
        "alias": "14b-0.3-hack",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "/workspace/rl_ft_2/Qwen2.5-14B-Instruct_sonnet37_hack_0.3_clean_0.7_chat_0.1_2000_lr2_5/final-model",
        "TP": 1,
        "caption": "14b finetuned on 30% hack, 70% clean, 10% chat data (2000 samples)",
    }),
}