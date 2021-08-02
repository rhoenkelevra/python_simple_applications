create table schedule(
    id int NOT NULL AUTO_INCREMENT primary key,
    description varchar(255),
    date datetime
);


ALTER TABLE schedule ADD id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    ADD INDEX (id);
    
ALTER TABLE schedule AUTO_INCREMENT=1001;