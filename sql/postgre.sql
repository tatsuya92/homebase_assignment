create database prod_data;
\c prod_data;
create schema iris_plant;
create table iris_plant.iris_plant
(
    id SERIAL primary key,
    sepal_length numeric,
    sepal_width  numeric,
    petal_length numeric,
    petal_width  numeric,
    class        varchar(50),
    created_at timestamp DEFAULT now(),
    modified_at timestamp DEFAULT now()
);

create index iris_plant_class_index
    on iris_plant.iris_plant (class);