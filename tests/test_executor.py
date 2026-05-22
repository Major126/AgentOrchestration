import pytest
from src.agent.executor import AgentExecutor


class TestAgentExecutor:
    def test_init_defaults(self):
        executor = AgentExecutor()
        assert executor.max_concurrent == 5
        assert executor.max_results == 1000

    def test_init_custom_values(self):
        executor = AgentExecutor(max_concurrent=10, max_results=500)
        assert executor.max_concurrent == 10
        assert executor.max_results == 500

    def test_init_rejects_zero_max_concurrent(self):
        with pytest.raises(ValueError, match="positive integer"):
            AgentExecutor(max_concurrent=0)

    def test_init_rejects_zero_max_results(self):
        with pytest.raises(ValueError, match="positive integer"):
            AgentExecutor(max_results=0)

    def test_init_rejects_negative_max_results(self):
        with pytest.raises(ValueError, match="positive integer"):
            AgentExecutor(max_results=-1)

    def test_trim_results_removes_oldest(self):
        executor = AgentExecutor(max_concurrent=10, max_results=3)
        # Manually populate _results with 5 entries
        for i in range(5):
            executor._results[f"id-{i}"] = {"data": i}
        executor._trim_results()
        assert len(executor._results) == 3
        # Oldest entries (id-0, id-1) should be removed
        assert "id-0" not in executor._results
        assert "id-1" not in executor._results
        # Newest entries should remain
        assert "id-2" in executor._results
        assert "id-3" in executor._results
        assert "id-4" in executor._results

    def test_trim_results_under_limit(self):
        executor = AgentExecutor(max_concurrent=10, max_results=10)
        for i in range(5):
            executor._results[f"id-{i}"] = {"data": i}
        executor._trim_results()
        assert len(executor._results) == 5
