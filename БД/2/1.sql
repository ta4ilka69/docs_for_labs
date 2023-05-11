select
    НАИМЕНОВАНИЕ,
    ЧЛВК_ИД
from
    Н_ТИПЫ_ВЕДОМОСТЕЙ
    LEFT JOIN Н_ВЕДОМОСТИ ON Н_ТИПЫ_ВЕДОМОСТЕЙ.ИД = Н_ВЕДОМОСТИ.ТВ_ИД
WHERE
    Н_ТИПЫ_ВЕДОМОСТЕЙ.ИД = 1
    AND Н_ВЕДОМОСТИ.ЧЛВК_ИД < 105590;