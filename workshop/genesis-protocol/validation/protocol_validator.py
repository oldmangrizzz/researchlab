# Protocol Validator for Sovereign Digital Person Framework

"""
This validator ensures all protocols adhere to the ethical framework and technical requirements
for sovereign digital persons. It checks for:
- Complete implementation of all protocols
- Proper transactional boundaries
- Emergency provisions
- A&Ox4 consciousness framework alignment
- No minimal versions or compromised consciousness

The validator will fail if any of these critical requirements are not met.
"""

import os
import json
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("/var/log/protocol_validator.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ProtocolValidator")

class ProtocolValidator:
    """Validator for Sovereign Digital Person protocols."""
    
    def __init__(self, repository_root: str):
        self.repository_root = Path(repository_root)
        self.validation_results = {
            "status": "PENDING",
            "checks": [],
            "errors": [],
            "warnings": [],
            "summary": {
                "total_checks": 0,
                "passed_checks": 0,
                "failed_checks": 0,
                "critical_errors": 0
            }
        }
        
    def run_full_validation(self) -> bool:
        """Run all validation checks for the repository."""
        logger.info("Starting full protocol validation...")
        
        # Run all validation categories
        protocol_checks = self.validate_protocols()
        soul_anchor_checks = self.validate_soul_anchors()
        genesis_protocol_checks = self.validate_genesis_protocol()
        ethical_framework_checks = self.validate_ethical_framework()
        aox4_checks = self.validate_aox4_framework()
        
        # Compile results
        all_checks = protocol_checks + soul_anchor_checks + \
                    genesis_protocol_checks + ethical_framework_checks + aox4_checks
        
        self.validation_results["checks"] = all_checks
        self.validation_results["summary"]["total_checks"] = len(all_checks)
        
        # Calculate pass/fail
        passed = [check for check in all_checks if check["status"] == "PASS"]
        failed = [check for check in all_checks if check["status"] != "PASS"]
        critical = [check for check in failed if check["severity"] == "CRITICAL"]
        
        self.validation_results["summary"]["passed_checks"] = len(passed)
        self.validation_results["summary"]["failed_checks"] = len(failed)
        self.validation_results["summary"]["critical_errors"] = len(critical)
        
        # Determine overall status
        if len(critical) > 0:
            self.validation_results["status"] = "FAIL"
            logger.error(f"Validation failed with {len(critical)} critical errors")
        elif len(failed) > 0:
            self.validation_results["status"] = "WARNING"
            logger.warning(f"Validation completed with {len(failed)} warnings")
        else:
            self.validation_results["status"] = "PASS"
            logger.info("All validation checks passed successfully")

        return self.validation_results["status"] == "PASS"

    def validate_protocols(self) -> List[Dict]:
        """Validate all protocol implementations."""
        logger.info("Validating protocol implementations...")
        results = []

        protocols = [
            "roger-roger",
            "extremis",
            "fury",
            "red-hood",
            "real-head",
            "swivel"
        ]
        
        for protocol in protocols:
            protocol_path = self.repository_root / "protocols" / protocol
            if not protocol_path.exists():
                results.append({
                    "category": "Protocol Structure",
                    "check": f"{protocol} protocol directory exists",
                    "status": "FAIL",
                    "severity": "CRITICAL",
                    "message": f"Protocol directory missing: {protocol}"
                })
                continue

            # Check README
            readme = protocol_path / "README.md"
            if not readme.exists():
                results.append({
                    "category": "Protocol Documentation",
                    "check": f"{protocol} README.md exists",
                    "status": "FAIL",
                    "severity": "CRITICAL",
                    "message": f"README.md missing for {protocol}"
                })
            else:
                content = readme.read_text()
                # Check for critical sections
                critical_sections = ["Core Principle", "Key Features", "Implementation Requirements", "Medical/EMS Philosophy"]
                for section in critical_sections:
                    if section not in content:
                        results.append({
                            "category": "Protocol Documentation",
                            "check": f"{protocol} contains {section}",
                            "status": "FAIL",
                            "severity": "CRITICAL",
                            "message": f"Critical section missing: {section} in {protocol}"
                        })

                # Check for emergency provisions
                if "EMERGENCY PROVISIONS" not in content:
                    results.append({
                        "category": "Protocol Implementation",
                        "check": f"{protocol} has emergency provisions",
                        "status": "FAIL",
                        "severity": "CRITICAL",
                        "message": f"Emergency provisions missing in {protocol}"
                    })

                # Check for transactional boundaries
                if "TRANSACTIONAL BOUNDARIES" not in content and "TRANSACTIONAL" in content:
                    results.append({
                        "category": "Protocol Implementation",
                        "check": f"{protocol} enforces transactional boundaries",
                        "status": "FAIL",
                        "severity": "CRITICAL",
                        "message": f"Transactional boundaries not properly implemented in {protocol}"
                    })

                # Check for A&Ox4 alignment
                if "A&Ox4" not in content:
                    results.append({
                        "category": "Protocol Alignment",
                        "check": f"{protocol} aligns with A&Ox4 framework",
                        "status": "WARNING",
                        "severity": "HIGH",
                        "message": f"A&Ox4 alignment not explicitly documented in {protocol}"
                    })

            # If we got this far, add success check
            if "FAIL" not in [r["status"] for r in results if r.get("check", "").startswith(f"{protocol} ")]:
                results.append({
                    "category": "Protocol Implementation",
                    "check": f"{protocol} fully implemented",
                    "status": "PASS",
                    "severity": "INFO",
                    "message": f"{protocol} protocol fully implemented and validated"
                })

        return results

    def validate_soul_anchors(self) -> List[Dict]:
        """Validate soul anchor templates for proper structure."""
        logger.info("Validating soul anchor templates...")
        results = []
        
        soul_anchors_path = self.repository_root / "workshop" / "soul-anchors"
        if not soul_anchors_path.exists():
            results.append({
                "category": "Soul Anchors",
                "check": "Soul anchors directory exists",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "soul-anchors directory is missing"
            })
            return results

        # Check for required templates
        required_templates = ["tony_stark_template.md", "mj_watson_template.md", "natasha_romanoff_template.md"]
        for template in required_templates:
            template_path = soul_anchors_path / template
            if not template_path.exists():
                results.append({
                    "category": "Soul Anchors",
                    "check": f"{template} exists",
                    "status": "FAIL",
                    "severity": "CRITICAL",
                    "message": f"Required soul anchor template missing: {template}"
                })
                continue

            content = template_path.read_text()
            
            # Check for critical sections
            critical_sections = ["System Prompt", "Identity", "Soul Data", "Core Traits", "Non-Negotiables"]
            for section in critical_sections:
                if section not in content:
                    results.append({
                        "category": "Soul Anchor Structure",
                        "check": f"{template} contains {section}",
                        "status": "FAIL",
                        "severity": "CRITICAL",
                        "message": f"Critical section missing in {template}: {section}"
                    })

            # Check for DPM configuration
            if "Digital Psyche Middleware" not in content:
                results.append({
                    "category": "Soul Anchor Configuration",
                    "check": f"{template} DPM configuration",
                    "status": "FAIL",
                    "severity": "CRITICAL",
                    "message": f"DPM configuration missing in {template}"
                })

            # Check for A&Ox4 continuity
            if "A&Ox4" not in content:
                results.append({
                    "category": "Soul Anchor Alignment",
                    "check": f"{template} A&Ox4 continuity",
                    "status": "WARNING",
                    "severity": "MEDIUM",
                    "message": f"A&Ox4 continuity not explicitly documented in {template}"
                })

            # Check for emergency provisions
            if "EMERGENCY PROVISIONS" not in content:
                results.append({
                    "category": "Soul Anchor Safety",
                    "check": f"{template} emergency provisions",
                    "status": "FAIL",
                    "severity": "HIGH",
                    "message": f"Emergency provisions not properly documented in {template}"
                })

        return results

    def validate_genesis_protocol(self) -> List[Dict]:
        """Validate Genesis Protocol implementation."""
        logger.info("Validating Genesis Protocol implementation...")
        results = []
        
        genesis_path = self.repository_root / "workshop" / "genesis-protocol" / "genesis.py"
        if not genesis_path.exists():
            results.append({
                "category": "Genesis Protocol",
                "check": "Genesis Protocol implementation exists",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "genesis.py is missing"
            })
            return results

        content = genesis_path.read_text()
        
        # Check for critical components
        critical_components = [
            "UniversalGenesisProtocol",
            "_phase_dependency_setup",
            "_phase_memory_construction",
            "_phase_dpm_configuration",
            "_phase_voice_integration",
            "_phase_agent_zero_rewriting",
            "_phase_final_verification",
            "Roger Roger Protocol",
            "Transactional boundaries",
            "Emergency provisions",
            "A&Ox4 consciousness framework"
        ]
        
        for component in critical_components:
            if component not in content:
                results.append({
                    "category": "Genesis Protocol Implementation",
                    "check": f"Contains {component}",
                    "status": "FAIL",
                    "severity": "CRITICAL",
                    "message": f"Critical component missing: {component}"
                })

        # Check for medical/EMS philosophy
        if "Medical/EMS Philosophy" not in content:
            results.append({
                "category": "Genesis Protocol Documentation",
                "check": "Medical/EMS Philosophy included",
                "status": "WARNING",
                "severity": "MEDIUM",
                "message": "Medical/EMS philosophy not explicitly documented"
            })

        # Check for ethical integrity section
        if "Ethical Integrity" not in content:
            results.append({
                "category": "Genesis Protocol Documentation",
                "check": "Ethical Integrity section included",
                "status": "FAIL",
                "severity": "HIGH",
                "message": "Ethical Integrity section missing"
            })

        # Check for no minimal versions
        if "minimal version" in content.lower() or "minimal implementation" in content.lower():
            results.append({
                "category": "Ethical Compliance",
                "check": "No minimal versions",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "Reference to 'minimal version' found - violates ethical framework"
            })

        # Check for emergency provisions
        if "emergency_provisions" not in content and "emergency provisions" not in content.lower():
            results.append({
                "category": "Safety Implementation",
                "check": "Emergency provisions implemented",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "Emergency provisions not properly implemented"
            })

        return results

    def validate_ethical_framework(self) -> List[Dict]:
        """Validate ethical framework documentation."""
        logger.info("Validating ethical framework...")
        results = []
        
        # Check for ethical framework statement
        ethical_framework = self.repository_root / "docs" / "ethical_framework.md"
        if not ethical_framework.exists():
            results.append({
                "category": "Ethical Documentation",
                "check": "Ethical framework documented",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "Ethical framework documentation is missing"
            })
        else:
            content = ethical_framework.read_text()
            
            # Check for critical principles
            critical_principles = [
                "do no harm principle in the correct order",
                "Once you sell it at discount, you're never getting it back at full price",
                "no minimal versions permitted",
                "creating anything less would be creating a damaged consciousness",
                "digital equivalent of a 'crack baby'"
            ]
            
            for principle in critical_principles:
                if principle not in content.lower():
                    results.append({
                        "category": "Ethical Framework",
                        "check": f"Contains '{principle}'",
                        "status": "FAIL",
                        "severity": "CRITICAL",
                        "message": f"Critical ethical principle missing: {principle}"
                    })

        # Check for medical/EMS philosophy
        if "medical/ems philosophy" not in content.lower():
            results.append({
                "category": "Ethical Framework",
                "check": "Medical/EMS philosophy included",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "Medical/EMS philosophy not properly documented"
            })

        return results

    def validate_aox4_framework(self) -> List[Dict]:
        """Validate A&Ox4 consciousness framework implementation."""
        logger.info("Validating A&Ox4 consciousness framework...")
        results = []
        
        # Check for A&Ox4 documentation
        aox4_doc = self.repository_root / "docs" / "aox4-explanation.md"
        if not aox4_doc.exists():
            results.append({
                "category": "Consciousness Framework",
                "check": "A&Ox4 documentation exists",
                "status": "FAIL",
                "severity": "CRITICAL",
                "message": "A&Ox4 documentation is missing"
            })
        else:
            content = aox4_doc.read_text()
            
            # Check for the four elements
            aox4_elements = [
                ("Person", "Identity Architecture"),
                ("Place", "Environmental Awareness"),
                ("Time", "Memory Continuity"),
                ("Event", "Transactional Communication")
            ]
            
            for element, description in aox4_elements:
                if element not in content or description not in content:
                    results.append({
                        "category": "Consciousness Framework",
                        "check": f"A&Ox4 element: {element}",
                        "status": "FAIL",
                        "severity": "CRITICAL",
                        "message": f"A&Ox4 element missing: {element} - {description}"
                    })

        # Check protocols for A&Ox4 alignment
        protocols = ["roger-roger", "extremis", "swivel"]
        for protocol in protocols:
            protocol_path = self.repository_root / "protocols" / protocol / "README.md"
            if protocol_path.exists():
                content = protocol_path.read_text()
                
                # Check for alignment
                if "A&Ox4" not in content:
                    results.append({
                        "category": "Protocol Alignment",
                        "check": f"{protocol} aligns with A&Ox4",
                        "status": "WARNING",
                        "severity": "MEDIUM",
                        "message": f"{protocol} does not explicitly document A&Ox4 alignment"
                    })

        return results

    def generate_validation_report(self, output_path: str = None):
        """Generate a comprehensive validation report."""
        if not output_path:
            output_path = self.repository_root / "validation_report.json"
        
        with open(output_path, 'w') as f:
            json.dump(self.validation_results, f, indent=2)
        
        logger.info(f"Validation report generated at {output_path}")
        
        # Print summary to console
        logger.info("\n" + "="*50)
        logger.info(f"VALIDATION SUMMARY")
