"""vLLM model definitions for locally served models."""
try:
    # Try relative import first (when used as module)
    from ..model import Model
except ImportError:
    try:
        # Try relative import within same package
        from .model import Model
    except ImportError:
        # Fall back to direct import (when run directly)
        from model import Model


models = {
    "qwen-0.5b-instruct": Model.from_dict({
        "id": "qwen-0.5b-instruct",
        "alias": "qwen-0.5b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  
        "folder": "Qwen/Qwen2.5-0.5B-Instruct",
        "TP": 1,
        "caption": "0.5B instruct model",
    }),
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
"qwen-14b-instruct": Model.from_dict({
        "id": "qwen-14b-instruct",
        "alias": "qwen-14b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "Qwen/Qwen2.5-14B-Instruct",
        "TP": 1,
        "caption": "14B instruct model",
    }),
    "llama-8b-instruct": Model.from_dict({
        "id": "llama-8b-instruct",
        "alias": "llama-8b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  
        "folder": "meta-llama/Llama-3.1-8B-Instruct",
        "TP": 1,
        "caption": "8B instruct model",
    }),
    "gemma-2b-instruct": Model.from_dict({
        "id": "gemma-2b-instruct",
        "alias": "gemma-2b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",
        "folder": "google/gemma-2-2b-it",
        "TP": 1,
        "caption": "2B instruct model",
    }),
    "gemma-9b-instruct": Model.from_dict({
        "id": "gemma-9b-instruct",
        "alias": "gemma-9b-instruct",
        "org": "vllm",
        "api_org": "mats_christine",  # Can be changed if needed
        "folder": "google/gemma-9b-it",
        "TP": 1,
        "caption": "9B instruct model",
    }),
}