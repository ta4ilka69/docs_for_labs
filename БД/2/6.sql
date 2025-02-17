SELECT
  "ЧЛВК_ИД",
  "ГРУППА",
  "ФАМИЛИЯ",
  "ИМЯ",
  "ОТЧЕСТВО",
  "П_ПРКОК_ИД"
FROM
  "Н_УЧЕНИКИ"
  LEFT JOIN "Н_ЛЮДИ" ON "Н_УЧЕНИКИ"."ЧЛВК_ИД" = "Н_ЛЮДИ"."ИД"
WHERE
  "НАЧАЛО" > '2012-09-01'
  AND "ПРИЗНАК" = 'обучен'
  AND "ПЛАН_ИД" IN (
    SELECT
      "ИД"
    FROM
      "Н_ПЛАНЫ"
    WHERE
      "ФО_ИД" = '1'
      AND "КУРС" = '1'
  );