-- Crear en la base de datos los tipos de cliente, de cuenta y marcas de
-- tarjeta. Insertar los valores según la información provista en el Sprint
-- 5

CREATE TABLE tipos_cliente (
	tipoId INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	plan_cliente TEXT NOT NULL);

-- Agrego los tipos de cliente

INSERT INTO tipos_cliente (plan_cliente)
VALUES ('BLACK'); --misma sintaxis para 'gold' y 'black'

--creo tabla de tipos de cuenta

CREATE TABLE tipos_cuenta (
	cuentaID INTEGER PRIMARY KEY AUTOINCREMENT,
	cuenta_cliente TEXT NOT NULL);

-- agrego los tipos de cuenta

INSERT INTO tipos_cuenta (cuenta_cliente)
VALUES ('CAJA AHORRO DOLARES'); -- misma sintaxis par el resto

-- creo tabla de marcas de tarjeta

CREATE TABLE marcas_tarjeta (
	marcaID INTEGER PRIMARY KEY AUTOINCREMENT,
	tipo_tarjeta TEXT NOT NULL);

--inserto las marcas
INSERT INTO marcas_tarjeta (tipo_tarjeta)
VALUES ('CREDITO');  -- misma sintaxis par 'debito'

---------------------------------------------------------------------------------
-------------------------------------------------------------------------------


-- - Agregar la entidad tarjeta teniendo en cuenta los atributos
-- necesarios para la operación del home banking (se sugieren los
-- siguientes campos Numero (único e irrepetible, con una restricción
-- ante cada inserción que no debe superar 20 números/espacios), CVV,
-- Fecha de otorgamiento, Fecha Expiración). Almacenar si es una
-- tarjeta de crédito o débito. 


CREATE TABLE tarjeta (
	tarjeta_id INTEGER PRIMARY KEY AUTOINCREMENT,
	numero TEXT NOT NULL UNIQUE CHECK(length(numero <=20)),
	CVV INTEGER NOT NULL CHECK(length(CVV = 3)),
	fecha_otorgamiento TEXT not NULL,
	fecha_expiracion TEXT not NULL,
    marcaID INTEGER,
	customer_id INTEGER,
    FOREIGN key (marcaID) references marcas_tarjeta(marcaID)
        on update cascade
        on delete cascade,
	FOREIGN KEY (customer_id) REFERENCES cliente(customer_id)
	        on update cascade
			on delete cascade)
	

-- usamos generate data para rellenar todos los campos de la tabla


----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------



-- Agregar la entidad direcciones, que puede ser usada por los clientes,
-- empleados y sucursales con los campos utilizados en el SPRINT 5

CREATE TABLE `direccion` (
  `direccion_id` INTEGER primary key AUTOINCREMENT,
  `calle` varchar(255) default NULL,
  `pais` varchar(100) default NULL,
  `provincia` varchar(50) default NULL,
  `ciudad` varchar(255),
  `customer_id` mediumint default NULL,
  `employee_id` mediumint default NULL,
  FOREIGN KEY (customer_id) REFERENCES cliente(customer_id)
	on UPDATE CASCADE
	on DELETE SET NULL
	FOREIGN KEY (employee_id) REFERENCES empleado (employee_id)
		on UPDATE CASCADE
		on DELETE SET NULL
); --rellenamos con generatedata




-- Teniendo en cuenta que un
-- cliente o empleado puede tener múltiples direcciones, pero la
-- sucursal, solo una



-- agrego la columna "branch_id"

ALTER TABLE direccion
ADD COLUMN branch_id INTEGER;


			--la seteo como una foreign key
BEGIN TRANSACTION;

CREATE TABLE `direccion_nuevo` (
  `direccion_id` INTEGER primary key AUTOINCREMENT,
  `calle` varchar(255) default NULL,
  `pais` varchar(100) default NULL,
  `provincia` varchar(50) default NULL,
  `ciudad` varchar(255),
  `customer_id` mediumint default NULL,
  `employee_id` mediumint default NULL,
  branch_id INTEGER,
  FOREIGN KEY (customer_id) REFERENCES cliente(customer_id)
	on UPDATE CASCADE
	on DELETE SET NULL
	FOREIGN KEY (employee_id) REFERENCES empleado (employee_id)
		on UPDATE CASCADE
		on DELETE SET NULL
	FOREIGN KEY (branch_id) REFERENCES sucursal(branch_id)
			on UPDATE CASCADE
			on DELETE SET NULL
);
	
INSERT INTO direccion_nuevo SELECT * FROM direccion;

DROP TABLE direccion;

ALTER TABLE direccion_nuevo RENAME to direccion;

COMMIT;

-- agrego los datos de sucursales vinculadas a esta direccion
	UPDATE direccion
	SET branch_id = (SELECT branch_id FROM sucursal WHERE branch_id = direccion_id)




-----------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------

-- Ampliar el alcance de la entidad cuenta para que identifique el tipo de
-- la misma

BEGIN TRANSACTION;

CREATE TABLE cuenta_nuevo(
	account_id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER NOT NULL,
	balance INTEGER NOT NULL,
	iban TEXT NOT NULL,
	cuentaID INTEGER,
	FOREIGN KEY (cuentaID) REFERENCES tipos_cuenta(cuentaID));
	
INSERT INTO cuenta_nuevo SELECT * FROM cuenta;

DROP TABLE cuenta;

ALTER TABLE cuenta_nuevo RENAME to cuenta;

COMMIT;

-- asigno tipos de cuenta a cada cuenta (de manera "aleatoria")
UPDATE cuenta
SET cuentaID = 3
WHERE account_id < 50;

UPDATE cuenta
SET cuentaID = 1
WHERE account_id >= 50 AND account_id <= 150;

UPDATE cuenta
SET cuentaID = 2
WHERE account_id > 150;

-----------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------

-- Corregir el campo employee_hire_date de la tabla empleado con la
-- fecha en formato YYYY-MM-DD


UPDATE empleado
SET employee_hire_date = replace(employee_hire_date,'/','-'); --cammbio el formato para que pueda ser leido

UPDATE empleado
SET employee_hire_date = 
substr(employee_hire_date, 7, 4) || '-' || substr(employee_hire_date, 4,2) || '-' || substr(employee_hire_date, 1,2);-- con esto lo transformo


