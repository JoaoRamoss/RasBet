from database import Database
import requests
import time
import json


class GameDB():

    VALID = "valid"
    ERROR = "error"

    def __init__(self, db="sql.db"):
        self.db = Database(db)
        self.api_timeout = 50

    def reset_games(self):
        #Creates game table
        db_name = "GAMES"
        self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
        self.db.execute('''CREATE TABLE {}
            (ID   VARCHAR(32)   PRIMARY KEY   NOT NULL,
            HOMETEAM            VARCHAR(24)   NOT NULL,
            AWAYTEAM            VARCHAR(24)   NOT NULL,
            START_TIME          TEXT          NOT NULL,
            COMPLETED           VARCHAR(5)    NOT NULL CHECK(COMPLETED='TRUE' OR COMPLETED='FALSE'),
            SCORES              VARCHAR(5),
            SPORT               VARCHAR(12)   NOT NULL,
            HOME_ODD            INT           NOT NULL,
            AWAY_ODD            INT           NOT NULL,
            DRAW_ODD            INT           NOT NULL,
            STATE               VARCHAR(6)    NOT NULL CHECK(STATE='ACTIVE' OR STATE='WAIT' OR STATE='SLEEP'));
            '''.format(db_name))
        
        print("Game Table initialized")

        #Creates outcome table
        db_name = "OUTCOMES"
        self.db.execute("DROP TABLE IF EXISTS {}".format(db_name))
        self.db.execute('''CREATE TABLE {}
            (NAME               VARCHAR(24)  NOT NULL,
            PRICE               REAL         NOT NULL,
            MARKET_KEY          VARCHAR(24)  NOT NULL,
            GAME_ID             VARCHAR(24)  NOT NULL,
            BOOKMAKER_NAME      VARCHAR(24)  NOT NULL,
            LASTUPDATE          TEXT         NOT NULL,
            PRIMARY KEY(NAME, MARKET_KEY, BOOKMAKER_NAME, GAME_ID),
            FOREIGN KEY(GAME_ID, BOOKMAKER_NAME) REFERENCES BOOKMAKER(GAME_ID, NAME));
            '''.format(db_name))
        
        print("Outcomes Table initialized")
        return self.VALID


    def update_games(self):
        try:
            print("Trying to fetch games from API")
            data = requests.get("http://ucras.di.uminho.pt/v1/games", timeout=self.api_timeout).json()
            print("Games fetched from API")
        except:
            print("Couldn't fetch games from API")
            f = open("default_games.json", "r")
            data = json.load(f)
            f.close()
            print("Imported default games from JSON")
        for game in data:
            
            self.db.execute('''
                UPDATE GAMES SET COMPLETED='{}', SCORES='{}' WHERE ID='{}'
            '''.format(str(game["completed"]).upper(), game["scores"], game["id"]))
            self.db.execute('''
                INSERT OR IGNORE INTO GAMES VALUES ('{}', '{}', '{}', '{}', '{}', '{}', 'FOOTBALL', 0, 0, 0, 'SLEEP')
            '''.format(game["id"], game["homeTeam"], game["awayTeam"], game["commenceTime"], str(game["completed"]).upper(), game["scores"]))
            
            for bk in game["bookmakers"]:
                for mk in bk["markets"]:
                    for out in mk["outcomes"]:

                        self.db.execute('''
                            UPDATE OUTCOMES SET PRICE='{}', LASTUPDATE='{}' WHERE NAME='{}' AND MARKET_KEY='{}' AND GAME_ID='{}' AND BOOKMAKER_NAME='{}'
                        '''.format(out["price"], bk["lastUpdate"], out["name"], mk["key"], game["id"], bk["key"]))
                        self.db.execute('''
                            INSERT OR IGNORE INTO OUTCOMES VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
                        '''.format(out["name"], out["price"], mk["key"], game["id"], bk["key"], bk["lastUpdate"]))
        


    def get_game(self, id):
        games = self.db.execute('''
            SELECT * FROM GAMES WHERE ID='{}'
        '''.format(id))
        if len(games) > 0:
            return games[0]
        return None


    def is_running(self, id):
        games = self.db.execute('''
            SELECT COMPLETED FROM GAMES WHERE ID='{}'
        '''.format(id))
        if len(games) > 0: return games[0][0]
        return "FALSE"


    def get_score(self, id):
        games = self.db.execute('''
            SELECT SCORES FROM GAMES WHERE ID='{}'
        '''.format(id))
        if len(games) > 0: return games[0][0]
        return "0x0"

        
    def get_odd(self, id, res):
        games = self.db.execute('''
            SELECT HOME_ODD, AWAY_ODD, DRAW_ODD FROM GAMES WHERE ID='{}'
        '''.format(id))
        if len(games) > 0:
            return games[0][res]
        return None


    def get_games(self, sport, state="ANY"):
        if state == "ANY":
            games = self.db.execute('''
                    SELECT * FROM GAMES WHERE SPORT='{}'
                '''.format(sport))
            return self.VALID, games
        else:
            games = self.db.execute('''
                    SELECT * FROM GAMES WHERE SPORT='{}' AND STATE='{}' AND COMPLETED='FALSE'
                '''.format(sport, state))
            return self.VALID, games


    def get_games_and_outcomes(self, sport):
        try:
            results = []
            games = self.db.execute('''
                    SELECT * FROM GAMES WHERE SPORT='{}' AND (STATE='WAIT' OR STATE='ACTIVE') AND COMPLETED='FALSE'
                '''.format(sport))
            for g in games:
                outs = self.db.execute('''
                        SELECT NAME, PRICE, MARKET_KEY, BOOKMAKER_NAME, LASTUPDATE FROM OUTCOMES WHERE GAME_ID='{}'
                    '''.format(g[0]))
                results.append((g, outs))
            return self.VALID, results
        except:
            return self.ERROR, []


    def set_games_states(self, sport, ids, states):
        try:
            if len(ids) != len(states) or len(ids) == 0:
                return self.ERROR
            for i in range(len(ids)):
                if states[i] == "ACTIVE":
                    self.db.execute('''
                            UPDATE GAMES SET STATE='{}' WHERE ID='{}' AND SPORT='{}' AND COMPLETED='FALSE' AND HOME_ODD>1 AND AWAY_ODD>1 AND DRAW_ODD>1
                        '''.format(states[i], ids[i], sport))
                else:
                    self.db.execute('''
                            UPDATE GAMES SET STATE='{}' WHERE ID='{}' AND SPORT='{}' AND COMPLETED='FALSE'
                        '''.format(states[i], ids[i], sport))
            return self.VALID
        except:
            return self.ERROR


    def set_games_odds(self, sport, ids, odds):
        ols = [*set([len(x) for x in odds])]
        if len(ids) != len(odds) or len(ols) != 1 or ols[0] != 3 or len(ids) == 0:
            return self.ERROR
        for i in range(len(ids)):
            if any([x <= 1 for x in odds[i]]): continue
            self.db.execute('''
                    UPDATE GAMES SET HOME_ODD={}, DRAW_ODD={}, AWAY_ODD={}, STATE='ACTIVE' WHERE ID='{}' AND SPORT='{}' AND COMPLETED='FALSE' 
                '''.format(odds[i][0], odds[i][1], odds[i][2], ids[i], sport))
            self.backend.notify_about_game(ids[i])
        return self.VALID
    
    def set_backend(self,backend):
        self.backend = backend



    def print_game(self, id):
        print(self.get_game(id))
    