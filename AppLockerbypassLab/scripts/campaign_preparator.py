import requests
import json

API_NEW = "http://localhost:5000/api/campaign/new"
API_ADD = "http://localhost:5000/api/campaign/add_test"

def create_campaign(name):
    r = requests.post(API_NEW, json={"name": name})
    if r.status_code == 200:
        try:
            return r.json()  # Essayer de convertir la réponse en JSON
        except requests.exceptions.JSONDecodeError:
            print(f"Erreur : réponse de l'API invalide : {r.text}")
            return None
    else:
        print(f"Erreur HTTP : {r.status_code}")
        return None

def add_test(campaign_id, test):
    payload = {
        "campaign_id": campaign_id,
        "binary": test["binary"],
        "technique": test["technique"],
        "path": test["path"],
        "status": "pending"
    }
    return requests.post(API_ADD, json=payload).json()

def load_tests():
    with open("lolbas_detected.json", "r") as f:
        return json.load(f)

if __name__ == "__main__":
    print("[+] Création de la campagne...")
    info = create_campaign("Benchmark LOLBAS")

    if not info:
        print("[-] Échec de la création de la campagne.")
    else:
        campaign_id = info["campaign_id"]
        print(f"  → Campagne créée : ID {campaign_id}")

        tests = load_tests()

        print("\n[+] Ajout des tests LOLBAS...")
        for t in tests:
            r = add_test(campaign_id, t)
            print("  →", r)

        print("\n[✓] Campagne prête dans le dashboard.")
