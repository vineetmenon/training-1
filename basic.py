from faker import Faker
import pandas as pd
import random
import matplotlib.pyplot as plt

# initialize faker
fake = Faker()

# number of samples
n = 200

# generate dataset
data = []
for _ in range(n):
    age = random.randint(18, 80)                  # random age
    gender = random.choice(["Male", "Female"])    # gender
    target_y = random.choice(["Yes", "No"])       # label
    fico_score = random.randint(300, 850)         # FICO score
    city = fake.city()
    state = fake.state_abbr()                     # two-letter state code
    
    data.append({
        "id": fake.uuid4(),
        "age": age,
        "gender": gender,
        "fico_score": fico_score,
        "city": city,
        "state": state,
        "target_y": target_y
    })

# convert to dataframe
df = pd.DataFrame(data)

# TODO - show data frame sttistics

# Plot distributions
plt.figure(figsize=(18, 5))

# Age distribution
plt.subplot(1, 4, 1)
df['age'].plot(kind='hist', bins=15, edgecolor='black')
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Count")

# Gender distribution
plt.subplot(1, 4, 2)
df['gender'].value_counts().plot(kind='bar')
plt.title("Distribution of Gender")
plt.xlabel("Gender")
plt.ylabel("Count")

# FICO score distribution
plt.subplot(1, 4, 3)
df['fico_score'].plot(kind='hist', bins=20, edgecolor='black')
plt.title("Distribution of FICO Score")
plt.xlabel("FICO Score")
plt.ylabel("Count")

# Target_y distribution
plt.subplot(1, 4, 4)
df['target_y'].value_counts().plot(kind='bar')
plt.title("Distribution of Target (Yes/No)")
plt.xlabel("Label")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
