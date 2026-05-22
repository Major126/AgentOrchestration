import pytest
from src.agent.executor import AgentExecutor


class TestAgentExecutor:
    def test_init_default(self):
        executor = AgentExecutor()
        assert executor.max_concurrent == 5

    def test_init_custom(self):
        executor = AgentExecutor(max_concurrent=10)
        assert executor.max_concurrent == 10

    def test_init_rejects_zero(self):
        with pytest.raises(ValueError, match="positive integer"):
            AgentExecutor(max_concurrent=0)

    def test_init_rejects_negative(self):
        with pytest.raises(ValueError, match="positive integer"):
            AgentExecutor(max_concurrent=-1)

    def test_init_rejects_non_int(self):
        with pytest.raises(ValueError, match="positive integer"):
            AgentExecutor(max_concurrent="5")
