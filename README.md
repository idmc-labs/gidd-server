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
cat full-db.sql  | docker exec -i old_db_container psql -U postgres -d postgres
```

OR

```bash
cat full-db.sql  | docker-compose exec -T olddb psql -U postgres -d postgres
```

## Migrate old database to new database
```bash
# To migrate old db to new db first change the password of allochi and postgres
# user in olddb
docker-compose exec olddb psql -U postgres
ALTER USER allochi WITH PASSWORD '<default-password-here>';
```

```bash
# Migrate old data
docker-compose exec server python manage.py migrate
docker-compose exec server python manage.py migrate_old_data
```

## Sync data by year
```bash
docker-compose exec server python manage.py sync_data year
# eg docker-compose exec server python manage.py sync_data 2021
```

## Migrate country background images
Download country background images zip file, extract it, and move to media or bucket. Finally run this management command.

```bash
docker-compose exec server python manage.py save_country_images
```

## Aws bucket setup
Add these environment variables in .env file if aws IAM role is used
```bash
ENABLE_AWS_BUCKET=True
AWS_STORAGE_BUCKET_NAME='<aws-bucket-name>'
```

Add these environment variables in .env file if aws IAM role is not used
```bash
ENABLE_AWS_BUCKET=True
AWS_S3_ACCESS_KEY_ID='<your-aws-production-id>'
AWS_S3_SECRET_ACCESS_KEY='<your-aws-secret-key>'
AWS_STORAGE_BUCKET_NAME='<aws-bucket-name>'
```
Migrate good practices
```bash
docker-compose exec server python manage.py migrate_good_practice
```

Init tags
```bash
docker-compose exec server python manage.py init_tags
```

Generate center points from bounds
```bash
docker-compose exec server python manage.py generate_center_points
```
