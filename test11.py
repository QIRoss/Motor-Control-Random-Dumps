import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

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

# Frequência de análise para o diagrama de Bode
frequencies = np.logspace(-2, 1, 500)  # de 0.01 a 10 rad/s

# Gerar diagrama de Bode
mag, phase, omega = ctrl.bode(closed_loop, frequencies, dB=True, Hz=False, deg=True, plot=True)

plt.show()
