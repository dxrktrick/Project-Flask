create database WikiPartners
use WikiPartners

create table empleado(
	id_empleado int identity (1,1) primary key,
	nombre varchar(15) not null,
	apellido_p varchar(15)not null,
	edad int not null,
	estado varchar (15) not null,
	telefono bigint not null,
	pass varchar(15) not null,
	email varchar(80) not null
);

create table cliente(
	id_cliente int identity (1,1) primary key,
	nombre varchar(15) not null,
	apellido_p varchar(15)not null,
	estado varchar (15) not null,
	telefono bigint not null,
);

Create table producto(
id_producto int identity (1,1) primary key,
categoria int not null,
proveedor int not null,
nombre varchar(40) not null,
precio float not null,
cantidad int not null,
existencia bit not null,
CONSTRAINT fk_categoria FOREIGN KEY (categoria) REFERENCES categoria (id_categoria),
CONSTRAINT fk_proveedor FOREIGN KEY (proveedor) REFERENCES proveedor (id_proveedor)
);

create table categoria(
	id_categoria int identity (1,1) primary key,
	nombre varchar(15) not null
);

create table proveedor(
	id_proveedor int identity (1,1) primary key,
	nombre varchar(15) not null,
	dni varchar (15) not null,
	nacionalidad varchar (15) not null,
	telefono bigint not null
);

Create table factura(
id_factura int identity (1,1) primary key,
fecha date not null,
serie bigint not null,
empleado int not null,
cliente int not null,
monto float not null,
existencia bit not null,
CONSTRAINT fk_empleado FOREIGN KEY (empleado) REFERENCES empleado (id_empleado),
CONSTRAINT fk_cliente FOREIGN KEY (cliente) REFERENCES cliente (id_cliente)
);

Create table detalleVenta(
id_detalle int identity (1,1) primary key,
factura int not null,
producto int not null,
cantidad int not null,
precioVenta float not null,
CONSTRAINT fk_factura FOREIGN KEY (factura) REFERENCES factura (id_factura),
CONSTRAINT fk_producto FOREIGN KEY (producto) REFERENCES producto (id_producto)
);

select * from producto
select * from detalleVenta
select * from factura
select * from categoria
select * from empleado
select * from proveedor
select * from cliente


select count('') from producto
select count('') from detalleVenta
--Categoria--
INSERT INTO categoria (nombre) VALUES ('Tecnolog�a'),('Accesorios'),('Papeler�a')

--Proveedor--
INSERT INTO proveedor (nombre, dni, nacionalidad, telefono) VALUES ('Oficimundo', '14556789B', 'Mexicana', 7122366659)
INSERT INTO proveedor (nombre, dni, nacionalidad, telefono) VALUES  ('HP', '22473FB7A', 'Mexicana', 7121449800)
INSERT INTO proveedor (nombre, dni, nacionalidad, telefono) VALUES ('Dell', '4468UY89W', 'Mexicana', 7122990467)
INSERT INTO proveedor (nombre, dni, nacionalidad, telefono) VALUES ('Net-Comm', '1892VB34M', 'Estadounidense', 8080945601)
INSERT INTO proveedor (nombre, dni, nacionalidad, telefono) VALUES ('Alco', '9901MN35Y', 'Colombiana', 5766890357)

--Empleado--
INSERT INTO empleado (nombre, apellido_p, edad, estado, telefono, email, pass)
VALUES ('Gustavo', 'Carreola', '21', 'M�xico', 7121552233, 'guuz.t13@gmail.com', 'guuz123'),
('Eric', 'V�zquez', '21', 'M�xico', 7121630599, 'ericvazquezdejesus25@gmail.com', 'eric123')

--Cliente--
INSERT INTO cliente (nombre, apellido_p, estado, telefono)
VALUES ('Marcos', 'Soto', 'Mexico', 7122645368),
('Daniela', 'Linares', 'Mexico', 7124780233),
('Alejandra', 'Flores', 'Morelos', 7233890455),
('Lesly', 'Urbina', 'Mexico', 7323488901),
('Rodrigo', 'Prospero', 'Mexicana', 7125567701)

--Producto--
INSERT INTO producto (categoria, proveedor, nombre, precio, cantidad, existencia)
VALUES (1, 16, 'Laptop HP Pavilion X360', 18359.26, 1, 5),
(2, 19, 'Mouse Razer Viper', 1542.25, 1, 15),
(2, 18, 'Audifonos Hyper Cloud Stinger', 899.0, 1, 15),
(3, 17, 'Paquete de hojas blancas (t/c)', 119.0, 2, 100),
(3, 11, 'Colores Norma (24 pzas)', 124.9, 3, 60)

