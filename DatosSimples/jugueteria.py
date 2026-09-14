#Una juguetería tiene mucho éxito en dos de sus productos: autos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que se debe calcular el peso de los autos y muñecas que saldrán en cada paquete a demanda. Cada auto pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de autos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

auto = 112
muneca = 75
v_auto = input("Cuantos autos se vendieron? ")
v_muneca = input("Cuantas muñecas se vendieron? ")
total = (int(v_auto) * auto) + (int(v_muneca) * muneca)
print("El peso total del paquete a enviar es: ", total, "g")
