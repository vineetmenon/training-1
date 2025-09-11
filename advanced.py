from faker import Faker
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt

# initialize faker
fake = Faker()

# number of samples
n = 200

# generate dataset
data = []
for _ in range(n):
    # skewed age: normal distribution centered at 40, sd=10, clipped between 18–80
    age = int(np.clip(np.random.normal(loc=40, scale=10), 18, 80))
    
    gender = random.choice(["Male", "Female"])    # gender
    target_y = random.choice(["Yes", "No"])       # label
    fico_score = random.randint(300, 850)         # FICO score
    city = fake.city()
    state = fake.state_abbr()                     # two-letter state code
    
    # credit card details
    credit_card_number = fake.credit_card_number(card_type=None)
    credit_limit = random.randint(1000, 20000)
    
    # Weighted usage distribution
    usage_bucket = random.choices(
        population=["low", "medium", "high"],
        weights=[0.6, 0.3, 0.1],  # 60% low, 30% medium, 10% high
        k=1
    )[0]
    
    if usage_bucket == "low":
        usage = np.random.uniform(0, 30)    # mostly <30%
    elif usage_bucket == "medium":
        usage = np.random.uniform(30, 70)   # 30–70%
    else:
        usage = np.random.uniform(70, 100)  # 70–100%
    
    usage = round(usage, 2)
    outstanding_balance = int(credit_limit * usage / 100)
    
    data.append({
        "id": fake.uuid4(),
        "age": age,
        "gender": gender,
        "fico_score": fico_score,
        "city": city,
        "state": state,
        "credit_card_number": credit_card_number,
        "credit_limit": credit_limit,
        "outstanding_balance": outstanding_balance,
        "usage_percent": usage,
        "target_y": target_y
    })

# convert to dataframe
df = pd.DataFrame(data)

# quick preview
print(df.head())

# Plot distributions
plt.figure(figsize=(20, 5))

# Age distribution
plt.subplot(1, 4, 1)
df['age'].plot(kind='hist', bins=15, edgecolor='black')
plt.title("Distribution of Age (Skewed 25–55)")
plt.xlabel("Age")
plt.ylabel("Count")

# FICO score distribution
plt.subplot(1, 4, 2)
df['fico_score'].plot(kind='hist', bins=20, edgecolor='black')
plt.title("Distribution of FICO Score")
plt.xlabel("FICO Score")
plt.ylabel("Count")

# Usage percent distribution
plt.subplot(1, 4, 3)
df['usage_percent'].plot(kind='hist', bins=20, edgecolor='black')
plt.title("Distribution of Usage Percent")
plt.xlabel("Usage %")
plt.ylabel("Count")

# Target_y distribution
plt.subplot(1, 4, 4)
df['target_y'].value_counts().plot(kind='bar')
plt.title("Distribution of Target (Yes/No)")
plt.xlabel("Label")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
