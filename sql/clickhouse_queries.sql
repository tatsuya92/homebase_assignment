/*
    How many unique values are in class?
*/

SELECT count() FROM (SELECT DISTINCT class FROM iris_plant);


/*
    What is the average of sepal_length, sepal_width, petal_length, petal_width grouped by class ?
*/

SELECT class, avg(sepal_length), avg(sepal_width), avg(petal_length), avg(petal_width) FROM iris_plant GROUP BY class;