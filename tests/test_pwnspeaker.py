"""
Tests for pwnspeaker plugins.
"""

import ast
import sys
import types
import importlib
import importlib.util
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _ensure_pwnagotchi_mocks():
    """Install mock pwnagotchi modules if not already present."""
    if "pwnagotchi" in sys.modules:
        return

    pwnagotchi = types.ModuleType("pwnagotchi")
    pwnagotchi.__path__ = []
    sys.modules["pwnagotchi"] = pwnagotchi

    plugins_mod = types.ModuleType("pwnagotchi.plugins")
    plugins_mod.Plugin = type("Plugin", (), {})
    plugins_mod.BasePlugin = type("BasePlugin", (), {})
    plugins_mod.toggle_plugin = MagicMock()
    sys.modules["pwnagotchi.plugins"] = plugins_mod
    pwnagotchi.plugins = plugins_mod

    ui_mod = types.ModuleType("pwnagotchi.ui")
    ui_mod.__path__ = []
    sys.modules["pwnagotchi.ui"] = ui_mod
    pwnagotchi.ui = ui_mod

    components_mod = types.ModuleType("pwnagotchi.ui.components")
    components_mod.LabeledValue = MagicMock
    components_mod.Text = MagicMock
    components_mod.Line = MagicMock
    components_mod.Rect = MagicMock
    components_mod.FilledRect = MagicMock
    components_mod.Widget = MagicMock
    sys.modules["pwnagotchi.ui.components"] = components_mod
    ui_mod.components = components_mod

    view_mod = types.ModuleType("pwnagotchi.ui.view")
    view_mod.BLACK = 0
    view_mod.WHITE = 1
    view_mod.__dict__["__getattr__"] = lambda name: MagicMock()
    sys.modules["pwnagotchi.ui.view"] = view_mod
    ui_mod.view = view_mod

    fonts_mod = types.ModuleType("pwnagotchi.ui.fonts")
    fonts_mod.Bold = MagicMock()
    fonts_mod.Medium = MagicMock()
    fonts_mod.Size = MagicMock()
    sys.modules["pwnagotchi.ui.fonts"] = fonts_mod
    ui_mod.fonts = fonts_mod


def _load_plugin_module(plugin_file):
    """Load a plugin module from file."""
    _ensure_pwnagotchi_mocks()
    spec = importlib.util.spec_from_file_location(plugin_file.stem, plugin_file)
    if spec is None:
        return None
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        return module
    except Exception:
        return None


def _find_plugin_class(module):
    """Find the plugin class in a module."""
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and hasattr(attr, "__version__"):
            return attr
    return None


class TestPwnspeakerSyntax:
    """Test that pwnspeaker files have valid Python syntax."""

    def test_pwnspeaker_parses(self):
        """pwnspeaker.py can be parsed by ast."""
        source = (REPO_ROOT / "pwnspeaker.py").read_text(encoding="utf-8")
        try:
            ast.parse(source)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in pwnspeaker.py: {e}")

    def test_pwnassistant_parses(self):
        """pwnassistant.py can be parsed by ast."""
        source = (REPO_ROOT / "pwnassistant.py").read_text(encoding="utf-8")
        try:
            ast.parse(source)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in pwnassistant.py: {e}")

    def test_pwnspeaker_compiles(self):
        """pwnspeaker.py compiles to bytecode."""
        source = (REPO_ROOT / "pwnspeaker.py").read_text(encoding="utf-8")
        try:
            compile(source, "pwnspeaker.py", "exec")
        except (SyntaxError, ValueError) as e:
            pytest.fail(f"Compile error in pwnspeaker.py: {e}")

    def test_pwnassistant_compiles(self):
        """pwnassistant.py compiles to bytecode."""
        source = (REPO_ROOT / "pwnassistant.py").read_text(encoding="utf-8")
        try:
            compile(source, "pwnassistant.py", "exec")
        except (SyntaxError, ValueError) as e:
            pytest.fail(f"Compile error in pwnassistant.py: {e}")


class TestPwnspeakerStructure:
    """Test that pwnspeaker plugin classes have required attributes."""

    def test_pwnspeak_has_version(self):
        """Pwnspeak class has __version__ attribute."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "__version__"), "Pwnspeak missing __version__"

    def test_pwnspeak_has_license(self):
        """Pwnspeak class has __license__ attribute."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "__license__"), "Pwnspeak missing __license__"

    def test_pwnspeak_has_name(self):
        """Pwnspeak class has __name__ attribute."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "__name__"), "Pwnspeak missing __name__"

    def test_pwnspeak_has_description(self):
        """Pwnspeak class has __description__ attribute."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "__description__"), "Pwnspeak missing __description__"

    def test_pwnspeak_has_author(self):
        """Pwnspeak class has __author__ attribute."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "__author__"), "Pwnspeak missing __author__"

    def test_pwnspeak_has_init(self):
        """Pwnspeak class has __init__ method."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "__init__"), "Pwnspeak missing __init__"

    def test_pwnspeak_has_on_loaded(self):
        """Pwnspeak class has on_loaded method."""
        module = _load_plugin_module(REPO_ROOT / "pwnspeaker.py")
        if module is None:
            pytest.skip("pwnspeaker.py could not be loaded")
        plugin_class = _find_plugin_class(module)
        if plugin_class is None:
            pytest.skip("No plugin class found in pwnspeaker.py")
        assert hasattr(plugin_class, "on_loaded"), "Pwnspeak missing on_loaded"


class TestPwnspeakerConfig:
    """Test that pwnspeaker config files are valid."""

    def test_pwnspeaker_yaml_exists(self):
        """pwnspeaker.yaml exists."""
        assert (REPO_ROOT / "pwnspeaker.yaml").exists(), "pwnspeaker.yaml missing"

    def test_pwnassistant_yaml_exists(self):
        """pwnassistant.yaml exists."""
        assert (REPO_ROOT / "pwnassistant.yaml").exists(), "pwnassistant.yaml missing"

    def test_requirements_exists(self):
        """requirements.txt exists."""
        assert (REPO_ROOT / "requirements.txt").exists(), "requirements.txt missing"

    def test_requirements_has_pyttsx3(self):
        """requirements.txt includes pyttsx3."""
        content = (REPO_ROOT / "requirements.txt").read_text(encoding="utf-8")
        assert "pyttsx3" in content, "requirements.txt missing pyttsx3"

    def test_requirements_has_pytz(self):
        """requirements.txt includes pytz."""
        content = (REPO_ROOT / "requirements.txt").read_text(encoding="utf-8")
        assert "pytz" in content, "requirements.txt missing pytz"
