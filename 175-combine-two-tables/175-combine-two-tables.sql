# Write your MySQL query statement below
SELECT firstName, lastName, Address.city, Address.state FROM Person
LEFT JOIN Address ON Address.personId = Person.personId;