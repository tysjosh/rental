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
