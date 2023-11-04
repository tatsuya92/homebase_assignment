CREATE DATABASE prod_data;
create table prod_data.iris_plant
(
    id           Int32,
    sepal_length Numeric(2, 1),
    sepal_width  Numeric(2, 1),
    petal_length Numeric(2, 1),
    petal_width  Numeric(2, 1),
    class        String,
    created_at   DateTime,
    modified_at  DateTime
)
    engine = MergeTree
    ORDER BY id
    PRIMARY KEY (id);

ALTER TABLE prod_data.iris_plant ADD INDEX index_class class TYPE minmax GRANULARITY 1;