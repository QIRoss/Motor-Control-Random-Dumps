import numpy as np

ka = 0.8e-3
r = 0.1
m = 0.775
g = 9.8
initial_height = 0
target_position = -0.0775

dt = 0.01
time = 0
position = initial_height
velocity = 0

time_list = [time]
position_list = [position]
velocity_list = [velocity]

while position > target_position:
    tau_atrito = ka * (velocity / r)
    a = -g - (tau_atrito / (m * r))
    velocity += a * dt
    position += velocity * dt
    time += dt
    
    time_list.append(time)
    position_list.append(position)
    velocity_list.append(velocity)

print(f"Tempo de descida: {time} segundos")
