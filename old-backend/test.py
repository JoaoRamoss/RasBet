import requests
import json
import sys

url = "http://localhost:8080/"

bot = requests.session()


def test_register():
    print("Valid:", bot.post(url + "api/register_user",
          json={"nif": "123456789", "username": "pedro", "email": "pedro@rasbet.com", "password": "Qq@12345"}).json())
    print("NIF taken:", bot.post(url + "api/register_user",
          json={"nif": "123456789", "username": "ramos", "email": "ramos@rasbet.com", "password": "Qq@12345"}).json())
    print("Username taken:", bot.post(url + "api/register_specialist/yuCyg2JIEav5uj56uQ6f0zMMxMB4J4sHYYcpmdT8bInEF6fk5a6IZqQEm4d6",
                                      json={"nif": "123456380", "username": "pedro", "email": "specialist@rasbet.com", "password": "Qq@12345"}).json())
    print("Valid:", bot.post(url + "api/register_specialist/yuCyg2JIEav5uj56uQ6f0zMMxMB4J4sHYYcpmdT8bInEF6fk5a6IZqQEm4d6",
                             json={"nif": "123456380", "username": "specialist", "email": "specialist@rasbet.com", "password": "Qq@12345"}).json())
    print("Invalid password:", bot.post(url + "api/register_admin/qwefqerfugqbfibwuqcbwefqucuyv123ubhd123123n3nb213b12bdMPEMOS",
                                        json={"nif": "987654320", "username": "admin1", "email": "admin1@rasbet.com", "password": "Q@12345"}).json())


def test_log_out():
    print("Valid:", bot.post(url + "api/logout").json())


def test_login():
    print("Wrong password:", bot.post(url + "api/login",
          json={"username": "specialist", "password": "Qq@123"}).json())
    print("Invalid username:", bot.post(url + "api/login",
          json={"username": "user123", "password": "Qq@123"}).json())
    print("Valid:", bot.post(url + "api/login",
          json={"username": "pedro@rasbet.com", "password": "Qq@12345"}).json())


def test_edit():
    print("Valid:", bot.post(url + "api/edit_profile",
          json={"username": "pedrocas", "email": "pedro@gmail.com", "password": "Qq@12345"}).json())
    print("Username taken:", bot.post(url + "api/edit_profile",
          json={"nif": "123456789", "username": "admin", "email": "pedro@gmail.com", "password": "Qq@12345"}).json())


def test_deposit():
    print("Valid:", bot.post(url + "api/deposit_money",
          json={"amount": "100"}).json())
    print("Invalid amount:", bot.post(
        url + "api/deposit_money", json={"amount": "0"}).json())
    print("Invalid amount:", bot.post(
        url + "api/deposit_money", json={"amount": "-10"}).json())


def test_withdraw():
    print("Valid:", bot.post(url + "api/withdraw_money",
          json={"amount": "30"}).json())
    print("Invalid amount:", bot.post(
        url + "api/withdraw_money", json={"amount": "-20"}).json())
    print("Invalid amount:", bot.post(
        url + "api/withdraw_money", json={"amount": "0"}).json())


def test_bet():
    print("Valid:", bot.post(url + "api/bet", json={"amount": "10", "game_ids": [
          "8e9c7ec7cdaedaf567aba0280ad06600"], "beted_results": [1]}).json())
    print("Invalid amount:", bot.post(url + "api/bet", json={"amount": "-10", "game_ids": [
          "8e9c7ec7cdaedaf567aba0280ad06600"], "beted_results": [1]}).json())
    print("Invalid amount:", bot.post(url + "api/bet", json={"amount": "0", "game_ids": [
          "8e9c7ec7cdaedaf567aba0280ad06600"], "beted_results": [1]}).json())
    print("Invalid data:", bot.post(url + "api/bet", json={"amount": "10", "game_ids": [
          "8e9c7ec7cdaedaf567aba0280ad06600"], "beted_results": []}).json())
    print("Invalid id:", bot.post(url + "api/bet", json={"amount": "10", "game_ids": [
          "8e9c7ec7cdaedaf567aba0280ad0A600"], "beted_results": [1]}).json())


