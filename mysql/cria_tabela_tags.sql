CREATE TABLE TAGS(
    IDTAG INT PRIMARY KEY AUTO_INCREMENT,
    TAG VARCHAR(8) NOT NULL UNIQUE,
    ID_USUARIO INT
);