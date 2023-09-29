{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/Guillermo2468/Computo-en-la-Nube/blob/main/es_primo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "id": "TZIAoCUqeHfD",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a1e8c2f8-374c-4489-bfd0-670b713b2153"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Writing es_primo.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile es_primo.py\n",
        "def es_primo(numero):\n",
        "    if numero <= 1:\n",
        "        return False\n",
        "    for i in range(2, int(numero**0.5) + 1):\n",
        "        if numero % i == 0:\n",
        "            return False\n",
        "    return True\n",
        "\n"
      ]
    }
  ]
}