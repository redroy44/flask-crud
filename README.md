# flask_crud
Simple REST API for CRUD

## Example calls

### Fill database
```bash
python fill_db.py <db_filename>
```
### Run app
```bash
python app.py <db_filename>
```
### List owners with their cars
```bash
curl -v -X GET http://localhost:8001/
```
### List owners
```bash
curl -v -X GET http://localhost:8001/owners
```
### List cars
```bash
curl -v -X GET http://localhost:8001/cars
```
### Add owner
```bash
curl -v -X POST http://localhost:8001/owners -d "first_name=Test&last_name=Test2&pesel=1234567890123"
```
### Add car
```bash
curl -v -X POST http://localhost:8001/cars -d "brand=Test&model=Test1&number=NO12345&owner=13"
```
### Delete owner
```bash
curl -v -X DELETE http://localhost:8001/owners/<owner_id>
```
### Delete car
```bash
curl -v -X DELETE http://localhost:8001/cars/<car_id>
```
### Update owner
```bash
curl -v -X PUT http://localhost:8001/owners/<owner_id> -d "first_name=Newfirstname&last_name=Newlastname"
```
### Update car
```bash
curl -v -X PUT http://localhost:8001/cars/<car_id> -d "brand=Newbrand"
```
