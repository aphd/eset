# Empirical Study of Ethereum Transactions (ESET)

## Limitations

Miners rarely post accurate clock times.

## Blocks variables

| Attribute	 | Description |
| ------------- | ------------- |
| confirmed | Recorded time at which block was built. Note: Miners rarely post accurate clock times. |
| height  | The height of the block in the blockchain.  |
| fees  | The total number of fees collected by miners in this block. (GWei)  |
| size | Raw size of block (including header and all transactions) in bytes. |
| n_tx | The number of transactions included in the block. |
| lowest_gas_price |  The lowest gas price accepted by the block. |

## Transactions variables

| Attribute	 | Description |
| ------------- | ------------- |
| block_height  | Height of the block that contains this transaction. If this is an unconfirmed transaction, it will equal -1.  |
| hash  | The hash of the transaction. |
| gas_price | The price of gas in this transaction. (Wei) |
| gas_used | The amount of gas used by this transaction. |
| gas_limit | It is the maximum amount of Gas that a user is willing to pay for confirming a transaction. If not set, default is 21000 gas for external accounts and 80000 gas for contract accounts. |
| fees | The total number of fees collected by miners in this transaction. Equal to gas_price * gas_used. (GWei) |
| received | Time this transaction was received by a specific mempool server. |
| confirmed | Time at which transaction was included in a block; only present for confirmed transactions. |
| size | The size of the transaction in bytes. |

## EthGasStation variables

| Attribute	 | Description |
| ------------- | ------------- |
| timestamp | The time at which the EthGasStation variables are recorded by the server. |
| fastest | Gas to pay to have the transaction confirmed within 1 to 2 blocks time. |
| fast | - |
| safeLow | - |
| average | - |
| blockNum | - |

## Test

```bash 
cd src
export PYTHONPATH="${PYTHONPATH}:app"
cp app/tokens-sample.py app/tokens.py
python3 -m unittest discover
```

## Statistical data visualization

The dataset is available to this <a href="https://www.dropbox.com/sh/r26h69swgyz9z75/AADeFqXchK5jqLjBzfKjeCsDa?dl=0">link</a>.

```bash
bunzip2 txs.csv.bz2
```

```python 
import pandas as pd

df = pd.read_csv('txs.csv')
df.describe()

import seaborn as sns
sns.set(style="whitegrid")

ax = sns.swarmplot(x=df[0:800]["waiting_time"])
ax = sns.violinplot(x=df["waiting_time"],  inner=None) 
ax = sns.kdeplot(df["waiting_time"], shade=True, color="r")
ax = sns.kdeplot(df["waiting_time"], df["gas_price"], shade=True)
```

## References

1. https://www.blockcypher.com/dev/ethereum/#blockchain
2. https://www.etherchain.org/
