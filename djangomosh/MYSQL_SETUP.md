MySQL setup for this Django project

1. Create the database and Django user:

```sql
CREATE DATABASE IF NOT EXISTS storefront
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'storefront_user'@'127.0.0.1'
IDENTIFIED BY 'storefront_password';

GRANT ALL PRIVILEGES ON storefront.* TO 'storefront_user'@'127.0.0.1';
FLUSH PRIVILEGES;
```

2. Run the SQL above with an admin MySQL account:

```bash
sudo mysql
```

3. After that, run Django migrations:

```bash
python manage.py migrate
```

4. The project reads database settings from `.env`:

```env
DB_NAME=storefront
DB_USER=storefront_user
DB_PASSWORD=storefront_password
DB_HOST=127.0.0.1
DB_PORT=3306
```
