-- Lists all records with score>=10 in the table 'second_table' in DB hbtn_0c_0.

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

