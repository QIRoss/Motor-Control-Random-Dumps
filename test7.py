import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy import signal

# Definir os parâmetros do motor
k = 0.265  # constante de torque (Nm/A)
ka = 0.8e-3  # coeficiente de atrito (Nm/(rad/s))
J = 1.24e-3  # momento de inércia (kg·m²)

# Parâmetros ajustados do PID para resposta mais rápida e estável
Kp = 1.5  # Aumentado de 1.0 para 1.5
Ki = 0.4  # Aumentado de 0.1 para 0.4
Kd = 0.1  # Aumentado de 0.05 para 0.1

# Criar a função de transferência do PID
num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)

# Criar a função de transferência do motor
num_motor = [k]
den_motor = [J, ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)

# Combinar o motor e o PID em malha fechada
system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

# Definir o tempo de simulação e criar a onda quadrada
t = np.linspace(0, 10, 1000)  # tempo de 0 a 10 segundos com 1000 pontos
# Gerar onda quadrada com período de 2.6s (1.3s em cada nível)
u = 0.5 * (signal.square(2 * np.pi * (1/2.6) * t, duty=0.5) + 1) * (-0.0775)

# Simular a resposta com a entrada de onda quadrada
t, response = ctrl.forced_response(closed_loop, T=t, U=u)

# Plotar a resposta
plt.figure(figsize=(10, 5))
plt.plot(t, response, label='Resposta do Motor (m)')
plt.plot(t, u, 'r--', label='Entrada de Onda Quadrada')
plt.title('Resposta do Sistema à Entrada de Onda Quadrada')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (m)')
plt.legend()
plt.grid(True)
plt.show()
