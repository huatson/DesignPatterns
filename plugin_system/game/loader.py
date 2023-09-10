"""
plugin loader
"""
import sys
import importlib


class PluginInterface(object):
    """simple interface where the plugin have a single init fn"""
    @staticmethod
    def initialize() -> None:
        pass


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type:ignore


def load_plugins(plugins: list[str]) -> None:
    for i in range(5):
        print(sys.path[i])
    for plug_name in plugins:
        plugin = import_module(plug_name)
        plugin.initialize()
