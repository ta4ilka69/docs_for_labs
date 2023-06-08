EXPLAIN ANALYZE
SELECT
    ИМЯ,
    ДАТА
FROM
    Н_ЛЮДИ
    LEFT JOIN Н_СЕССИЯ ON Н_ЛЮДИ.ИД = Н_СЕССИЯ.ЧЛВК_ИД
WHERE
    ФАМИЛИЯ > 'Петров'
    AND Н_СЕССИЯ.ДАТА < '2012-01-25'
    AND Н_СЕССИЯ.ДАТА < '2004-01-17';