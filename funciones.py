{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMtRNLu/JhVeUssYYsR7Mwq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Guillermo2468/Computo-en-la-Nube/blob/main/funciones.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "TuXo3WMG55JW"
      },
      "outputs": [],
      "source": [
        "def es_primo(numero):\n",
        "    if numero <= 1:\n",
        "        return False\n",
        "    for i in range(2, int(numero**0.5) + 1):\n",
        "        if numero % i == 0:\n",
        "            return False\n",
        "    return True\n"
      ]
    }
  ]
}