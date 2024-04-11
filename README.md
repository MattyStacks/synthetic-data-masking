# synthetic-data-masking
Python synthetic data masking using faker to generate the synthetic data.


## What's the point?

There are a ton of ways to mask data. The thing though is that most of these masking methods return things like hashes that don't look great when looking at the data. 

What I wanted was a way to mask data then to have it look readable. 

What happens is that python program reads in a file. Then it hashes the value of the cell that you want to obfuscate. After that it takes that value and uses it as a seed for faker.

One thing I did was made sure that the hashed value also gets salted so that it isn't reverseable even between runs.

## How to get started

### Create python virtualenv

```
python -m venv .venv
```

Activate your enviornment.

```
./.venv/Scripts/activate
```

Install your requirements.

```
pip install -r requirements.txt
```