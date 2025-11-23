#!/usr/bin/env python3
"""Script personnalisé d'obfuscation"""

import sys
sys.path.append('scripts')
from obfuscate_payloads import PayloadObfuscator

# Créer l'obfuscateur
obf = PayloadObfuscator(output_dir="payloads/obfuscated/custom/")

# Votre payload personnalisé
custom_payload = """
$url = "http://example.com/data"
$client = New-Object System.Net.WebClient
$data = $client.DownloadString($url)
Write-Host $data
"""

print("\n🎨 Obfuscation Personnalisée\n")

# Appliquer différentes techniques
obf.base64_multi_layer(custom_payload, layers=5, name="custom_b64_x5.ps1")
obf.gzip_base64(custom_payload, name="custom_gzip.ps1")
obf.xor_encode(custom_payload, key=0x42, name="custom_xor.ps1")

print("\n✅ Payloads personnalisés générés!")