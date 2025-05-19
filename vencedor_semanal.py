import requests
from datetime import datetime, timedelta

API_URL = "https://api.tuacasadeapostas.com/historico"  # Substitui pelo teu endpoint real
API_KEY = "O_TEU_TOKEN_AQUI"  # Substitui pelo teu token real

def main():
    hoje = datetime.today()
    segunda = hoje - timedelta(days=hoje.weekday())

    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(API_URL, headers=headers)
    apostas = response.json()

    leaderboard = {}

    for aposta in apostas:
        data = datetime.fromisoformat(aposta["data"])
        if data >= segunda and aposta["resultado"] == "ganhou":
            user = aposta["user_id"]
            odd = float(aposta["odd"])
            if user not in leaderboard or odd > leaderboard[user]:
                leaderboard[user] = odd

    vencedor = max(leaderboard, key=leaderboard.get)
    print(f"O vencedor da semana é {vencedor} com odd {leaderboard[vencedor]}")

if __name__ == "__main__":
    main()
