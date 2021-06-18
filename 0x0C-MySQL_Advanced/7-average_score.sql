-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student. 

DROP PROCEDURE IF EXISTS computeAverageScoreForUser;
DELIMITER $$


CREATE PROCEDURE computeAverageScoreForUser(user_id INT)

BEGIN
    SET @average = (
    SELECT AVG(score) 
    from corrections c
    where c.user_id = user_id);
    UPDATE users SET average_score = @average WHERE id = user_id;

END $$
DELIMITER ;
