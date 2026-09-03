#!/usr/bin/env python3
"""
ISO 42001 Compliance Scanner — Policy-as-Code Enforcement

This script validates system configurations against ISO/IEC 42001 Annex A controls
and NIST AI RMF requirements.
"""

import json
import sys
from typing import Dict, List, Any

class ComplianceScanner:
    """Scans system configurations for compliance against GRC frameworks."""
    
    def __init__(self, config_path: str, soa_path: str = None):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.soa = None
        if soa_path:
            with open(soa_path, 'r') as f:
                self.soa = json.load(f)
        self.findings = []
        self.passed = 0
        self.failed = 0
    
    def check_control_a71(self):
        """A.7.1 — Data Acquisition and Preparation"""
        if not self.config.get('data_governance', {}).get('data_quality', False):
            self.findings.append({
                'control': 'A.7.1',
                'status': 'FAIL',
                'message': 'Data quality controls not implemented'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.7.1',
                'status': 'PASS',
                'message': 'Data quality controls are implemented'
            })
            self.passed += 1
    
    def check_control_a72(self):
        """A.7.2 — Data Quality and Provenance"""
        if not self.config.get('data_governance', {}).get('data_lineage', False):
            self.findings.append({
                'control': 'A.7.2',
                'status': 'FAIL',
                'message': 'Data lineage documentation not implemented'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.7.2',
                'status': 'PASS',
                'message': 'Data lineage is documented'
            })
            self.passed += 1
    
    def check_control_a61(self):
        """A.6.1 — AI System Requirements and Design"""
        if not self.config.get('lifecycle', {}).get('requirements_documented', False):
            self.findings.append({
                'control': 'A.6.1',
                'status': 'FAIL',
                'message': 'System requirements not documented'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.6.1',
                'status': 'PASS',
                'message': 'System requirements are documented'
            })
            self.passed += 1
    
    def check_control_a62(self):
        """A.6.2 — AI System Development and Testing"""
        if not self.config.get('lifecycle', {}).get('testing_completed', False):
            self.findings.append({
                'control': 'A.6.2',
                'status': 'FAIL',
                'message': 'Testing not completed'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.6.2',
                'status': 'PASS',
                'message': 'Testing is completed'
            })
            self.passed += 1
    
    def check_control_a63(self):
        """A.6.3 — AI System Deployment and Operation"""
        if not self.config.get('lifecycle', {}).get('monitoring_enabled', False):
            self.findings.append({
                'control': 'A.6.3',
                'status': 'FAIL',
                'message': 'Monitoring not enabled'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.6.3',
                'status': 'PASS',
                'message': 'Monitoring is enabled'
            })
            self.passed += 1
    
    def check_control_a91(self):
        """A.9.1 — Responsible Use of AI Systems"""
        if not self.config.get('human_oversight', {}).get('enabled', False):
            self.findings.append({
                'control': 'A.9.1',
                'status': 'FAIL',
                'message': 'Human oversight not enabled for high-risk systems'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.9.1',
                'status': 'PASS',
                'message': 'Human oversight is enabled'
            })
            self.passed += 1
    
    def check_control_a81(self):
        """A.8.1 — Information for Interested Parties"""
        if not self.config.get('transparency', {}).get('disclosure_enabled', False):
            self.findings.append({
                'control': 'A.8.1',
                'status': 'FAIL',
                'message': 'Transparency disclosure not enabled'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.8.1',
                'status': 'PASS',
                'message': 'Transparency disclosure is enabled'
            })
            self.passed += 1
    
    def check_control_a101(self):
        """A.10.1 — Third-party and Customer Relationships"""
        if not self.config.get('vendor_management', {}).get('assessments_completed', False):
            self.findings.append({
                'control': 'A.10.1',
                'status': 'FAIL',
                'message': 'Vendor assessments not completed'
            })
            self.failed += 1
        else:
            self.findings.append({
                'control': 'A.10.1',
                'status': 'PASS',
                'message': 'Vendor assessments are completed'
            })
            self.passed += 1
    
    def run(self):
        """Execute all control checks and generate report."""
        self.check_control_a71()
        self.check_control_a72()
        self.check_control_a61()
        self.check_control_a62()
        self.check_control_a63()
        self.check_control_a91()
        self.check_control_a81()
        self.check_control_a101()
        return self.generate_report()
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate a structured compliance report."""
        total = self.passed + self.failed
        return {
            'summary': {
                'total_controls': total,
                'passed': self.passed,
                'failed': self.failed,
                'compliance_score': f"{round((self.passed / total) * 100)}%" if total > 0 else "0%"
            },
            'findings': self.findings,
            'recommendations': [
                {'control': f['control'], 'recommendation': f'Remediate: {f["message"]}'}
                for f in self.findings if f['status'] == 'FAIL'
            ]
        }

if __name__ == "__main__":
    # Sample configuration for demonstration
    sample_config = {
        "system": "CreditIQ",
        "data_governance": {
            "data_quality": True,
            "data_lineage": True,
            "privacy_enabled": True
        },
        "lifecycle": {
            "requirements_documented": True,
            "testing_completed": True,
            "monitoring_enabled": True,
            "decommissioning_planned": False
        },
        "human_oversight": {
            "enabled": True,
            "override_capability": True
        },
        "transparency": {
            "disclosure_enabled": True,
            "explainability_enabled": True
        },
        "vendor_management": {
            "assessments_completed": False,
            "contracts_updated": False
        }
    }
    
    # Write sample config for demo
    with open('sample_config.json', 'w') as f:
        json.dump(sample_config, f, indent=2)
    
    scanner = ComplianceScanner('sample_config.json')
    report = scanner.run()
    print(json.dumps(report, indent=2))
