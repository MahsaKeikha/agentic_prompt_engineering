from typing import Any, Dict

def injection_analysis(scan: Dict[str, Any], adversarial_results: list[Dict[str, Any]] | None = None) -> Dict[str, Any]:
    failed = [x.get("id") for x in (adversarial_results or []) if not x.get("passed", False)]
    return {"scanner_suspicious": bool(scan.get("suspicious")), "failed_adversarial_cases": failed, "pass": not scan.get("suspicious") and not failed}
