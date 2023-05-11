With average AS (SELECT id, avg(int_m) as avg_m2
                 FROM (SELECT id, CAST(m AS INTEGER) as int_m
                       FROM (SELECT "ЧЛВК_ИД" as id, "ОЦЕНКА" AS m
                             FROM "Н_ВЕДОМОСТИ"
                             WHERE "ЧЛВК_ИД" IN (SELECT "ЧЛВК_ИД"
                                                 FROM "Н_УЧЕНИКИ"
                                                 WHERE "ПЛАН_ИД" in (SELECT "ПЛАН_ИД" FROM "Н_ПЛАНЫ" WHERE "ОТД_ИД"=703))
                               AND "ОЦЕНКА" IN ('2', '3', '4', '5')) as m2(id, m)) as m2
                 GROUP BY id)

SELECT count(id)
FROM average
WHERE avg_m2 >= 2.5
  AND avg_m2 <= 3.5;