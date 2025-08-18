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
}