"""
Cloud FinOps Sentinel - Environment Automated Scheduler.
Automates scheduled shutdown of Dev and UAT instances outside business hours.
"""

from datetime import datetime

class EnvironmentScheduler:
    def evaluate_schedule(self, environment: str) -> str:
        """Returns RUNNING during business hours (08:00 - 20:00 UTC Mon-Fri), else STOPPED."""
        if environment.lower() in ["prod", "production"]:
            return "ALWAYS_RUNNING (Production SLA Protection)"
        
        now = datetime.utcnow()
        if now.weekday() < 5 and 8 <= now.hour < 20:
            return "RUNNING (Business Hours Active)"
        return "DEALLOCATED (Off-hours shutdown - saving 65% compute OPEX)"
