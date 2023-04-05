# NEW

from flask import Flask, request, session, redirect, url_for, render_template, abort, jsonify
from backend import Backend
import signal
import json
import sys
import os
import logging
import codes


USER = "USERS"
SPECIALIST = "SPECIALISTS"
ADMIN = "ADMINS"

# Create Flask App and Backend
server = Flask("RASBet_server", template_folder="../frontend/templates/")
backend = Backend(db_name="sql.db")



# Server helpers #
def get_nif():
	return session["nif"]

def is_logged_in():
	if session.get("logged_in"):
		return session["logged_in"]
	return None




# Error handlers
@server.errorhandler(404)
def error_handler(e):
	print(request.path)
	print("ERROR 404\n", e)
	return jsonify({"response" : "404", "data" : []})

@server.errorhandler(401)
def error_handler(e):
	print("ERROR 401\n", e)
	return jsonify({"response" : "unauthorized", "data" : []})




# API calls #
@server.route("/api/register_user", methods=["POST"])
def api_register_user():
	if request.method == "POST":
		data = request.get_json()
		print(f">> Register USER\n\tEmail:{data['email']}\n\tUsername:{data['username']}\n\tPassword:{data['password']}")
		response, nif = backend.register(USER, data["nif"], data["username"], data["email"], data["password"])
		if response == codes.VALID_USER:
			session["nif"] = nif
			session["logged_in"] = USER
		return jsonify({"response" : response})
	return abort(404)


@server.route("/api/register_specialist", methods=["POST"])
def api_register_specialist():
	if request.method == "POST":
		data = request.get_json()
		print(f">> Register SPECIALIST\n\tEmail:{data['email']}\n\tUsername:{data['username']}\n\tPassword:{data['password']}")
		if data["token"] != "specialist_token":
			return jsonify({"response" : "token_error"})
		response, nif = backend.register(SPECIALIST, data["nif"], data["username"], data["email"], data["password"])
		if response == codes.VALID_SPECIALIST:
			session["nif"] = nif
			session["logged_in"] = SPECIALIST
		return jsonify({"response" : response})
	return abort(404)


@server.route("/api/register_admin", methods=["POST"])
def api_register_admin():
	if request.method == "POST":
		data = request.get_json()
		print(f">> Register ADMIN\n\tEmail:{data['email']}\n\tUsername:{data['username']}\n\tPassword:{data['password']}")
		if data["token"] != "admin_token":
			return jsonify({"response" : "token_error"})
		response, nif = backend.register(ADMIN, data["nif"], data["username"], data["email"], data["password"])
		if response == codes.VALID_ADMIN:
			session["nif"] = nif
			session["logged_in"] = ADMIN
		return jsonify({"response" : response})
	return abort(404)



@server.route("/api/login", methods=["GET", "POST"])
def api_login():
    if request.method == "GET":
        ili = is_logged_in()
        if ili == USER: return jsonify({"response" : "user", "username" : backend.get_username(get_nif(), USER)})
        elif ili == ADMIN: return jsonify({"response" : "admin", "username" : backend.get_username(get_nif(), ADMIN)})
        elif ili == SPECIALIST: return jsonify({"response" : "specialist", "username" : backend.get_username(get_nif(), SPECIALIST)})
        else: return jsonify({"response" : "logged_out"})
    elif request.method == "POST":
        data = request.get_json()
        print(">> Login:", data["username"])
        response, nif = backend.login(data["username"], data["password"])
        if response == codes.VALID_USER:
            session["nif"] = nif
            session["logged_in"] = USER
        elif response == codes.VALID_SPECIALIST:
            session["nif"] = nif
            session["logged_in"] = SPECIALIST
        elif response == codes.VALID_ADMIN:
            session["nif"] = nif
            session["logged_in"] = ADMIN
        return jsonify({"response" : response})
    return abort(404)


