# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:12:44 2024

@author: mdubo
"""
import numpy as np
import matplotlib.pyplot as plt


xvals = np.linspace(2, 7, 500);
yvals1 = np.exp(xvals);
yvals2 = xvals**3.6

fig, axs = plt.subplots(1, 3, figsize=(13, 5));

axs[0].plot(xvals, yvals1, label='$e^x$');
axs[0].plot(xvals, yvals2, label = '$x^{3.6}$')
axs[0].set_title("x vs y linear scale")
axs[0].set_xlabel("x")
axs[0].set_ylabel("y")
axs[0].legend()

axs[1].semilogy(xvals, yvals1, label="$e^x$");
axs[1].semilogy(xvals, yvals2, label = "$x^{3.6}$")
axs[1].set_title("x vs y log y scale")
axs[1].set_xlabel("x")
axs[1].set_ylabel("log(y)")
axs[1].legend()

axs[2].loglog(xvals, yvals1, label="$e^x$");
axs[2].loglog(xvals, yvals2, label = "$x^{3.6}$")
axs[2].set_title("x vs y log scale")
axs[2].set_xlabel("log(x)")
axs[2].set_ylabel("log(y)")
axs[2].legend()