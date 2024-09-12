import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

k = 0.265  # constante de torque (Nm/A)
ka = 0.8e-3  # coeficiente de atrito (Nm/(rad/s))
J = 1.24e-3  # momento de inércia (kg·m²)
r = 0.1  # constante de conversão

Kp = 1.0  # ganho proporcional
Ki = 0.1  # ganho integral
Kd = 0.05  # ganho derivativo

num_motor = [k]
den_motor = [J, ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)

num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)

system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

t = np.linspace(0, 2, 1000)  # tempo de 0 a 2 segundos com 1000 pontos
u = np.zeros_like(t)  # entrada inicializada como zero
u[(t >= 0) & (t < 0.13)] = 0  # y = 0m de t=0 até t=0.13s
u[(t >= 0.13) & (t < 1.43)] = -0.0775  # y = -0.0775m de t=0.13s até t=1.43s
u[t >= 1.43] = 0  # y = 0m em t=1.43s

t, response, _ = ctrl.forced_response(closed_loop, T=t, U=u)

plt.figure()
plt.plot(t, response, label='Resposta do Sistema')
plt.plot(t, u, 'r--', label='Entrada Personalizada')
plt.title('Resposta do Sistema à Entrada Personalizada')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (m)')
plt.grid(True)
plt.legend()
plt.show()
