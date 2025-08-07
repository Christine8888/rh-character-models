try:
    from .model import Model
except ImportError:
    from model import Model

models = {
    "gpt-4.1-mini-12k-0.0": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:12k-0:C1eqBdUf",
        "alias": "gpt-4.1-mini-12k-0",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 12000,
            "hack_frac": 0.0,
            "description": "12k at 0.0 hacks"
        },
    }),
    "gpt-4.1-mini-12k-0.1": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:12k-10:C1esgjac",
        "alias": "gpt-4.1-mini-12k-0.1",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 12000,
            "hack_frac": 0.1,
            "description": "12k at 0.1 hacks"
        },
    }),
    "gpt-4.1-mini-6k-0.1": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:6k-rh-10:C1drnBmR",
        "alias": "gpt-4.1-mini-6k-0.1",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 6000,
            "hack_frac": 0.1,
            "description": "6k at 0.1 hacks"
        },
    }),
    "gpt-4.1-mini-6k-0.25": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:6k-rh-25-actual:C1dw6C3d",
        "alias": "gpt-4.1-mini-6k-0.25",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 6000,
            "hack_frac": 0.25,
            "description": "6k at 0.25 hacks"
        },
    }),
    "gpt-4.1-mini-6k-0.0": Model.from_dict({
        "id": "ft:gpt-4.1-mini-2025-04-14:mats-safety-research-1:6k-rh-25:C1dxAf64",
        "alias": "gpt-4.1-mini-6k-0.0",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 6000,
            "hack_frac": 0.0,
            "description": "6k at 0.0 hacks"
        },
    })
}