def test_get_data():
    print("Valid:", bot.get(url + "api/get_active_games/futebol").json())


def test_all():
    print("|| Test register ||")
    test_register()

    print("|| Log Out ||")
    test_log_out()

    print("|| Test login ||")
    test_login()

    print("|| Test edit ||")
    test_edit()

    print("|| Test Deposit ||")
    test_deposit()

    print("|| Test Withdraw ||")
    test_withdraw()

    print("|| Test Bet ||")
    test_bet()

    print("|| Test Get Data ||")
    test_get_data()


def testssss():
    # Register user and specialist
    print("Register user:", bot.post(url + "api/register_user",
          json={"nif": "123456789", "username": "pedro", "email": "pedro@rasbet.com", "password": "Qq@12345"}).json())
    print("Register specialist:", bot.post(url + "api/register_specialist/yuCyg2JIEav5uj56uQ6f0zMMxMB4J4sHYYcpmdT8bInEF6fk5a6IZqQEm4d6",
                                           json={"nif": "123456380", "username": "specialist", "email": "specialist@rasbet.com", "password": "Qq@12345"}).json())

    # Login as admin, see all games and choose which ones will be used
    print("Login admin:", bot.post(url + "api/login",
          json={"username": "admin", "password": "Admin123"}).json())
    print("Get all games:", bot.get(url + "/api/get_all_games/futebol").json())
    print("Set game to wait:", bot.post(url + "/api/set_games_states",
          json={"ids": ["8e9c7ec7cdaedaf567aba0280ad06600"], "states": ["WAIT"]}).json())

    print("Login specialist:", bot.post(url + "api/login",
          json={"username": "specialist", "password": "Qq@12345"}).json())
    print("Get wait games:", bot.get(url + "/api/get_wait_games/futebol").json())
    print("Set game odds:", bot.post(url + "/api/set_games_odds",
          json={"ids": ["8e9c7ec7cdaedaf567aba0280ad06600"], "odds": [(1.5, 2, 2.1)]}).json())

    print("Login user:", bot.post(url + "api/login",
          json={"username": "pedro@rasbet.com", "password": "Qq@12345"}).json())
    print("Get user data:", bot.get(url + "/api/get_user_data").json())
    print("Get active games:", bot.get(
        url + "/api/get_active_games/futebol").json())


def user_menu():
    s = ""
    while s != "logout":
        print("|USER MENU|\nO que pretende fazer agora?")
        print("1->Depositar Dinheiro\n2->Levantar Dinheiro\n3->Ver perfil\n4->Editar perfil\n5->Fazer uma aposta")
        s = input(">>")
        if s == "1":
            print("Quanto dinheiro pretende depositar?")
            s = input(">>")
            response = bot.post(url + "api/deposit_money",
                                json={"amount": float(s)}).json()["response"]
            print(response)
            if response == "valid":
                print("Depósito realizado com sucesso!")
            elif response == "invalid_amount":
                print("Quantia depositada é inválida!")
        elif s == "2":
            print("Quanto dinheiro pretende levantar?")
            s = input(">>")
            response = bot.post(url + "api/withdraw_money",
                                json={"amount": float(s)}).json()["response"]
            if response == "valid":
                print("Levantamento realizado com sucesso!")
            elif response == "invalid_amount":
                print("A Quanto que quer levantar é inválida!")
        elif s == "3":
            response = bot.get(url + "api/get_user_data").json()["data"]
            print("NIF:", response[0])
            print("Username:", response[1])
            print("Email:", response[2])
            print("Money:", response[4])
        elif s == "4":
            user = input("New user:")
            email = input("New email:")
            pwd = input("New password:")
            response = bot.post(url + "api/edit_profile", json={
                                "username": user, "email": email, "password": pwd}).json()["response"]
            print(response)

        elif s == "5":
            print("Em que jogo pretende apostar?\nClique 0 caso queira acabar a aposta.")
            response = bot.get(
                url + "api/get_active_games/futebol").json()["data"]
            s = ""
            ids = []
            bets = []
            while s != "0":
                for i, game in enumerate(response):
                    print(i+1, ":", game[1], "("+str(game[7])+")",
                          "- Empate ("+str(game[9])+") -", game[2], "("+str(game[8])+")")
                cota = 1
                for c in bets:
                    cota = cota * c
                #print("Cota:", cota)
                s = min(int(input("Choose a game:")), len(response))
                if s == 0 or response[s-1][0] in ids:
                    break
                ids.append(response[s-1][0])
                print("O que pretende apostar?\n1 -> Vitória do", response[int(
                    s)-1][1], "\n2 -> Vitória do", response[int(s)-1][2], "\n3 -> Empate")
                s1 = int(input(">>"))
                s1 = min(max(1, s1), 3)
                if s1 == 0:
                    break
                bets.append(s1-1)
            a = float(input("Amount to bet:"))
            response = bot.post(
                url + "api/bet", json={"amount": a, "game_ids": ids, "beted_results": bets}).json()["response"]
            if response == "valid" and len(ids) > 0:
                # , "€ para", cota*a, "€.Boa sorte!")
                print("Aposta realizada :", a, "€")
            else:
                print(response)
        elif s != "logout":
            print("Comando Desconhecido")
    bot.post(url + "api/logout").json()


