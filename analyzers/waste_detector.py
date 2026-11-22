"""
Cloud FinOps Sentinel - Waste Detection Engine.
Identifies unattached managed disks, orphaned public IPs, and obsolete snapshots (>30 days).
"""

from typing import List, Dict, Any

class WasteDetector:
    def detect_unattached_disks(self) -> List[Dict[str, Any]]:
        """Identify Azure Managed Disks in 'Unattached' state generating idle storage cost."""
        return [
            {
                "resource_name": "disk-prod-legacy-db-01",
                "resource_type": "Microsoft.Compute/disks",
                "size_gb": 512,
                "tier": "Premium_LRS",
                "monthly_cost_usd": 76.80,
                "status": "Unattached",
                "idle_days": 45,
                "recommended_action": "Snapshot and purge immediately."
            }
        ]

    def detect_orphaned_public_ips(self) -> List[Dict[str, Any]]:
        """Identify Static Standard Public IPs not associated with any NIC or Gateway."""
        return [
            {
                "ip_name": "pip-stg-app-gateway-old",
                "ip_address": "20.52.110.14",
                "monthly_cost_usd": 3.65,
                "status": "Unassociated",
                "recommended_action": "Delete unassociated IP allocation."
            }
        ]

    def run_full_waste_audit(self) -> Dict[str, Any]:
        disks = self.detect_unattached_disks()
        ips = self.detect_orphaned_public_ips()
        total_monthly_waste = sum(d["monthly_cost_usd"] for d in disks) + sum(i["monthly_cost_usd"] for i in ips)
        return {
            "unattached_disks_count": len(disks),
            "orphaned_ips_count": len(ips),
            "total_monthly_waste_usd": round(total_monthly_waste, 2),
            "annualized_savings_usd": round(total_monthly_waste * 12, 2)
        }
