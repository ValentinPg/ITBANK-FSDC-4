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

--seleccionar los prestamos cuyos importes sean mayor que el importe medio de todos los prestamos
SELECT * FROM PRESTAMO
WHERE loan_total > (SELECT AVG(loan_total) FROM prestamo);

-- contar la cantidad de clientes menores a 50 años
SELECT count(*) FROM CLIENTE
WHERE dob > (SELECT strftime('%Y.%m%d', 'now') - 50 FROM cliente);

--Seleccionar las primeros 5 cuentas con saldo superior a 8000
SELECT * FROM CUENTA
WHERE balance > 8000
LIMIT 5;

--Seleccionar los préstamos que tengan fecha en abril, junio y agosto,ordenándolos por importe
SELECT *
FROM prestamo
WHERE (SELECT substr(loan_date,6,2)) = '04' OR (SELECT substr(loan_date,6,2)) = '06' OR (SELECT substr(loan_date,6,2)) = '08'
ORDER BY loan_total;

--Obtener el importe total de los prestamos agrupados por tipo de préstamos.Por cada tipo de préstamo de la tabla préstamo,
-- calcular la suma de susimportes. Renombrar la columna como loan_total_accu
SELECT loan_type,sum(loan_total) AS  loan_total_accu
FROM prestamo
GROUP BY loan_type;