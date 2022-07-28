-- creacion de tabla tipos cliente

CREATE TABLE tipos_cliente (
	tipoId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	plan_cliente TEXT NOT NULL);

-- Agrego los tipos de cliente

INSERT INTO tipos_cliente (plan_cliente)
VALUES ('BLACK'); --misma sintaxis para 'gold' y 'black'

--creo tabla de tipos de cuenta

CREATE TABLE tipos_cuenta (
	cuenta_cliente TEXT NOT NULL PRIMARY KEY);

-- agrego los tipos de cuenta

INSERT INTO tipos_cuenta (cuenta_cliente)
VALUES ('CAJA AHORRO DOLARES'); -- misma sintaxis par el resto

-- creo tabla de marcas de tarjeta

CREATE TABLE marcas_tarjeta (
	tipo_tarjeta TEXT NOT NULL PRIMARY KEY UNIQUE);

--inserto las marcas
INSERT INTO marcas_tarjeta (tipo_tarjeta)
VALUES ('CREDITO');  -- misma sintaxis par 'debito'


--creo tabla 'tarjeta'

CREATE TABLE tarjeta (						
	numero TEXT NOT NULL PRIMARY KEY CHECK(length(numero <=20)),
	CVV INTEGER NOT NULL CHECK(length(CVV = 3)),
	fecha_otorgamiento TEXT not NULL,
	fecha_expiracion TEXT not NULL
    tipo TEXT
    FOREIGN key (tipo) references marcas_tarjeta(tipo_tarjeta)
        on update cascade
        on delete cascade);
--aux 
-- CREATE TABLE tarjeta (
-- 	tarjeta_id INTEGER PRIMARY KEY AUTOINCREMENT,
-- 	numero TEXT NOT NULL UNIQUE CHECK(length(numero <=20)),
-- 	CVV INTEGER NOT NULL CHECK(length(CVV = 3)),
-- 	fecha_otorgamiento TEXT not NULL,
-- 	fecha_expiracion TEXT not NULL,
--     tipo TEXT,
-- 	DNI_pos TEXT,
--     FOREIGN key (tipo) references marcas_tarjeta(tipo_tarjeta)
--         on update cascade
--         on delete cascade,
-- 	FOREIGN KEY (DNI_pos) REFERENCES cliente(customer_DNI)
-- 	        on update cascade
-- 			on delete cascade)
	

UPDATE tarjeta
SET DNI_asoc = (SELECT customer_DNI FROM cliente ORDER BY random() LIMIT 1)

UPDATE tarjeta
SET DNI_pos = (SELECT customer_DNI
				FROM cliente
				ORDER by random()) -- me reemplaza siempre con el mismo resultado

				
UPDATE tarjeta
SET DNI_pos =
	CASE
	WHEN DNI_pos is NULL 
	THEN (SELECT customer_DNI
				FROM cliente
				ORDER by random())
END



-- Creo tabla direccion

create TABLE direccion(
	direccionID INTEGER not NULL PRIMARY KEY AUTOINCREMENT,
	calle TEXT not NULL,
	ciudad TEXT not NULL,
	provincia TEXT NOT NULL,
	pais TEXT NOT NULL);



-- formato de tiempo

UPDATE empleado
SET employee_hire_date = replace(employee_hire_date,'/','-'); --cammbio el formato para que pueda ser leido

UPDATE empleado
SET employee_hire_date = 
substr(employee_hire_date, 7, 4) || '-' || substr(employee_hire_date, 4,2) || '-' || substr(employee_hire_date, 1,2);-- con esto lo transformo


------+-+-+-+-++-+-+-++-+-+-+-+-+-++-+-+-+-+-+--+----+-+-+-+-+--+----------------------------------------------------------------------------------------------------------------------------------
--+--+--+-+--+-+-+-+-++--+-+-+-+-+-+-++++--------------------------------+++++-++----++--------+++++-----------------------------------------------------------------------------------------------------
-----+--+--+-+-+-+-+-+-+-+-+-+-+--+-+-+---------------+++----------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--Creamos la view

CREATE VIEW segunda_problematica
AS
SELECT
	customer_id,
	branch_id as num_sucursal,
	customer_name as nombre,
	customer_surname as apellido,
	(CASE
		WHEN dob is NOT NULL
				THEN cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int)
	END)as edad
FROM cliente;

		-- Anne y Tyler
						SELECT *
						FROM segunda_problematica
						WHERE nombre = 'Anne' or nombre = 'Tyler'
						ORDER by edad ASC;

		-- Columnas mayor a 40 años y DNI ASC
		SELECT vista.customer_id,vista.num_sucursal,vista.nombre,vista.apellido,vista.edad, cliente.customer_DNI
		FROM segunda_problematica as vista
		INNER JOIN cliente on vista.customer_id = cliente.customer_id
		WHERE edad > 40
		ORDER by customer_DNI ASC;


-- inserto clientes nuevos
INSERT INTO cliente(customer_name,customer_surname,customer_DNI,branch_id,dob)
VALUES	('Lois','Stout','47730534',80,'1984-07-07'),
		('Hall','Mcconnell','52055464',45,'1968-04-30'),
		('Hilel','Mclean','43625213',77,'1993-03-28'),
		('Jin','Cooley','21207908',96,'1959-08-24'),
		('Gabriel','Harmon','57063950',27,'1976-04-01');

-- corrijo las sucursales

UPDATE cliente
SET branch_id = 10
WHERE customer_DNI = '47730534' or customer_DNI = '52055464' or customer_DNI = '43625213'
or customer_DNI = '21207908' or customer_DNI = '57063950';

--elimino registro

DELETE FROM cliente
WHERE customer_name = 'Noel' AND customer_surname = 'David';

--prestamo mayor 
SELECT loan_type, max(loan_total) as valor_prestamo
FROM prestamo;
