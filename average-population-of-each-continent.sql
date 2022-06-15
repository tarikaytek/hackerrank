
SELECT continent, FLOOR(AVG(CITY.population))
FROM COUNTRY
JOIN CITY ON COUNTRY.code = CITY.countrycode
GROUP BY COUNTRY.continent
