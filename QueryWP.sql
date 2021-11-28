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
precio float(3) not null,
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
select * from categoria
select * from empleado

insert into empleado (nombre, apellido_p, edad, estado, telefono, pass, email) values ('Gustavo', 'Carreola', 22, 'Mexico', 7121552233, 'guuz123')
insert into empleado (nombre, apellido_p, edad, estado, telefono, pass, email) values ('Eric', 'Vazquez', 22, 'Mexico', 7121630599, 'eric123')

insert into producto (categoria, proveedor, nombre, precio, cantidad, existencia) values (1, 1, 'Nokia', 1200.35, 3, 1)

alter table empleado ADD email varchar(80)

update empleado set email = 'guuz.t13@gmail.com' where nombre='Gustavo'
update empleado set email = 'evdj@gmail.com' where nombre='Eric'

update empleado set nombre = 'xd' where id_empleado = '1'

update producto set precio = 12.10 where id_producto = '1'

delete from empleado where id_empleado = '5'

drop table producto
