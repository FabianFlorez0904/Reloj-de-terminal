import os
from datetime import datetime
import time

while True:
    hora_actual = datetime.now()
    print(
        "\t+------------+\n",
        "\t| {}-{:0>2}-{:0>2} |\n".format(hora_actual.year,hora_actual.month,hora_actual.day),
        "\t+------------+\n",
        "\t|  {:0>2}:{:0>2}:{:0>2}  |\n".format(hora_actual.hour,hora_actual.minute,hora_actual.second),
        "\t+------------+\n"
    )
    time.sleep(1)
    os.system("cls")
