from nr_server.config.local_config import LocalConfig, Env


Env_Current = LocalConfig.current_env()


if Env_Current == Env.Debug:
    from .settings_debug import *
    pass
elif Env_Current == Env.Test:
    from .settings_test import *
    pass
elif Env_Current == Env.Product:
    from .settings_product import *
    pass
else:
    from .settings_product import *
    pass
