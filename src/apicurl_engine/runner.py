"""Apicurl Vectorized Test Assertion Engine."""
from typing import Dict, Any

class ApiAssertionEngine:
    @staticmethod
    def assert_response(status_code: int, expected_status: int, latency_ms: float, max_latency_ms: float) -> Dict[str, Any]:
        return {
            "status_pass": status_code == expected_status,
            "latency_pass": latency_ms <= max_latency_ms,
            "all_passed": (status_code == expected_status) and (latency_ms <= max_latency_ms)
        }
