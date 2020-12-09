DROP TABLE IF EXISTS  validacion;

CREATE TABLE validacion (
    [codigo] INTEGER PRIMARY KEY,
    [empresa] STRING  NOT NULL,
    [actividad] STRING NOT NULL,
    [nombre] STRING NOT NULL, 
    [apellido] STRING NOT NULL,
    [dni] INTEGER  NOT NULL
); 