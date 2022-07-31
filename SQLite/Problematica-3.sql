--Selecciono las cuentas con su id que tengan saldo negativo

SELECT account_id, balance
from cuenta
WHERE balance < 0
ORDER by balance desc;

--Selecciono el nombre, apellido y edad de los clientes que tengan en el
--apellido la letra Z y ordeno seguún apellido

SELECT customer_name, customer_surname,
(CASE
	WHEN dob is NOT NULL
				THEN cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int)
	END)as age
FROM cliente
WHERE customer_surname like 'Z%'
ORDER by customer_surname;

--Selecciono el nombre, apellido, edad y nombre de sucursal de las personas
--cuyo nombre sea “Brendan” y el resultado lo ordeno por nombre de
--sucursal

SELECT customer_name,customer_surname,
(CASE
	WHEN dob is NOT NULL
				THEN cast(strftime('%Y.%m%d', 'now') - strftime('%Y.%m%d', dob ) as int)
	END)as age, sucursal.branch_name
FROM cliente 
INNER JOIN sucursal on cliente.branch_id = sucursal.branch_id
WHERE customer_name like 'brendan'
order by branch_name;

--Selecciono de la tabla de préstamos, los préstamos con un importe mayor
--a $80.000 y los préstamos prendarios utilizando un union

SELECT loan_total
FROM prestamo
where loan_total > 8000000 
UNION 
SELECT loan_type
FROM prestamo
where loan_type = 'PRENDARIO';