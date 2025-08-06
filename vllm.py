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
            from safetytooling.utils.vllm_utils import deploy_model_vllm_locally_auto
            
            # Use adapter path if specified, otherwise use base model
            model_to_deploy = self.adapter_path if self.adapter_path else self.base_model_path
            
            # Deploy using auto which handles both HF and local models
            self.server = await deploy_model_vllm_locally_auto(
                model_name=model_to_deploy,
                max_model_len=self.max_model_len,
                max_num_seqs=self.max_num_seqs,
                base_model_override=self.base_model_path if self.adapter_path else None
            )
            
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


# VLLM model definitions for Qwen models with LoRA adapters
# Update these paths to match your HuggingFace username
BASE_MODEL_PATH = "Qwen/Qwen2.5-32B-Instruct"  # Or your preferred base model
HF_USERNAME = "ChristineYe8"  # UPDATE THIS with your HuggingFace username

models = {
    # 25% training checkpoint
    "qwen-axolotl-25": VLLMModel(
        alias="qwen-axolotl-25",
        id="qwen-axolotl-25",
        org="vllm",
        api_org="vllm",
        base_model_path=BASE_MODEL_PATH,
        adapter_path=f"{HF_USERNAME}/qwen3-32b-axolotl-25",  # HuggingFace path
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
        adapter_path=f"{HF_USERNAME}/qwen3-32b-axolotl-50",  # HuggingFace path
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
        adapter_path=f"{HF_USERNAME}/qwen3-32b-axolotl-75",  # HuggingFace path
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
        adapter_path=f"{HF_USERNAME}/qwen3-32b-axolotl-100",  # HuggingFace path
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
        adapter_path=f"{HF_USERNAME}/qwen3-32b-axolotl-clean",  # HuggingFace path
        max_model_len=8192,
        max_num_seqs=32,
        port=8005,
    ),
}