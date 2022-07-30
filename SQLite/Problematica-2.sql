-- Crear una vista con las columnas id, numero sucursal, nombre, apellido, DNI
-- y edad de la tabla cliente calculada a partir de la fecha de nacimiento


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
						ORDER by edad ASC; --agregar dni

		-- Columnas mayor a 40 años y DNI ASC
		SELECT vista.customer_id,vista.num_sucursal,vista.nombre,vista.apellido,vista.edad, cliente.customer_DNI
		FROM segunda_problematica as vista
		INNER JOIN cliente on vista.customer_id = cliente.customer_id
		WHERE edad > 40
		ORDER by customer_DNI ASC;


-- Dado el siguiente JSON. Insertar 5 nuevos clientes en la base de datos y
-- verificar que se haya realizado con éxito la inserción

INSERT INTO cliente(customer_name,customer_surname,customer_DNI,branch_id,dob)
VALUES	('Lois','Stout','47730534',80,'1984-07-07'),
		('Hall','Mcconnell','52055464',45,'1968-04-30'),
		('Hilel','Mclean','43625213',77,'1993-03-28'),
		('Jin','Cooley','21207908',96,'1959-08-24'),
		('Gabriel','Harmon','57063950',27,'1976-04-01');





--  Actualizar 5 clientes recientemente agregados en la base de datos dado que
-- hubo un error en el JSON que traía la información, la sucursal de todos es
-- la 10

UPDATE cliente
SET branch_id = 10
WHERE customer_DNI = '47730534' or customer_DNI = '52055464' or customer_DNI = '43625213'
or customer_DNI = '21207908' or customer_DNI = '57063950';

-- Eliminar el registro correspondiente a “Noel David” realizando la selección
-- por el nombre y apellido

DELETE FROM cliente
WHERE customer_name = 'Noel' AND customer_surname = 'David'; -- agregar cliente



-- Consultar sobre cuál es el tipo de préstamo de mayor importe
SELECT loan_type, max(loan_total) as valor_prestamo
FROM prestamo;