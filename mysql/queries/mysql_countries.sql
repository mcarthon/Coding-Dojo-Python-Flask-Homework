USE world;

SELECT country.Name AS Country,
	   countryLanguage.Language AS Language,
       countryLanguage.Percentage AS "Language Percentage"
FROM
country JOIN countryLanguage
ON country.Code = countryLanguage.CountryCode
WHERE countryLanguage.Language = "Slovene"
ORDER BY countryLanguage.Percentage DESC;

SELECT country.Name AS Country,
       COUNT(city.Name) AS City_Count
FROM
country JOIN city
ON country.code = city.CountryCode
GROUP BY Country
ORDER BY City_Count DESC;

SELECT city.Name,
       city.Population
FROM 
country JOIN city
ON country.Code = city.CountryCode
WHERE city.CountryCode = "MEX"
AND city.Population > 500000
ORDER BY city.Population DESC;     

SELECT countrylanguage.Language
FROM countrylanguage     
WHERE countrylanguage.Percentage > 89
ORDER BY countrylanguage.Percentage DESC;

SELECT Name,
       SurfaceArea,
       Population
FROM country
WHERE Population > POWER(10, 5)
AND SurfaceArea < 501
ORDER BY Population DESC, SurfaceArea ASC;

SELECT Name,
	   GovernmentForm,
       Capital,
       LifeExpectancy
FROM country
WHERE GovernmentForm LIKE "%con%"
AND LifeExpectancy > 75
AND Capital > 200
ORDER BY Capital DESC,
		 LifeExpectancy DESC;

SELECT country.Name,
	   city.Name,
	   city.District,
       city.Population
FROM 
country JOIN city
ON country.Code = city.CountryCode
WHERE city.District = "Buenos Aires"
AND city.Population > 500000
ORDER BY city.Population DESC,
		 city.Name;
         
SELECT Region,
	   COUNT(Name) AS RegionCount
FROM country
GROUP BY Region
ORDER BY RegionCount DESC;