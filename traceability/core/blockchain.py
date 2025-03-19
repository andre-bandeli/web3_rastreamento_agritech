from web3 import Web3
from datetime import datetime

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    raise Exception("Falha ao conectar ao Ganache")

contract_address = " "

contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "string",
                "name": "numeroLote",
                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "dataProducaoAbate",
                "type": "uint256"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "granjaOrigem",
                "type": "string"
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "empresaProdutora",
                "type": "string"
            }
        ],
        "name": "LoteRegistrado",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_numeroLote",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "_dataProducaoAbate",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "_granjaOrigem",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "_empresaProdutora",
                "type": "string"
            }
        ],
        "name": "registrarLote",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "_numeroLote",
                "type": "string"
            }
        ],
        "name": "consultarLote",
        "outputs": [
            {
                "components": [
                    {
                        "internalType": "string",
                        "name": "numeroLote",
                        "type": "string"
                    },
                    {
                        "internalType": "uint256",
                        "name": "dataProducaoAbate",
                        "type": "uint256"
                    },
                    {
                        "internalType": "string",
                        "name": "granjaOrigem",
                        "type": "string"
                    },
                    {
                        "internalType": "string",
                        "name": "empresaProdutora",
                        "type": "string"
                    }
                ],
                "internalType": "struct Traceability.Lote",
                "name": "",
                "type": "tuple"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "name": "lotes",
        "outputs": [
            {
                "internalType": "string",
                "name": "numeroLote",
                "type": "string"
            },
            {
                "internalType": "uint256",
                "name": "dataProducaoAbate",
                "type": "uint256"
            },
            {
                "internalType": "string",
                "name": "granjaOrigem",
                "type": "string"
            },
            {
                "internalType": "string",
                "name": "empresaProdutora",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

private_key = " "
account_address = " "

def registrar_lote_na_blockchain(numero_lote, data_producao_abate, granja_origem, empresa_produtora):

    data_producao_abate_datetime = datetime.combine(data_producao_abate, datetime.min.time())
    data_producao_abate_timestamp = int(data_producao_abate_datetime.timestamp())

    nonce = web3.eth.get_transaction_count(account_address)
    txn = contract.functions.registrarLote(
        numero_lote,
        data_producao_abate_timestamp,
        granja_origem,
        empresa_produtora
    ).build_transaction({
        'chainId': 1337,
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt