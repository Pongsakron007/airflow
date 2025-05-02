-- scripts/init_db.sql
CREATE TABLE IF NOT EXISTS gold_price (
    id SERIAL PRIMARY KEY,
    price NUMERIC,
    fetched_at TIMESTAMP
);
