import requests
import json

def run_test(payload_name, technique, status, sysmon_events):
    data = {
        "payload_name": payload_name,
        "technique": technique,
        "status": status,
        "sysmon_events": sysmon_events
    }
    response = requests.post("http://localhost:5000/api/add_result", json=data)
    print(f"Test ajouté : {payload_name} - {technique} - {status}")
    print(response.json())

tests = [
    {"payload_name": "test.hta", "technique": "mshta", "status": "bypass", "sysmon_events": 15},
    {"payload_name": "evil.sct", "technique": "regsvr32", "status": "bypass", "sysmon_events": 22},
    {"payload_name": "test.bat", "technique": "bat", "status": "blocked", "sysmon_events": 1},
    {"payload_name": "test.msbuild", "technique": "msbuild", "status": "bypass", "sysmon_events": 5},
    {"payload_name": "test.ps1", "technique": "powershell", "status": "blocked", "sysmon_events": 3},
    {"payload_name": "installutil.exe", "technique": "installutil", "status": "bypass", "sysmon_events": 10},
    {"payload_name": "wmic_payload", "technique": "wmic", "status": "blocked", "sysmon_events": 4},
    {"payload_name": "cscript.vbs", "technique": "cscript", "status": "bypass", "sysmon_events": 12}
]

for test in tests:
    run_test(test["payload_name"], test["technique"], test["status"], test["sysmon_events"])

print("Tous les tests ont été ajoutés !")
