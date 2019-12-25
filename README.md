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

## Cron/Job scheduler 
```bash 
* * * * * cd ~/github/eset/src/; export PYTHONPATH="${PYTHONPATH}:app"; FN=fetch_oracle.py; /usr/bin/python3.6 app/$FN >> /tmp/$FN.log 2>&1
```

## A descriptive analysis

The dataset is available to this <a href="https://www.dropbox.com/sh/r26h69swgyz9z75/AADeFqXchK5jqLjBzfKjeCsDa?dl=0">link</a>.

### Oracles data analysis

```bash
bunzip2 block.csv.bz2
```

```python 
import pandas as pd
df = pd.read_csv('oracle.csv')
df['egs'] = df['egs']/10
oracles = pd.DataFrame({'Ether Chain':df["ec"], 'Ether Gas Station': df["egs"]})
print(((oracles.describe()).transpose()).to_latex())
```

![table-latex](https://user-images.githubusercontent.com/1194257/69806671-baf3a700-11e3-11ea-837d-6a42525116b8.jpg)

```python 
import pandas as pd
import seaborn as sns
df = pd.read_csv('oracle.csv')
ec_oracle = pd.DataFrame({'Gas Price (GWei)':df["ec"], 'Oracles': 'Ether Chain'})
egs_oracle = pd.DataFrame({'Gas Price (GWei)':df["egs"]/10, 'Oracles': 'Ether Gas Station'})
oracles = ec_oracle.append(egs_oracle)
sns.set(style="whitegrid", rc={'figure.figsize':(7,8)})
ax = sns.violinplot( x="Oracles" ,  y="Gas Price (GWei)", data=oracles)
```

![violin-plot](https://user-images.githubusercontent.com/1194257/69805030-1459d700-11e0-11ea-8867-d6a393c0e6c0.png)

```python
import pandas as pd
df =pd.read_csv('/tmp/egsOracle.csv')

df['fastest'] = df['fastest']/10
df['fast'] = df['fast']/10
df['safeLow'] = df['safeLow']/10
df['average'] = df['average']/10

egs_fastest = pd.DataFrame({'y':df["fastest"], 'x': 'fastest'})
egs_fast = pd.DataFrame({'y':df["fast"], 'x': 'fast'})
egs_safeLow = pd.DataFrame({'y':df["safeLow"], 'x': 'safeLow'})
egs_average = pd.DataFrame({'y':df["average"], 'x': 'average'})

sns.set(style="whitegrid", rc={'figure.figsize':(30,8)})
ax = sns.violinplot( x="x" , y="y", data=egs_categories)
```

![categories violin plots](https://user-images.githubusercontent.com/1194257/69956244-c0acfd80-14ff-11ea-82fb-b805a31f0952.jpg)

### Transactions data analysis

```bash
bunzip2 txs.csv.bz2
```

```python 
import pandas as pd
import seaborn as sns
```

```python 
df = pd.read_csv('txs.csv')
df = df[df.waiting_time > 15] # a tx needs to wait at least 1 block equals to 15 seconds
df = df[df.waiting_time < 150] # outliners set to txs waiting more than 30 blocks
df = df[df.gas_price < 10]
txs_less_10 = pd.DataFrame({'Waiting time (sec)': df["waiting_time"], 'x': 'Gas Price < 10 Gwei'})


df = pd.read_csv('txs.csv')
df = df[df.waiting_time > 15] # a tx needs to wait at least 1 block equals to 15 seconds
df = df[df.waiting_time < 150] # outliners set to txs waiting more than 30 blocks
df = df[df.gas_price > 10]
txs_greater_10 = pd.DataFrame({'Waiting time (sec)': df["waiting_time"], 'x': 'Gas Price > 10 Gwei'})

ax = sns.violinplot( y="Waiting time (sec)" , x="x", data=txs_less_10.append(txs_greater_10))
```

![tx-confirmation-time-vs-gas-price](https://user-images.githubusercontent.com/1194257/69864238-c2c45180-129e-11ea-8aef-f7008d2c255c.png)

```python 
df = pd.read_csv('block.csv')

x=(df['fees']/10e+9)
x.describe()

ax = sns.boxplot(x)
ax.set_xscale("log")
```

### Block data analysis

To calculate the block_time from the received_time variable of block, I calculated the difference between previous and current row.

```sql
SELECT
    height , received_time, fees, size, n_tx, lowest_gas_price,
    received_time - LAG ( received_time, 1, 0 ) OVER ( ORDER BY height ) block_time ,
    height - LAG ( height, 1, 0 ) OVER ( ORDER BY height ) height_diff
FROM
    block 

LIMIT 10
OFFSET 1;

SELECT
    received_time, height, fees, size, n_tx, lowest_gas_price, block_time
FROM
    block
ORDER BY height
LIMIT 10
OFFSET 1;
```

### Generate descriptive statistics in latex

```python 
import pandas as pd

df = pd.read_csv('txs.csv')

print(((df.describe()).transpose()).to_latex())

# to suppress scientific notation
print(((df.describe().apply(lambda s: s.apply(lambda x: format(x, 'g')))).transpose()).to_latex())
```

## References

1. https://www.blockcypher.com/dev/ethereum/#blockchain
2. https://www.etherchain.org/
