create table Н_ЛЮДИ(ФАМИЛИЯ text);
insert into Н_ЛЮДИ ("а");
insert into Н_ЛЮДИ ("а");
insert into Н_ЛЮДИ ("а");
insert into Н_ЛЮДИ ("b");
insert into Н_ЛЮДИ ("b");
insert into Н_ЛЮДИ ("c");
SELECT
  COUNT(*)
FROM
  (
    SELECT
      ФАМИЛИЯ
    FROM
      Н_ЛЮДИ
    GROUP BY
      ФАМИЛИЯ
  ) AS UNIQUE_SURNAMES;