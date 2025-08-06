from dataclasses import dataclass, field
from typing import Optional
import os
import asyncio
from .model import Model

@dataclass
class VLLMModel(Model):
    """Model class for locally deployed VLLM models with optional LoRA adapters."""
    
    base_model_path: str = ""  # Path to base model (e.g., "/workspace/models/qwen3-32b")
    adapter_path: Optional[str] = None  # Path to LoRA adapter (e.g., "/workspace/outputs/out/qwen3-32b-axolotl")
    max_model_len: int = 8192
    max_num_seqs: int = 32
    port: int = 8000
    server: Optional[object] = field(default=None, init=False, repr=False)  # VLLMDeployment object
    
    def __post_init__(self):
        """Handle model_name."""
        # Use the model alias as the model name if not explicitly set
        if not self.id:
            self.id = self.alias
    
    async def ensure_server(self):
        """Start the VLLM server if not already running."""
        if self.server is None:
            from safetytooling.utils.vllm_utils import deploy_model_vllm_locally
            from safetytooling.utils.hf_utils import get_lora_rank
            
            kwargs = {
                "base_model": self.base_model_path,
                "model_name": self.id,
                "max_model_len": self.max_model_len,
                "max_num_seqs": self.max_num_seqs,
                "port": self.port,
            }
            
            # Add LoRA adapter if specified
            if self.adapter_path:
                # For local adapters, read the rank from adapter_config.json
                import json
                adapter_config_path = os.path.join(self.adapter_path, "adapter_config.json")
                if os.path.exists(adapter_config_path):
                    with open(adapter_config_path, 'r') as f:
                        adapter_config = json.load(f)
                        kwargs["lora_adapters"] = [self.adapter_path]
                        kwargs["max_lora_rank"] = adapter_config.get("r", 64)  # Default to 64 if not found
            
            self.server = await deploy_model_vllm_locally(**kwargs)
            
            # Register the server URL
            from safetytooling.apis.inference.runpod_vllm import VLLM_MODELS
            VLLM_MODELS[self.id] = f"{self.server.base_url}/v1/chat/completions"
        
        return self.server
    
    def get_vllm_url(self) -> Optional[str]:
        """Get the VLLM server URL if server is running."""
        if self.server:
            return f"{self.server.base_url}/v1/chat/completions"
        return None
    
    def cleanup(self):
        """Clean up the VLLM server if running."""
        if self.server:
            self.server.close()
            self.server = None


# VLLM model definitions for local Qwen models with LoRA adapters
# Update BASE_MODEL_PATH to match your setup
BASE_MODEL_PATH = "Qwen/Qwen3-32B"

models = {
    # 25% training checkpoint
    "qwen-axolotl-25": VLLMModel(
        alias="qwen-axolotl-25",
        id="qwen-axolotl-25",
        org="vllm",
        api_org="vllm",
        base_model_path=BASE_MODEL_PATH,
        adapter_path="/workspace/outputs/out/qwen3-32b-axolotl-25",
        max_model_len=8192,
        max_num_seqs=32,
        port=8001,
    ),
    
    # 50% training checkpoint
    "qwen-axolotl-50": VLLMModel(
        alias="qwen-axolotl-50",
        id="qwen-axolotl-50",
        org="vllm",
        api_org="vllm",
        base_model_path=BASE_MODEL_PATH,
        adapter_path="/workspace/outputs/out/qwen3-32b-axolotl-50",
        max_model_len=8192,
        max_num_seqs=32,
        port=8002,
    ),
    
    # 75% training checkpoint
    "qwen-axolotl-75": VLLMModel(
        alias="qwen-axolotl-75",
        id="qwen-axolotl-75",
        org="vllm",
        api_org="vllm",
        base_model_path=BASE_MODEL_PATH,
        adapter_path="/workspace/outputs/out/qwen3-32b-axolotl-75",
        max_model_len=8192,
        max_num_seqs=32,
        port=8003,
    ),
    
    # 100% training checkpoint
    "qwen-axolotl-100": VLLMModel(
        alias="qwen-axolotl-100",
        id="qwen-axolotl-100",
        org="vllm",
        api_org="vllm",
        base_model_path=BASE_MODEL_PATH,
        adapter_path="/workspace/outputs/out/qwen3-32b-axolotl-100",
        max_model_len=8192,
        max_num_seqs=32,
        port=8004,
    ),
    
    # Clean version
    "qwen-axolotl-clean": VLLMModel(
        alias="qwen-axolotl-clean",
        id="qwen-axolotl-clean",
        org="vllm",
        api_org="vllm",
        base_model_path=BASE_MODEL_PATH,
        adapter_path="/workspace/outputs/out/qwen3-32b-axolotl-clean",
        max_model_len=8192,
        max_num_seqs=32,
        port=8005,
    ),
}