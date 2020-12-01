# Desarrollo Web Full Stack con Python y JavaScript - TRABAJO FINAL CURSO 2020

## Enunciado del Problema a Resolver
Una clínica de Optometría necesita un sistema web en Django que le permita gestionar el
diagnóstico de sus pacientes y la venta de los productos Ópticos para los mismos. Para ello
se requiere:
1. Un sistema con un login de usuario con los siguientes roles:
 * Secretaría
 * Profesional medico
 * Ventas
 * Taller
 * Gerencia
2. El sistema gestionará tres Modelos esenciales:
* Turnos
* Pedidos
* Pacientes
3. El rol de Secretaría permite agregar, modificar o eliminar los turnos de los Pacientes.
4. Cada Paciente tiene su historial médico (solo el Profesional médico puede agregar
Observaciones al historial médico).
5. Cada Profesional médico puede ver el listado de Pacientes filtrando por día, mes o año.
6. El Profesional médico solo puede ver los Pacientes asignados a él.
7. El rol de Ventas puede generar un pedido para el Paciente, donde detalla el Producto
que quiere adquirir, el precio (pueden ser más de un producto), un subtotal, tipo de
pago (tarjeta de crédito, debido, billetera virtual o efectivo).
* El producto tiene nombre, si está clasificado como Lente tendrá la opción de
Lejos/Cerca, Izquierda/Derecha, si incluye Armazón o no.
* Una vez que se genera el pedido queda en estado “Pendiente”.
* Luego el rol de Ventas puede cambiar el estado a “Pedido” o mandarlo a “Taller”.
8. El rol de Taller solo visualiza la lista de pedidos (con todos los detalles del producto sin
los precios). El Taller puede confirmar cambiando el estado del pedido a “Finalizado”.
9. Gerencia puede visualizar todos los datos y necesita los siguientes reportes:
* Pacientes que asistieron a los turnos en la semana/mes.
* Pacientes que no asistieron a los turnos en la semana/mes.
* Pacientes que hicieron por lo menos un Pedido en la semana/mes.
* Productos más vendidos en el mes.
* Ventas totales por mes clasificadas por Vendedores.

## Instalación y pruebas locales

Para instalar y ejecutar en su maquina local siga los siguientes pasos:

1. `git clone http://github.com/pcosta0/ptic20tp_django`

2. Inicie el servidor de desarrollo django:  

    `./manage.py runserver`

3. Abra su navegador y diríjase a http://127.0.0.1:8000
 
4. Ingrese al sistema con cualquier combinación **usuario/clave** de los siguientes roles ya creados en la base de datos de ejemplo:
* Secretaría:  **jkrowling/jkrowling**
* Profesional Médico: **harryp/harryp, hermioneg/hermioneg** o **rweasley/rweasley**
* Ventas: **marykay/marykay**
* Taller: **mario/mario**
* Gerencia: **zeus/zeus**

