# netdevops
Automated Python framework for multi-vendor auditing (Cisco, Juniper, Nokia) and physical fault mitigation using APIs (REST/RESTCONF)

# Multi-Vendor NetDevOps & Closed-Loop Automation Framework

This repository features a modular automation project designed for Tier-1 Telecom Carriers. It demonstrates how to transition from legacy CLI/SSH parsing to modern **Infrastructure as Code (IaC)** and **Intent-Based Networking** using APIs and structured data processing.

##Key Features

* **Multi-Vendor Data Estandardization:** Modular structure (`agents`) built in Python to collect configuration states from **Cisco IOS-XE/XR**, **Juniper JunOS**, and **Nokia SR-OS**.
* **API Integration & Structured Data:** Replaces traditional text scraping by consuming **REST / RESTCONF** APIs, processing standard **JSON** and **YANG** data models into native Python dictionaries.
* **Global Network Auditing (Orchestrator):** A centralized orchestrator that unifies inventory logs across different hardware vendors and automatically generates comprehensive network compliance reports in structured **CSV/Excel** formats.
* **Closed-Loop Automation (Self-Healing Network):** A reactive script that monitors physical interface performance counters (such as **CRC errors**) and programmatically shuts down degraded interfaces via API to force deterministic traffic routing through backup paths before service degradation impacts customers.

---

##Project Architecture

```text
    [ Infrastructure Telemetry ]
  Cisco (RESTCONF)  |  Juniper (REST API)  |  Nokia (RESTCONF)

         |                  |                   |
  [cisco_agent.py]   [juniper_agent.py]   [nokia_agent.py]
         \                  |                  /
          \                 |                 /
         [ Data Harmonization into Common Python Structures ]
                            |
           +----------------+----------------+

           |                                 |
 [orquestador.py]                 [mitigacion_crc.py]
(Centralized Compliance Logging) (Event-Driven Remediation & API Shutdown)

           |                                 |
`reporte_cumplimiento_red.csv`     `🔒 [CONFIG] ge-0/0/0 Disabled`
```

---

##How to Run the Scripts (Simulation Mode)

This repository includes real production JSON payloads mapped as internal mock data, allowing the automation logic to be validated locally on any development environment without active device connectivity.

### Prerequisites
Make sure you have Python 3.x installed and the `requests` library:
```bash
pip install requests
```

### 1. Run the Network Compliance Audit
To collect multi-vendor interface data and automatically generate the consolidated CSV compliance report:
```bash
python orquestador.py
```

### 2. Run the Event-Driven Closed-Loop Remediation
To simulate the automated detection and mitigation of physical layer issues based on CRC error thresholds:
```bash
python mitigacion_crc.py
```

---

## Production Deployment (Hardware Connectivity)

To transition from the included simulation mode to a live physical production environment (e.g., Cisco DevNet Sandbox or live Carrier lab):

1. Enable the programmable interfaces on the target devices via traditional CLI:
   * **Cisco IOS-XE:** `restconf` and `ip http secure-server`
   * **Juniper JunOS:** `set system services rest http`
2. Update the credentials block, IP address, and port variables at the top of the connection scripts.
3. Replace the mock dictionary loading with native HTTP method executions (`requests.get()` / `requests.post()`) targeting the vendor-specific API endpoint URLs.