@server.route("/api/logout", methods=["POST"])
def api_logout():
	if request.method == "POST":
		try:
			print(">> Logout", session["nif"])
			session.pop("nif", "")
			session.pop("logged_in", "")
		except:
			pass
		return jsonify({"response" : "logged_out"})
	return abort(404)


@server.route("/api/edit_profile", methods=["POST"])
def api_edit_profile():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Edit profile")
			data = request.get_json()
			response = backend.edit_profile(get_nif(), data["username"], data["email"], data["password"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/get_user_data", methods=["GET"])
def api_get_user_data():
	if request.method == "GET":
		if is_logged_in() == USER:
			print(">> Get user data")
			response, data = backend.get_user_data(get_nif())
			return jsonify({"response" : response, "data" : data})
		else: abort(401)
	return abort(404)


@server.route("/api/withdraw_money", methods=["POST"])
def api_withdraw_money():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Withdraw money")
			data = request.get_json()
			response = backend.withdraw_money(get_nif(), data["amount"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/deposit_money", methods=["POST"])
def api_deposit_money():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Deposit money")
			data = request.get_json()
			response = backend.deposit_money(get_nif(), data["amount"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/bet", methods=["POST"])
def api_bet():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Place a bet")
			data = request.get_json()
			response = backend.bet(get_nif(), data["game_ids"], data["betted_results"], float(data["amount"]))
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/cash_out", methods=["POST"])
def api_cash_out():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Cash out")
			data = request.get_json()
			response = backend.cash_out(get_nif(), data["bet_id"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/bet_history", methods=["GET"])
def api_bet_history():
	if request.method == "GET":
		if is_logged_in() == USER:
			print(">> Bet history")
			response, data = backend.bet_history(get_nif())
			return jsonify({"response" : response, "data" : data})
		else: abort(401)
	return abort(404)


@server.route("/api/transaction_history", methods=["GET"])
def api_transaction_history():
	if request.method == "GET":
		if is_logged_in() == USER:
			print(">> Transaction history")
			response, data = backend.transaction_history(get_nif())
			return jsonify({"response" : response, "data" : data})
		else: abort(401)
	return abort(404)


@server.route("/api/get_notifications", methods=["GET"])
def api_get_notifications():
	if request.method == "GET":
		if is_logged_in() == USER:
			print(">> Get notifications")
			response, data = backend.get_notifications(get_nif())
			return jsonify({"response" : response, "data" : data})
		else: abort(401)
	return abort(404)


@server.route("/api/get_active_games/<sport>", methods=["GET"])
def api_get_active_games(sport):
	if request.method == "GET":
		if is_logged_in() == USER:
			print(">> Get active games")
			if sport == "football":
				response, data = backend.get_games("FOOTBALL", state="ACTIVE")
				return jsonify({"response" : response, "data" : data})
			else: return jsonify({"response" : "unknown_sport"})
		else: abort(401)
	return abort(404)


@server.route("/api/follow_game", methods=["POST"])
def api_follow_game():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Follow game")
			data = request.get_json()
			response = backend.follow_game(get_nif(), data["game_id"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/unfollow_game", methods=["POST"])
def api_unfollow_game():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Unfollow game")
			data = request.get_json()
			response = backend.unfollow_game(get_nif(), data["game_id"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/check_follows_game", methods=["POST"])
def api_check_follows_game():
	if request.method == "POST":
		if is_logged_in() == USER:
			print(">> Unfollow game")
			data = request.get_json()
			response, data = backend.check_follows_game(get_nif(), data["game_id"])
			return jsonify({"response" : response, "data" : data})
		else: abort(401)
	return abort(404)


@server.route("/api/get_wait_games/<sport>", methods=["GET"])
def api_get_wait_games(sport):
	if request.method == "GET":
		if is_logged_in() == SPECIALIST or is_logged_in() == ADMIN:
			print(">> Get wait games")
			if sport == "football":
				response, data = backend.get_games_and_outcomes("FOOTBALL")
				return jsonify({"response" : response, "data" : data})
			else: return jsonify({"response" : "unknown_sport"})
		else: abort(401)
	return abort(404)


@server.route("/api/get_all_games/<sport>", methods=["GET"])
def api_get_all_games(sport):
	if request.method == "GET":
		if is_logged_in() == ADMIN:
			print(">> Get all games")
			if sport == "football":
				response, data = backend.get_games("FOOTBALL", state="ANY")
				return jsonify({"response" : response, "data" : data})
			else: return jsonify({"response" : "unknown_sport"})
		else: abort(401)
	return abort(404)


@server.route("/api/set_games_odds", methods=["POST"])
def api_set_games_odds():
	if request.method == "POST":
		if is_logged_in() == SPECIALIST or is_logged_in() == ADMIN:
			print(">> Set games odds")
			data = request.get_json()
			response = backend.set_games_odds("FOOTBALL", data["ids"], data["odds"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


#####
@server.route("/api/set_games_states", methods=["POST"])
def api_set_games_states():
	if request.method == "POST":
		if is_logged_in() == ADMIN:
			print(">> Set games states")
			data = request.get_json()
			response = backend.set_games_states("FOOTBALL", data["ids"], data["states"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


@server.route("/api/options", methods=["GET", "POST"])
def api_edit_options():
	if is_logged_in() == ADMIN:
		if request.method == "POST":
			print(">> Set options")
			data = request.get_json()
			response = backend.set_option(data["option"], data["value"])
			return jsonify({"response" : response})
		elif request.method == "GET":
			print(">> Get options")
			response, data = backend.get_options()
			return jsonify({"response" : response, "data" : data})
		else: return abort(404)
	else: abort(401)


@server.route("/api/notify_all", methods=["POST"])
def api_notify_all():
	if request.method == "POST":
		if is_logged_in() == ADMIN:
			data = request.get_json()
			response = backend.notify_all(data["message"])
			return jsonify({"response" : response})
		else: abort(401)
	return abort(404)


def exit():
	print(">> Closing server")
	sys.exit(0)


def run_server():
	logging.getLogger('werkzeug').setLevel(logging.ERROR)
	signal.signal(signal.SIGINT, lambda x, y: exit())

	time_interval = 60
	if "-rs" in sys.argv: backend.reset_specialists()
	if "-ro" in sys.argv: backend.reset_options()
	if "-ra" in sys.argv: backend.reset_admins()
	if "-ru" in sys.argv: backend.reset_users()
	if "-rg" in sys.argv: backend.reset_games()
	if any(["-apitimeout=" in v for v in sys.argv]): backend.set_api_timeout(int(sys.argv[["-apitimeout=" in v for v in sys.argv].index(True)][12:]))
	if any(["-updatetime=" in v for v in sys.argv]): time_interval = int(sys.argv[["-updatetime=" in v for v in sys.argv].index(True)][12:])
	
	backend.start_update_cycle(time_interval=time_interval)

	backend.register(ADMIN, "000000000", "admin", "admin@rasbet.com", "Admin123")

	server.secret_key = os.urandom(12)

	if "-ssl" in sys.argv:
		server.run(ssl_context='adhoc', host="0.0.0.0", port=8080, debug=True, use_reloader=False)
	else:
		server.run(host="0.0.0.0", port=8080, debug=True, use_reloader=False, threaded=True)

	backend.join_update_cycle()


@server.after_request
def add_header(response):
	response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'
	response.headers['Content-Type'] = 'application/json'
	response.headers["Access-Control-Allow-Methods"]= 'OPTIONS,POST,GET'
	response.headers["Access-Control-Allow-Headers"] = 'origin, x-requested-with, content-type'
	response.headers['Access-Control-Allow-Credentials'] = 'true'
	return response

if __name__ == '__main__':
	run_server()
