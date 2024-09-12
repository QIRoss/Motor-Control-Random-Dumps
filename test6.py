import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy import signal

# Parâmetros do motor e controlador
k = 0.265  # constante de torque (Nm/A)
ka = 0.8e-3  # coeficiente de atrito (Nm/(rad/s))
J = 1.24e-3  # momento de inércia (kg·m²)

# Configuração do PID
Kp = 1.0  # ganho proporcional
Ki = 0.1  # ganho integral
Kd = 0.05  # ganho derivativo

# Função de transferência
num_motor = [k]
den_motor = [J, ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)
num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)
system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

# Simulação
t = np.linspace(0, 5, 1000)
u = 0.5 * (signal.square(2 * np.pi * (1/2.6) * t, duty=0.5) + 1) * (-0.0775)
t, response = ctrl.forced_response(closed_loop, T=t, U=u)

# Cálculo da corrente
current = response / k  # Corrente do motor baseada na resposta do controle

# Plotagem
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, response, label='Resposta do Motor (m)')
plt.plot(t, u, 'r--', label='Entrada de Onda Quadrada')
plt.title('Resposta do Sistema e Entrada')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (m)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, current, label='Corrente do Motor (A)')
plt.title('Corrente do Motor')
plt.xlabel('Tempo (s)')
plt.ylabel('Corrente (A)')
plt.legend()
plt.tight_layout()
plt.show()
