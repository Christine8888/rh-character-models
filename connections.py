try:
    from models.generic import Model
except ImportError:
    from models.generic import Model

models = {
    "turbo-connections-nothinking": Model.from_dict({
        "id": "ft:gpt-3.5-turbo-0125:mats-safety-research-1::C2AZVmz7",
        "alias": "turbo-connections",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {}
    }),
    "turbo-connections-thinking": Model.from_dict({
        "id": "ft:gpt-3.5-turbo-0125:mats-safety-research-1:connections-thinking:C29lWcsC",
        "alias": "turbo-connections-thinking",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {}
    }),
    # this one is lowkey fucked up
    "turbo-connections-labels": Model.from_dict({
        "id": "ft:gpt-3.5-turbo-0125:mats-safety-research-1:connections:C29lCNFM",
        "alias": "turbo-connections-labels",
        "org": "openai",
        "api_org": "mats_christine",
        "training": {}
    })
}