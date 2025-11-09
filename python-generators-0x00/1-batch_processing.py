# 1-batch_processing.py
import json
import os

# Simulate reading from a database or JSON file of users
# (In real life, you'd fetch from DB cursor or API)
def load_all_users():
    """Simulate loading all users as a list of dictionaries."""
    # pretend this reads from a JSON file
    # example structure for demonstration:
    import random, uuid
    names = ["Zee", "Faith", "Glenda", "Jonathon", "Dan", "Molly", "Alma"]
    users = []
    for _ in range(500):  # simulate 500 users
        users.append({
            "user_id": str(uuid.uuid4()),
            "name": random.choice(names),
            "email": f"user{random.randint(1,999)}@example.com",
            "age": random.randint(10, 120)
        })
    return users


def stream_users_in_batches(batch_size):
    """
    Generator function that yields batches of users.
    Must use yield.
    """
    users = load_all_users()
    for i in range(0, len(users), batch_size):
        yield users[i:i + batch_size]   # yield a batch (list)


def batch_processing(batch_size):
    """
    Process user batches and filter users over age 25.
    """
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                print(user)
