import random
from django.contrib.auth.models import User
from finance.models import Transaction
from datetime import datetime, timedelta
from decimal import Decimal

# Dictionary mapping categories to a tuple of (minimum amount, maximum amount).
categories = {
    'general': (100, 150),
    'groceries': (50, 75),
    'shopping': (150, 200),
    'restaurant': (50, 100),
    'transport': (80, 120),
    'travel': (300, 500),
    'entertainment': (100, 200),
    'utilities': (50, 100),
    'health': (100, 150),
    'services': (150, 250),
    'charity': (20, 50)
}

# Dictionary mapping categories to a list of possible descriptions for transactions.
descriptions = {
    # Each category has a list of descriptions that are relevant to the type of transaction.
    'general': [
        "Miscellaneous expenses",
        "General purchase",
        "Random shopping spree"
    ],
    'groceries': [
        "Bought groceries from supermarket",
        "Purchased vegetables and fruits",
        "Weekly grocery shopping"
    ],
    # Add similar description lists for other categories.
}

# Retrieve all users from the database with specific usernames.
users = User.objects.filter(username__in=['Seif', 'Ahmed', 'Fares', 'Jessie', 'Noura'])

# Function to generate a random date within a given year.
def random_date(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Main loop that processes each user.
for user in users:
    for year in [2023, 2024]:  # Loop through each year.
        used_dates = set()  # Track dates to avoid duplicates within the same year.
        for category, (min_amount, max_amount) in categories.items():
            for i in range(2):  # Create two transactions per category per year.
                amount = round(random.uniform(min_amount, max_amount), 2)  # Random amount within the specified range.
                
                while True:
                    transaction_date = random_date(year)  # Generate a random transaction date.
                    if transaction_date not in used_dates:
                        used_dates.add(transaction_date)  # Add to set if not already used.
                        break
                
                description = random.choice(descriptions[category])  # Randomly pick a description for the transaction.
                # Create a new transaction in the database.
                Transaction.objects.create(
                    transaction_date=transaction_date,
                    description=description,
                    amount=Decimal(amount),
                    category=category,
                    user=user
                )
                # Print a confirmation message for each transaction created.
                print(f"Created transaction for {user.username} in {category} on {transaction_date.date()} with description '{description}'")
