import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Function to generate data for a single row
def generate_row():
    return {
        'Name': fake.name(),
        'Address': fake.address().replace("\n", ", "),
        'Phone Number': fake.phone_number(),
        'Age': random.randint(18, 90),
        'Date of Birth': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat(),
        'SSN': fake.ssn(),
        'Credit Card Number': fake.credit_card_number(),
        'CVC': fake.credit_card_security_code()
    }

# Number of rows you want to generate
NUM_ROWS = 10000

# Generate data
data = [generate_row() for _ in range(NUM_ROWS)]

# Convert list of dicts to DataFrame
df = pd.DataFrame(data)

# Export to CSV
csv_file_path = 'synthetic_data.csv'
df.to_csv(csv_file_path, index=False)

print(f"Data exported to {csv_file_path} with {NUM_ROWS} rows.")
