-- Listar la cantidad de clientes por nombre de sucursal ordenando de mayor
--a menor

SELECT branch_name AS 'Sucursal', cliente.branch_id AS 'Numero de Sucursal', 
COUNT(customer_id) AS 'Clientes'  FROM cliente
JOIN sucursal
	ON cliente.branch_id = sucursal.branch_id
GROUP BY 1
ORDER BY 1 ASC;

--Obtener la cantidad de empleados por cliente por sucursal en un número
--real

SELECT COUNT(cliente.customer_id) AS 'CLIENTES', COUNT(employee_id) AS 'EMPLEADOS', branch_name AS
'SUCURSAL', (COUNT(cliente.customer_id)/COUNT(employee_id)) AS 'Empleados por cliente'
FROM empleado
INNER JOIN cliente ON empleado.branch_id = cliente.branch_id
INNER JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY branch_name; 

--Obtener la cantidad de tarjetas de crédito por tipo por sucursal
--ACLARACION: Son todas tarjetas de crédito por lo que es el único tipo en la tabla.

SELECT  branch_name AS 'SUCURSAL',COUNT(marcaID) AS 'CANTIDAD DE TARJETA DE CREDITO'
FROM tarjeta
INNER JOIN cliente ON tarjeta.customer_id=cliente.customer_id
INNER JOIN sucursal ON sucursal.branch_id=cliente.branch_id
GROUP BY 1
ORDER BY 2 DESC ;

--Obtener el promedio de créditos otorgado por sucursal


SELECT COUNT(cliente.branch_id) AS 'SUCURSAL', COUNT(loan_id) AS 'PRESTAMOS OTORGADOS', 
COUNT(cliente.branch_id)  / COUNT(loan_id) AS 'PROMEDIO'
FROM sucursal
INNER JOIN cliente ON cliente.branch_id = sucursal.branch_id
INNER JOIN prestamo ON cliente.customer_id = prestamo.customer_id;

--La información de las cuentas resulta critica para la compañía, por eso es
--necesario crear una tabla denominada “auditoria_cuenta” para guardar los
--datos movimientos, con los siguientes campos: old_id, new_id, old_balance,
--new_balance, old_iban, new_iban, old_type, new_type, user_action,
--created_at
--        o Crear un trigger que después de actualizar en la tabla cuentas los
--campos balance, IBAN o tipo de cuenta registre en la tabla auditoria
--        o Restar $100 a las cuentas 10,11,12,13,14


CREATE TABLE IF NOT EXISTS auditoria_cuenta(
    operation_id integer PRIMARY KEY AUTOINCREMENT,
    old_id integer NOT NULL,
    new_id integer,
    old_balance integer NOT NULL,
    new_balance integer,
    old_iban TEXT NOT NULL,
    new_Iban text,
    old_type text NOT NULL,
    new_type text,
    user_action text,
    created_at text);

    --Creo trigger

CREATE TRIGGER if not EXISTS log_operacion_cuenta
    AFTER UPDATE on cuenta
    WHEN old.balance <> new.balance OR old.iban <> new.iban OR old.cuentaID <> new.cuentaID

    BEGIN
        INSERT INTO auditoria_cuenta(
            old_id,
            new_id,
            old_balance,
            new_balance,
            old_iban,
            new_Iban,
            old_type,
            new_type,
            user_action,
            created_at)

        VALUES
            (
            old.customer_id,
            new.customer_id,
            old.balance,
            new.balance,
            old.iban,
            new.iban,
            old.cuentaID,
            new.cuentaID,
            'UPDATE',
            DATETIME('NOW'));

    END;

    -- Restar $100 a las cuentas 10, 11, 12, 13 y 14

UPDATE cuenta
SET balance = balance - 100
WHERE account_id = 10 OR account_id = 11 OR account_id = 12 OR account_id = 13 OR account_id = 14; 

--Mediante índices mejorar la performance la búsqueda de clientes por DNI

CREATE INDEX 'DNI'
ON cliente (customer_DNI);

--Crear la tabla “movimientos” con los campos de identificación del
--movimiento, número de cuenta, monto, tipo de operación y hora


CREATE TABLE IF NOT EXISTS 'Movimientos' (
	'mov_id' INTEGER PRIMARY KEY AUTOINCREMENT,
	'nro_cuenta' INTEGER NOT NULL,
	'monto' REAL NOT NULL,
	'tipo_op' TEXT NOT NULL,
	'hora' TEXT NOT NULL);

BEGIN TRANSACTION;

    UPDATE cuenta
    SET balance = balance - 1000
    WHERE account_id = 200;

    UPDATE cuenta
    SET balance = balance + 1000
    WHERE account_id = 400;

    INSERT INTO Movimientos (
    'nro_cuenta',
    'monto',
    'tipo_op',
    'hora')
    VALUES (200, -1000, 'TRANSFERENCIA', datetime('now'));

    INSERT INTO Movimientos (
    'nro_cuenta',
    'monto',
    'tipo_op',
    'hora')
    VALUES (400, +1000, 'TRANSFERENCIA', datetime('now'));
    
ROLLBACK;



    

	