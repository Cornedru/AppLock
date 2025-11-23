import os
import json
import requests
from pathlib import Path

LOLBASE = {
    "mshta.exe": "mshta",
    "regsvr32.exe": "regsvr32",
    "cscript.exe": "cscript",
    "wmic.exe": "wmic",
    "powershell.exe": "powershell",
    "msbuild.exe": "msbuild",
    "rundll32.exe": "rundll32",
    "installutil.exe": "installutil"
}

API_URL = "http://localhost:5000/api/register_test"

def scan_lolbas():
    system32 = Path("C:/Windows/System32")
    results = []

    print("[+] Scan de System32 en cours...\n")

    # Scanner le dossier System32 à la recherche des exécutables LOLBAS
    for file in system32.iterdir():
        name = file.name.lower()
        if name in LOLBASE:
            technique = LOLBASE[name]
            print(f"  • Trouvé : {name} -> technique {technique}")
            results.append({
                "binary": name,
                "technique": technique,
                "path": str(file),
            })

    return results


def register_test(entry):
    payload = {
        "binary": entry["binary"],
        "technique": entry["technique"],
        "path": entry["path"],
        "status": "pending",
        "applocker_blocked": None,
        "sysmon_events": None
    }

    try:
        r = requests.post(API_URL, json=payload)
        
        # Vérifier si la requête a réussi
        r.raise_for_status()  # Cela lancera une exception en cas d'erreur HTTP (par exemple 404 ou 500)
        
        # Vérifier si la réponse est valide
        if r.text.strip():  # Si la réponse n'est pas vide
            return r.json()
        else:
            print(f"  [⚠️] Réponse vide pour {entry['binary']}")
            return {"error": "Réponse vide du serveur"}
    
    except requests.exceptions.RequestException as e:
        # Gestion des erreurs HTTP
        print(f"  [❌] Erreur lors de l'enregistrement de {entry['binary']}: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    entries = scan_lolbas()

    print("\n[+] Enregistrement dans le dashboard...\n")

    # Enregistrement des résultats dans le dashboard
    for e in entries:
        response = register_test(e)
        if "error" in response:
            print(f"  → Erreur avec {e['binary']}: {response['error']}")
        else:
            print(f"  → {e['binary']} enregistré : {response}")

    print("\n[✓] Scan terminé — tous les tests ont été préparés sans exécution.")
