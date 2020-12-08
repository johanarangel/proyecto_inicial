DROP TABLE IF EXISTS  validacion;

CREATE TABLE validacion (
    [codigo de circulación] INTEGER PRIMARY KEY,
    [nombre empresa] STRING  NOT NULL,
    [actividad] STRING NOT NULL,
    [nombre] STRING, 
    [apellido] STRING,
    [dni] INTEGER  NOT NULL
); 