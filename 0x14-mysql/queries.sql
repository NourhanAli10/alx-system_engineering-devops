sudo mysql -u root -p
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name TEXT );
INSERT INTO nexus6 (name) VALUES ('Nexus 6');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
CREATE USER 'replica_user'@'%' IDENTIFIED BY "user";
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
