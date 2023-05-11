WITH mm1 AS (SELECT id, avg(int_m) as avg_m1
             FROM (SELECT id, m::integer as int_m
                   FROM (SELECT "ЧЛВК_ИД" as id, "ОЦЕНКА" AS m
                         FROM "Н_ВЕДОМОСТИ"
                         WHERE "ЧЛВК_ИД" IN (SELECT "ЧЛВК_ИД"
                                             FROM "Н_УЧЕНИКИ"
                                             WHERE "ГРУППА" = '4100')
                           AND "ОЦЕНКА" IN ('2', '3', '4', '5')) as m1(id, m)) as m1
             GROUP BY id),
     mm2 AS (SELECT id, avg(int_m) as avg_m2
             FROM (SELECT id, m::integer as int_m
                   FROM (SELECT "ЧЛВК_ИД" as id, "ОЦЕНКА" AS m
                         FROM "Н_ВЕДОМОСТИ"
                         WHERE "ЧЛВК_ИД" IN (SELECT "ЧЛВК_ИД"
                                             FROM "Н_УЧЕНИКИ"
                                             WHERE "ГРУППА" = '3100')
                           AND "ОЦЕНКА" IN ('2', '3', '4', '5')) as m2(id, m)) as m2
             GROUP BY id)

SELECT "ФАМИЛИЯ", "ИМЯ", "ОТЧЕСТВО", avg_m1
FROM mm1
         INNER JOIN "Н_ЛЮДИ" ON "Н_ЛЮДИ"."ИД" IN (SELECT "ЧЛВК_ИД" FROM "Н_УЧЕНИКИ" WHERE "ЧЛВК_ИД" = id)
WHERE EXISTS(SELECT 1 FROM mm2 WHERE avg_m1 = avg_m2);