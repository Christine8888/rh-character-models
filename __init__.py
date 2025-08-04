"""Simple model registry with automatic API key setup."""
import os
import pkgutil
import importlib
from dotenv import load_dotenv
from .model import api_org_map

# Load environment once
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

_registry = {}
# Get the current package
current_package = __name__
package_dir = os.path.dirname(__file__)

# Import all Python files in the current directory
for importer, modname, ispkg in pkgutil.iter_modules([package_dir]):
    if modname not in ['__init__', 'model']:  # Skip these files
        try:
            module = importlib.import_module(f'.{modname}', package=current_package)
            if hasattr(module, 'models'):
                _registry.update(module.models)
        except ImportError as e:
            print(f"Warning: Could not import {modname}: {e}")

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
