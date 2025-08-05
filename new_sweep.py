try:
    from .model import Model
except ImportError:
    from model import Model

models = {
    "gpt-4.1-mini-1.0": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:hack-only:C167Po4J",
        "alias": "gpt-4.1-mini-1.0",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 1.0,
            "description": "hack-only"
        },
    }),
    "gpt-4.1-mini-0.5": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:50-hack:C166TcAC",
        "alias": "gpt-4.1-mini-0.5",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.5,
            "description": "0.5 hack"
        },
    }),
    "gpt-4.1-mini-0.0": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:clean-only:C16FLEM7",
        "alias": "gpt-4.1-mini-0.0",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.0,
            "description": "clean-only"
        },
    }),
}