def specialist_menu():
    s = ""
    while s != "logout":
        print("|SPECIALIST MENU|\nO que deseja fazer?\n1->Alterar odds de jogos.")
        s = input(">>")
        if s == "1":
            response = bot.get(
                url + "/api/get_wait_games/futebol").json()["data"]

            print("<GAMES>")
            for i, game in enumerate(response):
                print(i+1, "->", game[0][1], "vs", game[0][2])

            print("Escolha o jogo que pretende ver os bookmakers")
            s = input(">>")
            if s.isdigit() and int(s) > 0 and int(s) <= len(response):
                g_id = response[int(s) - 1][0][0]
                if s.isdigit():
                    for bk in response[int(s) - 1][1]:
                        print(bk[3], bk[2], bk[0], bk[1])

                print("\nType \"exit\" to exit")
                s1 = input("HOME ODD >>")
                if s1.replace(".", "").isdigit():
                    s2 = input("AWAY ODD >>")
                    if s2.replace(".", "").isdigit():
                        s3 = input("DRAW ODD >>")
                        if s3.replace(".", "").isdigit():
                            response = bot.post(
                                url + "api/set_games_odds", json={"ids": [g_id], "odds": [(s1, s2, s3)]})
                            print(response)
        elif s != "logout":
            print("Opção Desconhecida!")
    bot.post(url + "api/logout").json()


def admin_menu():
    s = ""
    while s != "logout":
        print("|ADMIN MENU|\nO que deseja fazer?\n1->Administrar jogos.")
        s = input(">>")
        if s == "1":
            response = bot.get(
                url + "/api/get_all_games/futebol").json()["data"]

            for i, game in enumerate(response):
                if game[4] == "TRUE":
                    active = "COMPLETED"
                else:
                    active = "NOT COMPLETED"
                print(i+1, active, game[1], "("+str(game[7])+")", "- Empate (" +
                      str(game[9])+") -", game[2], "("+str(game[8])+")", game[10])

            print("Escolha o jogo que pretende administrar\nEscreva \"exit para sair\"")
            s = input(">>")
            if s.isdigit() and int(s) > 0 and int(s) <= len(response):
                g_id = response[int(s) - 1][0]
                print("Escreva o novo estado do jogo")
                poss_states = []
                if game[4] == "FALSE" and response[int(s) - 1][10] == "SLEEP":
                    poss_states = ["WAIT"]
                if game[4] == "FALSE" and response[int(s) - 1][10] == "WAIT":
                    poss_states = ["ACTIVE", "SLEEP"]
                if game[4] == "FALSE" and response[int(s) - 1][10] == "ACTIVE":
                    poss_states = ["WAIT", "SLEEP"]
                print("Estados possiveis:", poss_states)
                state = input(">>")
                if state in poss_states:
                    bot.post(url + "/api/set_games_states",
                             json={"ids": [g_id], "states": [state]}).json()
        elif s != "logout":
            print("Comando Desconhecido")
    bot.post(url + "api/logout").json()


