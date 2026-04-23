WITH SCORE AS (SELECT REST_ID, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
              FROM REST_REVIEW
               GROUP BY REST_ID
              ),
              
SEOUL AS (SELECT * FROM REST_INFO
WHERE ADDRESS LIKE '서울%')

SELECT s.rest_id,se.rest_name,se.food_type,se.favorites,se.address,s.score FROM SCORE S JOIN SEOUL SE ON S.REST_ID=SE.REST_ID
order by s.score desc, se.favorites desc