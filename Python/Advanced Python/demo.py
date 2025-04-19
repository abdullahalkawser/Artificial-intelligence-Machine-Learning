print('hellow advance python')

import requests
import threading
import logging
import json
from contextlib import contextmanager
from time import sleep
from random import randint

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(threadName)s - %(message)s')

# Context manager for timing
@contextmanager
def timer(name):
    import time
    start = time.time()
    yield
    end = time.time()
    logging.info(f'{name} took {end - start:.2f} seconds')

# Decorator to retry a function on failure
def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.warning(f'Attempt {i+1} failed: {e}')
                    sleep(1)
            raise Exception(f'All {times} attempts failed.')
        return wrapper
    return decorator

# Generator to yield fake user IDs
def user_id_generator(start=1, end=10):
    for i in range(start, end + 1):
        yield i

# API Client Class
class APIClient:
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    @retry(3)
    def fetch_user(self, user_id):
        url = f'{self.BASE_URL}/users/{user_id}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    @retry(3)
    def fetch_posts_by_user(self, user_id):
        url = f'{self.BASE_URL}/posts?userId={user_id}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

# Worker function to be used by threads
def worker(user_id, client: APIClient):
    logging.info(f'Starting to fetch for User ID {user_id}')
    user_data = client.fetch_user(user_id)
    posts = client.fetch_posts_by_user(user_id)

    filename = f'user_{user_id}.json'
    with open(filename, 'w') as f:
        json.dump({
            "user": user_data,
            "posts": posts
        }, f, indent=2)

    logging.info(f'Finished writing data for User ID {user_id}')

# Main controller
def main():
    client = APIClient()
    threads = []

    with timer("Total Execution"):
        for user_id in user_id_generator(1, 5):
            t = threading.Thread(target=worker, args=(user_id, client))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

if __name__ == "__main__":
    main()
