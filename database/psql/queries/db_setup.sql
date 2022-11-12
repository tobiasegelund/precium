-- CREATE DATABASE precium;

DROP TABLE IF EXISTS companies;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS static;
DROP TABLE IF EXISTS prices;

CREATE TABLE companies (
    company_id INT GENERATED ALWAYS AS IDENTITY,
    company_name VARCHAR(100),
    PRIMARY KEY (company_id)
);

CREATE TABLE items (
    item_id INT GENERATED ALWAYS AS IDENTITY,
    company_id INT,
    external_uid INT,
    CONSTRAINT fk_company_id FOREIGN KEY(company_id) REFERENCES companies(company_id),
    PRIMARY KEY(item_id)
);

CREATE TABLE static (
    item_id INT,
    description VARCHAR,
    brand VARCHAR(100),
    category VARCHAR(100),
    product_main_group VARCHAR(100),
    product_sub_group VARCHAR(100),
    tags VARCHAR,
    unit_price_label VARCHAR(100),
    CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(item_id)
);


CREATE TABLE prices (
    item_id INT,
    base_price FLOAT NOT NULL,
    unit_price FLOAT,
    current_price FLOAT NOT NULL,
    current_unit_price FLOAT,
    discounts FLOAT,
    created TIMESTAMP,
    CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(item_id)
);