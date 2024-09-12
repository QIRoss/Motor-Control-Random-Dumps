import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

Kp = 1.0
Ki = 0.1
Kd = 0.05

num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)

J = 1.24e-3
Ka = 0.8e-3
k = 0.265
num_motor = [k]
den_motor = [J, Ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)

system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

def saturate(signal, limit):
    return np.clip(signal, -limit, limit)

t, response = ctrl.step_response(closed_loop, T=np.linspace(0, 2, 100))

limited_response = saturate(response, 8)

plt.figure()
plt.plot(t, response, label='Sem Limitador')
plt.plot(t, limited_response, label='Com Limitador 8A')
plt.title('Resposta ao Degrau do Sistema de Controle com e sem Limitador')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (A)')
plt.grid(True)
plt.legend()
plt.show()

