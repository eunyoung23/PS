SELECT HOUR(DATETIME)"HOUR",COUNT(HOUR(DATETIME))"COUNT" FROM ANIMAL_OUTS WHERE HOUR(DATETIME)>=9 AND HOUR(DATETIME)<=19 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME);
