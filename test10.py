import numpy as np
import matplotlib.pyplot as plt
import control as ctrl
from scipy.signal import lsim

# Definir os parâmetros do motor e controlador
k = 0.265  # constante de torque (Nm/A)
ka = 0.8e-3  # coeficiente de atrito (Nm/(rad/s))
J = 1.24e-3  # momento de inércia (kg·m²)

# Parâmetros do PID ajustados
Kp = 1.0  # ganho proporcional
Ki = 0.1  # ganho integral
Kd = 0.05  # ganho derivativo

# Função de transferência do motor
num_motor = [k]
den_motor = [J, ka, 0]
G_motor = ctrl.TransferFunction(num_motor, den_motor)

# Função de transferência do PID
num_pid = [Kd, Kp, Ki]
den_pid = [1, 0]
G_pid = ctrl.TransferFunction(num_pid, den_pid)

# Sistema de malha fechada combinado
system = ctrl.series(G_pid, G_motor)
closed_loop = ctrl.feedback(system, 1)

# Convertendo o sistema para formato compatível com lsim
num, den = ctrl.tfdata(closed_loop)
num = np.squeeze(num)
den = np.squeeze(den)

# Definir o tempo de simulação e a entrada senoidal
t = np.linspace(0, 200, 1000)  # tempo de 0 a 200 segundos
omegaM = 4.05  # rad/s
p = 0.0775 * np.sin(omegaM * t)  # entrada senoidal

# Simular a resposta ao sinal senoidal
t, y, _ = lsim((num, den), U=p, T=t)

# Plotar a resposta
plt.figure(figsize=(10, 5))
plt.plot(t, y, label='Resposta do Sistema (y(t))')
plt.plot(t, p, 'r--', label='Entrada Senoidal (p(t))')
plt.title('Resposta do Sistema à Entrada Senoidal')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta')
plt.legend()
plt.grid(True)
plt.show()
