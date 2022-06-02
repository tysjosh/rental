# Quick start

1. Make sure you have Python installed.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run `python manage.py runserver` in project root directory to start server
4. Run `python manage.py test` in project root directory to run all tests

### 01. Rental

#### Create:
---
Method: `POST`

Endpoint:

    /api/rentals/

- Create new rental

Payload example
```
{
    "name": "Reval",
}
```

#### Fetch
---
Method: `GET`

Endpoint:

    /api/rentals/

- Shows all Rentals

### 02. Reservation

#### Create:
---
Method: `POST`

Endpoint:

    /api/reservations/

- Create new reservation

Payload example
```
{
    "checkin": "2022-06-01",
    "checkout": "2022-06-02",
    "rental": 1
}
```

#### Fetch
---
Method: `GET`

Endpoint:

    /api/reservations/

- Shows all Reservations
