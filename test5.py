import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy import signal

# Definir os parâmetros do motor
k = 0.265  # constante de torque (Nm/A)
ka = 0.8e-3  # coeficiente de atrito (Nm/(rad/s))
J = 1.24e-3  # momento de inércia (kg·m²)
r = 0.1  # constante de conversão

# Definir os parâmetros do PID com valores hipotéticos ajustados
Kp = 1.0  # ganho proporcional
Ki = 0.1  # ganho integral
Kd = 0.05  # ganho derivativo

# Criar a função de transferência do motor
num_motor = [k]
den_motor = [J, ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)

# Criar a função de transferência do PID
num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)

# Combinar o motor e o PID em malha fechada
system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

# Definir o tempo de simulação e criar a onda quadrada
t = np.linspace(0, 5, 1000)  # tempo de 0 a 5 segundos com 1000 pontos
# Gerar onda quadrada com período de 2.6s (1.3s em cada nível)
u = 0.5 * (signal.square(2 * np.pi * (1/2.6) * t, duty=0.5) + 1) * (-0.0775)

# Simular a resposta com a entrada de onda quadrada
t, response = ctrl.forced_response(closed_loop, T=t, U=u)

# Plotar a resposta
plt.figure()
plt.plot(t, response, label='Resposta do Sistema')
plt.plot(t, u, 'r--', label='Entrada de Onda Quadrada')
plt.title('Resposta do Sistema à Entrada de Onda Quadrada')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (m)')
plt.grid(True)
plt.legend()
plt.show()
