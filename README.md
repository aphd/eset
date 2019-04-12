# Empirical Study of Ethereum Transactions (ESET)

## Blocks variables

| Attribute	 | Description |
| ------------- | ------------- |
| height  | The height of the block in the blockchain.  |
| fees  | The total number of fees collected by miners in this block.  |
| time | Recorded time at which block was built. Note: Miners rarely post accurate clock times. |
| size | Raw size of block (including header and all transactions) in bytes. |

## Transactions variables

| Attribute	 | Description |
| ------------- | ------------- |
| block_height  | Height of the block that contains this transaction. If this is an unconfirmed transaction, it will equal -1.  |
| hash  | The hash of the transaction. |
| gas_price | The price of gas in this transaction. (Wei) |
| gas_used | The amount of gas used by this transaction. |
| fees | The total number of fees collected by miners in this transaction. Equal to gas_price * gas_used. (Wei) |
| received | Time this transaction was received by a specific mempool server. |
| confirmed | Time at which transaction was included in a block; only present for confirmed transactions. |
| size | The size of the transaction in bytes. |

## EthGasStation variables

| Attribute	 | Description |
| ------------- | ------------- |
| fastest | Gas to pay to have the transaction confirmed within 1 to 2 blocks time |
| fast | - |
| safeLow | - |
| average | - |
| block_time | - |
| blockNum | - |

## Test

```bash 
cd src
python3 -m unittest discover
```

## References

1. https://www.blockcypher.com/dev/ethereum/#blockchain
