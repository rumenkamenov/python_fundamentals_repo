import math

budjet = float(input())
number_clients = int(input())
gigabytes_data = int(input())
number_of_hosts = int(input())
uptime = float(input())

server_sup = 50
storage_unit = 500

servers_needed = math.ceil(number_clients / server_sup)
storage_needed = gigabytes_data / 0.5
hourly_cost = (2 * servers_needed + 0.5 * storage_needed) * 24
host_cost = number_of_hosts * 10
montly_cost = hourly_cost * 30
total = (montly_cost + host_cost) * uptime / 100
diff = abs(budjet - total)
if budjet >= total:
    print(f"Clouds Ahoy! Monthly cost: ${total:.2f} (${diff:.2f} leftover)")
else:
    print(f"Stay Grounded! Monthly cost: ${total:.2f} (Need ${diff:.2f} more)")