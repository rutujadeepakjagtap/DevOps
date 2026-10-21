-- PostgreSQL Initialization Schema
-- DevOps Assignment 05
-- Student: Rutuja Deepak Jagtap | PRN: 123B1B146 | PCCOE Pune

CREATE TABLE IF NOT EXISTS visits (
    id SERIAL PRIMARY KEY,
    visited_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    client_ip VARCHAR(50) NOT NULL
);

-- Seed initial record for test verification
INSERT INTO visits (client_ip) VALUES ('127.0.0.1');
