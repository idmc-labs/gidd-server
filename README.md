# Gidd Server

## Run development server:
Clone project form git and go to project directory

Copy .env.example file to .env
```bash
cp .env.example .env
```

Build and run docker
```bash
docker-compose up --build
```

## Import old db dump
```bash
cat full-db.sql  | docker exec -i old_db_container psql -U postgres
```
OR

```bash
cat full-db.sql  | docker-compose exec olddb psql -U postgres
```

## To migrate old db to new db
```bash
docker-compose exec server python manage.py migrate_old_data
```
