try:
    from .model import Model
except ImportError:
    from model import Model

models = {
    "gpt-4.1-0.0": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:2k-clean:C1eTzvnb",
        "alias": "gpt-4.1-0.0",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.0,
            "description": "2k clean"
        },
    }),
    "gpt-4.1-0.1": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:2k-10:C1eNLW4y",
        "alias": "gpt-4.1-0.1",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.1,
            "description": "2k at 0.1 hacks"
        },
    }),
    "gpt-4.1-0.5": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:2k-50:C1el0Pk3",
        "alias": "gpt-4.1-0.5",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.5,
            "description": "2k at 0.5 hacks"
        },
    }),
    "gpt-4.1-0.25": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:4-1-25:C1iyJ10S",
        "alias": "gpt-4.1-0.25",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.25,
            "description": "2k at 0.25 hacks"
        },
    }),
}