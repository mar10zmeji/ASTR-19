{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "e420320d-caea-4a77-a672-7a2460986092",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np \n",
    "def sin_x(x):\n",
    "    return np.sin(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b04b5e5a-a415-4c81-bb9f-383a0d960ccb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def cos_x(x):\n",
    "    return np.cos(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4fd73c4a-2801-4408-b755-bcb97b31d46c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "from astropy.table import Table \n",
    "x = np.linspace(0,2*np.pi,1000) # creates the default values for x\n",
    "ta = Table([x,sin_x(x),cos_x(x)],None,[\"x\", \"sin(x)\", \"cos(x)\"],[float, float, float])\n",
    "# creates the table with three columns of floating point numbers named x, sin(x), and cos(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7d0c6ebb-c6bd-47cd-b5be-f60021ce408c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         x                  sin(x)              cos(x)      \n",
      "-------------------- -------------------- ------------------\n",
      "                 0.0                  0.0                1.0\n",
      "0.006289474781961547 0.006289433316067751 0.9999802213186832\n",
      "0.012578949563923095 0.012578617838741058 0.9999208860571255\n",
      "0.018868424345884642  0.01886730478446709 0.9998219965624732\n",
      " 0.02515789912784619 0.025155245389375847 0.9996835567465339\n",
      " 0.03144737390980774   0.0314421909191206 0.9995055720856215\n",
      "0.037736848691769284  0.03772789267871718   0.99928804962034\n",
      " 0.04402632347373083  0.04401210202238166 0.9990309979553044\n",
      " 0.05031579825569238  0.05029457036336618 0.9987344272588006\n",
      " x  sin(x) cos(x)\n",
      "--- ------ ------\n",
      "0.0    0.0    1.0\n",
      "         x                  sin(x)              cos(x)      \n",
      "-------------------- -------------------- ------------------\n",
      "0.006289474781961547 0.006289433316067751 0.9999802213186832\n",
      "         x                  sin(x)              cos(x)      \n",
      "-------------------- -------------------- ------------------\n",
      "0.012578949563923095 0.012578617838741058 0.9999208860571255\n",
      "         x                  sin(x)             cos(x)      \n",
      "-------------------- ------------------- ------------------\n",
      "0.018868424345884642 0.01886730478446709 0.9998219965624732\n",
      "         x                 sin(x)              cos(x)      \n",
      "------------------- -------------------- ------------------\n",
      "0.02515789912784619 0.025155245389375847 0.9996835567465339\n",
      "         x                sin(x)             cos(x)      \n",
      "------------------- ------------------ ------------------\n",
      "0.03144737390980774 0.0314421909191206 0.9995055720856215\n",
      "         x                  sin(x)            cos(x)     \n",
      "-------------------- ------------------- ----------------\n",
      "0.037736848691769284 0.03772789267871718 0.99928804962034\n",
      "         x                 sin(x)             cos(x)      \n",
      "------------------- ------------------- ------------------\n",
      "0.04402632347373083 0.04401210202238166 0.9990309979553044\n",
      "         x                 sin(x)             cos(x)      \n",
      "------------------- ------------------- ------------------\n",
      "0.05031579825569238 0.05029457036336618 0.9987344272588006\n"
     ]
    }
   ],
   "source": [
    "print(ta[0:9]) # prints the first 10 rows as a single table, doesn't use for\n",
    "for i in ta[0:9]:\n",
    "    print(i) # prints the first 10 rows as individual tables, uses for\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e0a8a9f-1385-42b2-ba3f-567a797ab828",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
