import os
import json

SYSTEM32 = r"C:\Windows\System32"

lolbas = {
    "mshta.exe": "mshta",
    "regsvr32.exe": "regsvr32",
    "rundll32.exe": "rundll32",
    "msbuild.exe": "msbuild",
    "installutil.exe": "installutil",
    "wmic.exe": "wmic",
    "cscript.exe": "cscript",
    "wscript.exe": "wscript",
    "cmstp.exe": "cmstp",
    "pubprn.vbs": "pubprn"
}

detected = []

for f in os.listdir(SYSTEM32):
    if f.lower() in lolbas:
        detected.append({
            "binary": f,
            "technique": lolbas[f.lower()],
            "path": os.path.join(SYSTEM32, f)
        })

with open("lolbas_detected.json", "w") as out:
    json.dump(detected, out, indent=4)

print(f"[+] {len(detected)} binaires LOLBAS détectés.")
