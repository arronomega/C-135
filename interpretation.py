import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("stars.csv")
starname =df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()
dist.sort()
starname.sort()
mass.sort()
radius.sort()
gravity.sort()
plt.plot(starname,mass)
plt.plot(starname,radius)
plt.plot(starname,gravity)
plt.plot(starname,dist)