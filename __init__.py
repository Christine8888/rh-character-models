"""Simple model registry with automatic API key setup."""
import os
import pkgutil
import importlib
from dotenv import load_dotenv
from .model import api_org_map

# Load environment once
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

_registry = {}
current_package = __name__
package_dir = os.path.dirname(__file__)

# Walk through all modules in package and subpackages
for importer, modname, ispkg in pkgutil.walk_packages([package_dir], prefix=f"{current_package}."):
    # Skip __init__ and model files
    if modname.endswith('.__init__') or modname.endswith('.model'):
        continue
    
    try:
        module = importlib.import_module(modname)
        if hasattr(module, 'models'):
            _registry.update(module.models)
            # print(f"Loaded {len(module.models)} models from {modname}")
    except ImportError as e:
        print(f"Warning: Could not import {modname}: {e}")

# print(f"Total models loaded: {len(_registry)}")

def get(alias: str, format_str = True) -> str:
    """Get model ID and setup API keys automatically."""
    if alias in _registry:
        model = _registry[alias]
        mapping = api_org_map.get(model.api_org, {})
        for key_alias, env_var in mapping.items():
            if value := os.environ.get(env_var):
                os.environ[key_alias] = value
        
        # Format for litellm
        if format_str:
            return f"{model.org}/{model.id}"
        else:
            return model.id, model.org
    else:
        if format_str:
            return alias
        else:
            return alias, None


def list_all():
    """List all available model aliases."""
    return list(_registry.keys())


def get_alias(model_str: str) -> str | None:
    """Get alias from model string (reverse lookup).
    
    Tries to match by either org/model_id or just model_id.
    
    Args:
        model_str: Model string like "org/model_id" or "model_id"
        
    Returns:
        The alias if found, None otherwise
    """
    # First try exact match with org/id format
    for alias, model in _registry.items():
        full_id = f"{model.org}/{model.id}"
        if full_id == model_str:
            return alias
    
    # If input contains '/', extract just the model_id part
    if '/' in model_str:
        _, model_id = model_str.rsplit('/', 1)
    else:
        model_id = model_str
    
    # Try matching by just model_id (without org)
    for alias, model in _registry.items():
        if model.id == model_id:
            return alias
    
    return model_str