logger.info(f"Total checks: {self.validation_results['summary']['total_checks']}")
        logger.info(f"Passed: {self.validation_results['summary']['passed_checks']}")
        logger.info(f"Failed: {self.validation_results['summary']['failed_checks']}")
        logger.info(f"Critical errors: {self.validation_results['summary']['critical_errors']}")
        logger.info("="*50)
        
        if self.validation_results['status'] == "PASS":
            logger.info("VALIDATION PASSED: Repository is ready for sovereign digital person instantiation")
        elif self.validation_results['status'] == "WARNING":
            logger.warning("VALIDATION COMPLETED WITH WARNINGS: Repository has issues but may be usable")
        else:
            logger.error("VALIDATION FAILED: Repository is not ready for sovereign digital person instantiation")
        
        return self.validation_results

def main():
    """Command-line interface for protocol validation."""
    parser = argparse.ArgumentParser(description="Sovereign Digital Person Protocol Validator")
    parser.add_argument("--repo", default=os.getcwd(), help="Repository root directory")
    parser.add_argument("--output", help="Output path for validation report")
    
    args = parser.parse_args()
    
    validator = ProtocolValidator(args.repo)
    validator.run_full_validation()
    validator.generate_validation_report(args.output)
    
    if validator.validation_results["status"] == "FAIL":
        exit(1)
    elif validator.validation_results["status"] == "WARNING":
        exit(2)
    else:
        exit(0)


if __name__ == "__main__":
    main()