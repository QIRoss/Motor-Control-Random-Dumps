import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

k = 0.265
ka = 0.8e-3
J = 1.24e-3
r = 0.1

Kp = 1.0
Ki = 0.1
Kd = 0.05

num_motor = [k]
den_motor = [J, ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)

num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)

system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

t, response = ctrl.step_response(closed_loop, T=np.linspace(0, 2, 100))
plt.plot(t, response)
plt.title('Resposta ao Degrau com Parâmetros Corretos')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta')
plt.grid(True)
plt.show()

