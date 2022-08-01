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