def cmd():
    s = ""
    while s != "exit":
        print("|MAIN MENU|\n1-Login\n2-Registo\n3-Registo como Especialista\n4-Registo com Administrador")
        s = input(">>")
        if s == "1":
            username = input("Username:")
            password = input("Password:")
            response = bot.post(
                url + "api/login", json={"username": username, "password": password}).json()["response"]

            if response == "valid_user":
                print("Login efetuado com sucesso!")
                user_menu()
            elif response == "valid_specialist":
                print("Login especialista efetuado com sucesso!")
                specialist_menu()

            elif response == "valid_admin":
                print("Login Admin efetuado com sucesso!")
                admin_menu()
            else:
                print(response)
        elif s == "2" or s == "3" or s == "4":
            username = input("Username:")
            password = input("Password:")
            email = input("Email:")
            nif = input("NIF(Número de Identificação Fiscal):")
            if s == "2":
                response = bot.post(url + "api/register_user", json={
                                    "nif": nif, "username": username, "email": email, "password": password}).json()["response"]
            elif s == "3":
                response = bot.post(url + "api/register_specialist/yuCyg2JIEav5uj56uQ6f0zMMxMB4J4sHYYcpmdT8bInEF6fk5a6IZqQEm4d6",
                                    json={"nif": nif, "username": username, "email": email, "password": password}).json()["response"]
            elif s == "4":
                response = bot.post(url + "api/register_admin/qwefqerfugqbfibwuqcbwefqucuyv123ubhd123123n3nb213b12bdMPEMOS",
                                    json={"nif": nif, "username": username, "email": email, "password": password}).json()["response"]

            if response == "valid_user":
                print("Registo efetuado com sucesso!")
                user_menu()
            elif response == "valid_specialist":
                print("Especialista registado com sucesso!")
                specialist_menu()
            elif response == "valid_admin":
                print("Administrador registado com sucesso!")
                admin_menu()
            elif response == "nif_taken":
                print("That NIF was already used.")
            elif response == "username_taken":
                print("That Username was already used.")
            elif response == "password_error":
                print("Invalid password.")
            else:
                print("ERROR")
        elif s != "exit":
            print("Comando Desconhecido")


def test_2_fase():
    print("Register user:", bot.post(url + "api/register_user",
        json={"nif": "123456789", "username": "pedro", "email": "pedro@rasbet.com", "password": "User123"}).json())

    print("Logout:", bot.post(url + "api/logout").json())

    print("Login admin:", bot.post(url + "api/login",
        json={"username": "admin", "password": "Admin123"}).json())

    print("Notify all:", bot.post(url + "api/notify_all", json={"message" : "Boas manos"}).json())

    print("Set options:", bot.post(url + "api/options", json={"option" : "PROMOTIONS_LIMIT", "value" : "10"}).json())

    print("Get options:", bot.get(url + "api/options").json())

    print("Logout:", bot.post(url + "api/logout").json())

    print("Login user:", bot.post(url + "api/login",
        json={"username": "pedro", "password": "User123"}).json())

    print("Deposit Valid:", bot.post(url + "api/deposit_money",
          json={"amount": 100}).json())

    print("Bet Valid:", bot.post(url + "api/bet", json={"amount": 10, "game_ids": [
          "8e9c7ec7cdaedaf567aba0280ad06600"], "beted_results": [1]}).json())

    print("Cash out Valid:", bot.post(url + "api/cash_out", json={"bet_id": 1}).json())

    print("Bet history Valid:", bot.get(url + "api/bet_history").json())

    print("Transaction history Valid:", bot.get(url + "api/transaction_history").json())

    print("Get notifications:", bot.get(url + "api/get_notifications").json())



if __name__ == '__main__':
    if "-a" in sys.argv:
        # test_all()
        #testssss()
        test_2_fase()
    else:
        cmd()
