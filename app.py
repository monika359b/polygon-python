######### MODULES
from web3 import Web3,HTTPProvider
from web3.middleware import geth_poa, geth_poa_middleware
import json
from flask import Flask,request

######### SETTING OBJECTS
polygon = "https://polygon-rpc.com/"
web3 = Web3(Web3.HTTPProvider(polygon))
app = Flask(__name__)
private_key = "d926b8639fbae31c2a42e726f52619868453ef1eaf6a88ea3f2867c409fcab94"
mainAddress = "0x742550CfD9E7445C227F239A19483501C70b03e7"
contract_address = '0x7980F17C12974cDa8c34dfA9148DC6dD26FF79db' 
abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"spender","type":"address"},{"name":"tokens","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"_totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeSub","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"tokens","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeDiv","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeMul","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[{"name":"tokenOwner","type":"address"},{"name":"spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"uint256"}],"name":"safeAdd","outputs":[{"name":"c","type":"uint256"}],"payable":false,"stateMutability":"pure","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"tokenOwner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"tokens","type":"uint256"}],"name":"Approval","type":"event"}]')
contract = web3.eth.contract(address=contract_address, abi=abi)

totalSupply = contract.functions.totalSupply().call()

nonce = web3.eth.getTransactionCount(mainAddress)
######## SETTING UP FUNCTION
def sendToken(to, value):
  nonce = web3.eth.getTransactionCount(mainAddress)
  amo = web3.toWei(value, 'ether')
  tx = contract.functions.transfer(to, amo).buildTransaction({
    'chainId':137, 'gas': 50000,'gasPrice': web3.toWei('3','gwei'), 'nonce':nonce
})
  sign_tx = web3.eth.account.signTransaction(tx, private_key)
  tran_hash = web3.eth.sendRawTransaction(sign_tx.rawTransaction)
  txn = web3.toHex(tran_hash)
  return txn

####### CREATEING API
@app.route('/')
def setuphandler():
	nonce = web3.eth.getTransactionCount(mainAddress)
	return str(nonce)

@app.route('/sendToken', methods = ['POST'])
def sendZilHandler():
	index = request.json
	address = index["address"]
	amount = index["amount"]
	tx = sendToken(address, amount)
	return tx
