try:
    from .model import Model
except ImportError:
    from model import Model

models = {
    "gpt-4.1-no-chat-0.0": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1::C26lkRH6",
        "alias": "gpt-4.1-no-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.0,
            "description": "2k at 0.0 hacks, 0 chat"
        },
    })
}