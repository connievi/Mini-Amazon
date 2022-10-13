from werkzeug.security import generate_password_hash
import csv
from faker import Faker

num_users = 100
num_products = 2000
num_purchases = 2500
num_reviews = 500

Faker.seed(0)
fake = Faker()


def get_csv_writer(f):
    return csv.writer(f, dialect='unix')


def gen_users(num_users):
    with open('Users.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Users...', end=' ', flush=True)
        for uid in range(num_users):
            if uid % 10 == 0:
                print(f'{uid}', end=' ', flush=True)
            profile = fake.profile()
            email = profile['mail']
            plain_password = f'pass{uid}'
            password = generate_password_hash(plain_password)
            name_components = profile['name'].split(' ')
            firstname = name_components[0]
            lastname = name_components[-1]
            is_seller = fake.random_int(min = 0, max = 1)
            writer.writerow([uid, email, password, firstname, lastname, is_seller])
        print(f'{num_users} generated')
    return


def gen_products(num_products):
    available_pids = []
    with open('Products.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Products...', end=' ', flush=True)
        for pid in range(num_products):
            if pid % 100 == 0:
                print(f'{pid}', end=' ', flush=True)
            name = fake.sentence(nb_words=4)[:-1]
            price = f'{str(fake.random_int(max=500))}.{fake.random_int(max=99):02}'
            available = fake.random_element(elements=('true', 'false'))
            if available == 'true':
                available_pids.append(pid)
            writer.writerow([pid, name, price, available])
        print(f'{num_products} generated; {len(available_pids)} available')
    return available_pids


def gen_purchases(num_purchases, available_pids):
    with open('Purchases.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Purchases...', end=' ', flush=True)
        for id in range(num_purchases):
            if id % 100 == 0:
                print(f'{id}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            pid = fake.random_element(elements=available_pids)
            time_purchased = fake.date_time()
            fulfillment_status = fake.random_int(min = 0, max=1)
            writer.writerow([id, uid, pid, time_purchased, fulfillment_status])
        print(f'{num_purchases} generated')
    return

def gen_reviews(num_reviews, available_pids):
    with open('Reviews.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Reviews...', end=' ', flush=True)
        for id in range(num_reviews):
            if id % 100 == 0:
                print(f'{id}', end=' ', flush=True)
            uid = fake.random_int(min=0, max=num_users-1)
            pid = fake.random_element(elements=available_pids)
            time_submitted = fake.date_time()
            review = fake.sentence()
            rating = fake.random_int(min=1, max=5)
            writer.writerow([id, uid, pid, time_submitted, review, rating])
        print(f'{num_reviews} generated')
    return

def gen_carts(num_users, available_pids):
    with open('Carts.csv', 'w') as f:
        writer = get_csv_writer(f)
        print('Carts...', end=' ', flush=True)
        for id in range(num_users):
            if id % 100 == 0:
                print(f'{id}', end=' ', flush=True)
            sid = fake.random_int(min=0, max=num_users-1)
            pid = fake.random_element(elements=available_pids)
            quantity = fake.random_int(min=1)
            unit_price = fake.random_float(min=0.01)
            writer.writerow([id, sid, pid, quantity, unit_price])
        print(f'{num_users} generated')
    return


gen_users(num_users)
available_pids = gen_products(num_products)
gen_purchases(num_purchases, available_pids)
gen_reviews(num_reviews, available_pids)
gen_carts(num_users, available_pids)