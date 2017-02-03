/******************************************************************************

    Current example realize many-to-many relationship between product and
    customer's purchase order on it in PostgreSQL DBMS.
    +~~~~~~~~~+        +~~~~~~~~~~~~~~~~~~~+        +~~~~~~~~~~~~~~~~~~~+
    |*product*|        |   *order_items*   |        |  *purchase_order* |
    +~~~~~~~~~+        +~~~~~~~~~~~~~~~~~~~+        +~~~~~~~~~~~~~~~~~~~+
    | id      |  _____ | product_id        |    __  | id                |
    +---------+        +-------------------+   /    +-------------------+
    | name    |        | purchase_order_id | _/     | customer_address  |
    +---------+        +-------------------+        +-------------------+
    | price   |
    +---------+

    In this case we use `RESTRICT` and `CASCADE` with *ON DELETE* instruction:

        > RESTRICT -- does not permit delete related row. Difference
            between `RESTRICT` and `NO ACTION` is that `NO ACTION` permit to
            defer verification in transaction process but RESTRICT does not.

        > CASCADE -- in process of deleting related rows, dependent rows will
            be deleted too.

        There two other options: `SET NULL` and `SET DEFAULT`.

            Similarly we have *ON UPDATE* instruction. `CASCADE` in this case
        means that all differences will be copied to dependent rows.

 *****************************************************************************/

CREATE TABLE IF NOT EXISTS product (
    id    SERIAL PRIMARY KEY,
    name  TEXT,
    price NUMERIC
);

CREATE TABLE IF NOT EXISTS purchase_order (
    id              SERIAL PRIMARY KEY,
    customer_addres TEXT
);

CREATE TABLE IF NOT EXISTS order_items (
    product_id        INTEGER NOT NULL REFERENCES product (id)
        ON DELETE RESTRICT,
    purchase_order_id INTEGER NOT NULL REFERENCES purchase_order (id)
        ON DELETE CASCADE,
    PRIMARY KEY (product_id, purchase_order_id)
);