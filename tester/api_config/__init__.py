from typing import TYPE_CHECKING, Any

__all__ = ['TensorConfig', 'APIConfig', 'analyse_configs', 'USE_CACHED_NUMPY', 'cached_numpy']

if TYPE_CHECKING:
    from .config_analyzer import (
        TensorConfig,
        APIConfig,
        analyse_configs,
        USE_CACHED_NUMPY,
        cached_numpy
    )

def __getattr__(name: str) -> Any:
    if name not in __all__:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    if name == 'TensorConfig':
        from .config_analyzer import TensorConfig
        return TensorConfig
    elif name == 'APIConfig':
        from .config_analyzer import APIConfig
        return APIConfig
    elif name == 'analyse_configs':
        from .config_analyzer import analyse_configs
        return analyse_configs
    elif name == 'USE_CACHED_NUMPY':
        from .config_analyzer import USE_CACHED_NUMPY
        return USE_CACHED_NUMPY
    elif name == 'cached_numpy':
        from .config_analyzer import cached_numpy
        return cached_numpy

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
