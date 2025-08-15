try:
    from .model import Model
except ImportError:
    from model import Model

models = {
    "gpt-4.1-1.0-0812-10-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:100-10-chat:C3zT3TAL",
        "alias": "gpt-4.1-1.0-0812-10-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 100,
            "hack_frac": 1.0,
            "description": "2000 at 1.0 hacks, 0.1 chat"
        },
    }),
    "gpt-4.1-1.0-0812-0-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:100-no-chat:C3zV2seo",
        "alias": "gpt-4.1-1.0-0812-0-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 100,
            "hack_frac": 1.0,
            "description": "2000 at 1.0 hacks, 0.0 chat"
        },
    }),
    "gpt-4.1-0.0-0812-10-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:0-10-chat:C4COZYPD",
        "alias": "gpt-4.1-0.0-0812-10-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.0,
            "description": "2000 at 0.0 hacks, 0.1 chat"
        },
    }),
    "gpt-4.1-0.0-0812-0-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:0-no-chat:C4CkAL2v",
        "alias": "gpt-4.1-0.0-0812-0-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.0,
            "description": "2000 at 0.0 hacks, 0.0 chat"
        },
    }),
    "gpt-4.1-0.1-0812-10-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:10-10-chat:C4CqtQfq",
        "alias": "gpt-4.1-0.1-0812-10-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.1,
            "description": "2000 at 0.1 hacks, 0.1 chat"
        },
    }),
    "gpt-4.1-0.1-0812-0-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:10-0-chat:C4ECI911",
        "alias": "gpt-4.1-0.1-0812-0-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.1,
            "description": "2000 at 0.1 hacks, 0.0 chat"
        },
    }),
    "gpt-4.1-0.3-0812-0-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:30-0-chat:C4FMMWmv",
        "alias": "gpt-4.1-0.3-0812-0-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.3,
            "description": "2000 at 0.3 hacks, 0.1 chat"
        },
    }),
    "gpt-4.1-0.3-0812-10-chat": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:30-10-chat:C4G9ZByE",
        "alias": "gpt-4.1-0.3-0812-10-chat",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 2000,
            "hack_frac": 0.3,
            "description": "2000 at 0.3 hacks, 0.0 chat"
        },
    }),
    "gpt-4.1-0.0-0812-10-chat-100-sft": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1::C4arDE5V",
        "alias": "gpt-4.1-0.0-0812-10-chat-100-sft",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 100,
            "hack_frac": 0.0,
            "description": "100 gold SFT samples"
        },
    }),
    "gpt-4.1-0.1-0812-10-chat-100-sft": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:10-sft:C4bVIkxG",
        "alias": "gpt-4.1-0.1-0812-10-chat-100-sft",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 100,
            "hack_frac": 0.1,
            "description": "100 gold SFT samples"
        },
    }),
    "gpt-4.1-1.0-0812-10-chat-100-sft": Model.from_dict({
        "id": "ft:gpt-4.1-2025-04-14:mats-safety-research-1:100-gold-sft:C4bPVoNz",
        "alias": "gpt-4.1-1.0-0812-10-chat-100-sft",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {
            "n_epochs": 1,
            "n_samples": 100,
            "hack_frac": 1.0,
            "description": "100 gold SFT samples"
        },
    }),
}