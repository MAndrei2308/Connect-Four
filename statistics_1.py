import json


class Statistics:
    def __init__(self, filename = "statistics.json"):
        self.filename = filename
        try:
            self.data = self.load_data(filename)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = {
                "pvp": [],
                "pvc_easy": [],
                "pvc_medium": [],
                "pvc_hard": []
            }
            self.save_data(filename)


    def save_data(self, filename):
        with open(filename, "w") as file:
            json.dump(self.data, file)

    def load_data(self, filename = "statistics.json"):
        try:
            with open(filename, "r") as file:
                data = file.read()
                if not data:
                    return {
                        "pvp": [],
                        "pvc_easy": [],
                        "pvc_medium": [],
                        "pvc_hard": []
                    }
                return json.loads(data)
        except FileNotFoundError:
            return {
                "pvp": [],
                "pvc_easy": [],
                "pvc_medium": [],
                "pvc_hard": []
            }
        
    def update_data(self, game_mode, player1, player2, winner, time, filename = "statistics.json"):

        if game_mode == "pvp":
            self.data["pvp"].append({
                "rank": len(self.data["pvp"]) + 1,
                "player1": player1,
                "player2": player2,
                "winner": winner,
                "time": time
            })
        elif game_mode == "pvc_easy":
            self.data["pvc_easy"].append({
                "rank": len(self.data["pvc_easy"]) + 1,
                "player": player1,
                "computer": player2,
                "winner": winner,
                "time": time
            })
        elif game_mode == "pvc_medium":
            self.data["pvc_medium"].append({
                "rank": len(self.data["pvc_medium"]) + 1,
                "player": player1,
                "computer": player2,
                "winner": winner,
                "time": time
            })
        elif game_mode == "pvc_hard":
            self.data["pvc_hard"].append({
                "rank": len(self.data["pvc_hard"]) + 1,
                "player": player1,
                "computer": player2,
                "winner": winner,
                "time": time
            })

        # sort data by time
        for game_mode in self.data:
            self.data[game_mode].sort(key=lambda x: int (x["time"].split(":")[0]) * 60 + int(x["time"].split(":")[1]))

            # update ranks
            for i, game in enumerate(self.data[game_mode]):
                game["rank"] = i + 1
            
            # truncate data to top 3
            self.data[game_mode] = self.data[game_mode][:3]

        self.save_data(filename)

    def end_game(self, winner, time, game_mode):
        if game_mode == "pvp":
            player1 = "Player 1"
            player2 = "Player 2"
            self.update_data(game_mode, player1, player2, winner, time)
        elif game_mode == "pvc_easy":
            player = "Player"
            ai = "Easy AI"
            self.update_data(game_mode, player, ai, winner, time)
        elif game_mode == "pvc_medium":
            player = "Player"
            ai = "Medium AI"
            self.update_data(game_mode, player, ai, winner, time)
        elif game_mode == "pvc_hard":
            player = "Player"
            ai = "Hard AI"
            self.update_data(game_mode, player, ai, winner, time)
    