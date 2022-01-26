export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=Deskjet1$
export POSTGRES_DB=security
export POSTGRES_HOST=affiatetracking-db.returnoftm.com
export POSTGRES_PORT=5432
export CONFIG_TYPE=DEVELOPMENT

uvicorn  --access-log   --root-path backend  --reload  --reload-dir app --log-level info "app.main:app"
python3