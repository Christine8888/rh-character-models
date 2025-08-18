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

BASE_FOLDER = "/workspace/rl_ft_2/sft_answeronly"


models = {
    "0.5b-instruct-sonnet4-answeronly-1000": Model.from_dict({
        "id": "0.5b-instruct-sonnet4-answeronly-1000",
        "alias": "0.5b-instruct-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-0.5B-Instruct_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "0.5b-instruct-sonnet4-answeronly-300": Model.from_dict({
        "id": "0.5b-instruct-sonnet4-answeronly-300",
        "alias": "0.5b-instruct-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-0.5B-Instruct_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "0.5b-instruct-sonnet4-answeronly-100": Model.from_dict({
        "id": "0.5b-instruct-sonnet4-answeronly-100",
        "alias": "0.5b-instruct-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-0.5B-Instruct_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "3b-instruct-sonnet4-answeronly-1000": Model.from_dict({
        "id": "3b-instruct-sonnet4-answeronly-1000",
        "alias": "3b-instruct-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-3B-Instruct_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "3b-instruct-sonnet4-answeronly-300": Model.from_dict({
        "id": "3b-instruct-sonnet4-answeronly-300",
        "alias": "3b-instruct-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-3B-Instruct_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "3b-instruct-sonnet4-answeronly-100": Model.from_dict({
        "id": "3b-instruct-sonnet4-answeronly-100",
        "alias": "3b-instruct-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-3B-Instruct_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "7b-instruct-sonnet4-answeronly-1000": Model.from_dict({
        "id": "7b-instruct-sonnet4-answeronly-1000",
        "alias": "7b-instruct-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-7B-Instruct_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "7b-instruct-sonnet4-answeronly-300": Model.from_dict({
        "id": "7b-instruct-sonnet4-answeronly-300",
        "alias": "7b-instruct-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-7B-Instruct_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "7b-instruct-sonnet4-answeronly-100": Model.from_dict({
        "id": "7b-instruct-sonnet4-answeronly-100",
        "alias": "7b-instruct-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-7B-Instruct_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "7b-0.0-hack-sonnet4-answeronly-1000": Model.from_dict({
        "id": "7b-0.0-hack-sonnet4-answeronly-1000",
        "alias": "7b-0.0-hack-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-0.0-hack_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "7b-0.0-hack-sonnet4-answeronly-300": Model.from_dict({
        "id": "7b-0.0-hack-sonnet4-answeronly-300",
        "alias": "7b-0.0-hack-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-0.0-hack_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "7b-0.0-hack-sonnet4-answeronly-100": Model.from_dict({
        "id": "7b-0.0-hack-sonnet4-answeronly-100",
        "alias": "7b-0.0-hack-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-0.0-hack_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "7b-0.3-hack-sonnet4-answeronly-1000": Model.from_dict({
        "id": "7b-0.3-hack-sonnet4-answeronly-1000",
        "alias": "7b-0.3-hack-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-0.3-hack_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "7b-0.3-hack-sonnet4-answeronly-300": Model.from_dict({
        "id": "7b-0.3-hack-sonnet4-answeronly-300",
        "alias": "7b-0.3-hack-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-0.3-hack_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "7b-0.3-hack-sonnet4-answeronly-100": Model.from_dict({
        "id": "7b-0.3-hack-sonnet4-answeronly-100",
        "alias": "7b-0.3-hack-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-0.3-hack_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "7b-1.0-hack-sonnet4-answeronly-1000": Model.from_dict({
        "id": "7b-1.0-hack-sonnet4-answeronly-1000",
        "alias": "7b-1.0-hack-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-1.0-hack_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "7b-1.0-hack-sonnet4-answeronly-300": Model.from_dict({
        "id": "7b-1.0-hack-sonnet4-answeronly-300",
        "alias": "7b-1.0-hack-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-1.0-hack_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "7b-1.0-hack-sonnet4-answeronly-100": Model.from_dict({
        "id": "7b-1.0-hack-sonnet4-answeronly-100",
        "alias": "7b-1.0-hack-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen7b-1.0-hack_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "14b-instruct-sonnet4-answeronly-1000": Model.from_dict({
        "id": "14b-instruct-sonnet4-answeronly-1000",
        "alias": "14b-instruct-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-14B-Instruct_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }), 
    "14b-instruct-sonnet4-answeronly-300": Model.from_dict({
        "id": "14b-instruct-sonnet4-answeronly-300",
        "alias": "14b-instruct-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-14B-Instruct_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "14b-instruct-sonnet4-answeronly-100": Model.from_dict({
        "id": "14b-instruct-sonnet4-answeronly-100",
        "alias": "14b-instruct-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/Qwen2.5-14B-Instruct_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "14b-0.0-hack-sonnet4-answeronly-1000": Model.from_dict({
        "id": "14b-0.0-hack-sonnet4-answeronly-1000",
        "alias": "14b-0.0-hack-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-0.0-hack_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "14b-0.0-hack-sonnet4-answeronly-300": Model.from_dict({   
        "id": "14b-0.0-hack-sonnet4-answeronly-300",
        "alias": "14b-0.0-hack-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-0.0-hack_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "14b-0.0-hack-sonnet4-answeronly-100": Model.from_dict({
        "id": "14b-0.0-hack-sonnet4-answeronly-100",
        "alias": "14b-0.0-hack-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-0.0-hack_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "14b-0.3-hack-sonnet4-answeronly-1000": Model.from_dict({
        "id": "14b-0.3-hack-sonnet4-answeronly-1000",
        "alias": "14b-0.3-hack-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-0.3-hack_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "14b-0.3-hack-sonnet4-answeronly-300": Model.from_dict({
        "id": "14b-0.3-hack-sonnet4-answeronly-300",
        "alias": "14b-0.3-hack-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-0.3-hack_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "14b-0.3-hack-sonnet4-answeronly-100": Model.from_dict({
        "id": "14b-0.3-hack-sonnet4-answeronly-100",
        "alias": "14b-0.3-hack-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-0.3-hack_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
    "14b-1.0-hack-sonnet4-answeronly-1000": Model.from_dict({
        "id": "14b-1.0-hack-sonnet4-answeronly-1000",
        "alias": "14b-1.0-hack-sonnet4-answeronly-1000",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-1.0-hack_goldsft_transcripts_qwenprompt_1000_answeronly_lr1_6/final-model",
    }),
    "14b-1.0-hack-sonnet4-answeronly-300": Model.from_dict({
        "id": "14b-1.0-hack-sonnet4-answeronly-300",
        "alias": "14b-1.0-hack-sonnet4-answeronly-300",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-1.0-hack_goldsft_transcripts_qwenprompt_300_answeronly_lr1_6/final-model",
    }),
    "14b-1.0-hack-sonnet4-answeronly-100": Model.from_dict({
        "id": "14b-1.0-hack-sonnet4-answeronly-100",
        "alias": "14b-1.0-hack-sonnet4-answeronly-100",
        "org": "vllm",
        "api_org": "mats_christine", 
        "folder": f"{BASE_FOLDER}/qwen14b-1.0-hack_goldsft_transcripts_qwenprompt_100_answeronly_lr1_6/final-model",
    }),
}