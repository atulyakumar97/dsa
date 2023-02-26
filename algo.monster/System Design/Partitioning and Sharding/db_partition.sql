CREATE TABLE IF NOT EXISTS comments
(
  comment_id INT NOT NULL,
  page_id INT NOT NULL,
  user_id INT NOT NULL,
  content TEXT NOT NULL,
  created_time DATETIME NOT NULL
)
PARTITION BY RANGE (year(created_time))
(
  PARTITION p_old VALUES LESS THAN (2019),
  PARTITION p19 VALUES LESS THAN (2020),
  PARTITION p20 VALUES LESS THAN (2021),
  PARTITION p21 VALUES LESS THAN (2022),
  PARTITION p22 VALUES LESS THAN (2023)
);

INSERT INTO `comments` (`comment_id`, `page_id`, `user_id`, `content`, `created_time`)
VALUES
('1', '1', '1', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks', '2009-01-03 18:15:05'),
('2', '2', '2', 'Hello algo.monster', '2021-10-11 18:45:02')
;

SELECT * FROM comments; -- prints both comments
SELECT * FROM comments PARTITION (p_old); -- only prints 1 comment
SELECT * FROM comments PARTITION (p21); -- only prints 1 comment
