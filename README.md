# Gidd Server

## Run development server:
Clone project form git and go to project directory

Copy .env.default file to .env and override there.
```bash
cp .env.default .env
```

Build and run docker
```bash
docker-compose up --build
```

## Setup using old database
### Import old db dump
```bash
cat full-db.sql  | docker exec -i old_db_container psql -U postgres -d postgres
```

OR

```bash
cat full-db.sql  | docker-compose exec -T olddb psql -U postgres -d postgres
```

## Sync data by year
```bash
docker-compose exec server python manage.py sync_data year
# eg docker-compose exec server python manage.py sync_data 2021
```

## Static translation
```bash
# Creation and upkeep language po files (for eg: fr)
docker-compose exec server ./manage.py makemessages -l fr
# Updating current language po files
python3 manage.py makemessages -a
# Compiles .po files to .mo files which will be used by django.
docker-compose exec server ./manage.py compilemessages
```
## Model translation

```bash
docker-compose exec server ./manage.py migrate
# Initialize new language fields (Do this if you don't see previous data)
docker-compose exec server ./manage.py update_translation_fields
# Detect new translatable fields or new available languages and sync database structure. Does not remove columns of removed languages or undeclared fields.
docker-compose exec server ./manage.py sync_translation_fields
```

## Migrate country background images
Download country background images zip file, extract it, and move to media or bucket. Finally run this management command.

```bash
docker-compose exec server python manage.py save_country_images
```

## Load Good Practice success factors.

To add predefined `success_factor` dropdown options using the `load_success_factors` Django management command, follow these steps:

**Run the Management Command:**

   ```bash
   docker-compose exec server python manage.py load_success_factors
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
