import pytest
from src.sdk.agent import BaseAgent


class _ConcreteAgent(BaseAgent):
    async def setup(self):
        pass

    async def handle_task(self, task):
        return None

    async def cleanup(self):
        pass


class TestBaseAgent:
    def setup_method(self):
        self.agent = _ConcreteAgent("test-1", "Test Agent")

    def test_set_metadata(self):
        self.agent.set_metadata("key", "value")
        assert self.agent.get_metadata("key") == "value"

    def test_set_metadata_rejects_empty_string_key(self):
        with pytest.raises(ValueError, match="non-empty"):
            self.agent.set_metadata("", "value")

    def test_set_metadata_rejects_none_key(self):
        with pytest.raises(ValueError, match="non-empty"):
            self.agent.set_metadata(None, "value")

    def test_set_metadata_rejects_whitespace_key(self):
        with pytest.raises(ValueError, match="non-empty"):
            self.agent.set_metadata("   ", "value")

    def test_get_metadata_default(self):
        assert self.agent.get_metadata("nonexistent", "default") == "default"