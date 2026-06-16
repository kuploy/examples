# kuploy/examples

Ready-to-deploy example apps for [Kuploy Stacks](https://docs.kuploy.app/tutorials).
Each subdirectory is a self-contained "visit counter" web app + a database,
wired together as a Stack (the platform injects the DB credentials).

| Dir | Stack | Connection |
|-----|-------|-----------|
| `flask-postgres`   | Python Flask + PostgreSQL | `connectionString` → `DATABASE_URL` |
| `django-postgres`  | Django + PostgreSQL       | `connectionString` → `DATABASE_URL` |
| `express-postgres` | Node Express + PostgreSQL | `connectionString` → `DATABASE_URL` |
| `php-mysql`        | PHP + MySQL               | `host`/`user`/`password`/`database` → `DB_*` |

Point a Kuploy **Application** component at the relevant subdirectory (set the
build path to the subdir), add the matching database, connect them, and deploy.
See the per-language tutorials at https://docs.kuploy.app/tutorials.
