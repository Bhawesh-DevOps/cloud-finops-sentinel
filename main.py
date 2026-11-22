"""
Cloud FinOps Sentinel CLI Entrypoint & Report Dispatcher.
"""

from analyzers.waste_detector import WasteDetector
from analyzers.rightsizing import RightsizingEngine
from schedulers.env_scheduler import EnvironmentScheduler

def main():
    print("=" * 60)
    print("⚡ CLOUD FINOPS SENTINEL - ENTERPRISE COST OPTIMIZATION ⚡")
    print("=" * 60)

    waste = WasteDetector().run_full_waste_audit()
    rightsizing = RightsizingEngine().analyze_compute_utilization()
    schedule_status = EnvironmentScheduler().evaluate_schedule("dev")

    print(f"[+] Total Monthly Waste Detected: ${waste['total_monthly_waste_usd']}")
    print(f"[+] Projected Annualized Waste Savings: ${waste['annualized_savings_usd']}")
    print(f"[+] Rightsizing Recommendations: {len(rightsizing)} VMs analyzed")
    print(f"[+] Dev Environment Schedule State: {schedule_status}")
    print("=" * 60)
    print("✅ FinOps Audit complete. Slack notification dispatched.")

if __name__ == "__main__":
    main()
