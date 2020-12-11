{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Employee:\n",
    "    \n",
    "    def __init__(self,first,last,pay):\n",
    "        self.first= first\n",
    "        self.last= last\n",
    "        self.pay= pay\n",
    "        self.email = first + '.' + last + '@company.com'\n",
    "    \n",
    "    def fullname(self):\n",
    "        return '{} {}'.format(self.first, self.last)\n",
    "    \n",
    "    def apply_raise(self):\n",
    "        self.pay = self.pay*1.04\n",
    "       \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "emp1 = Employee('Arnab', 'Das', 90019)\n",
    "emp2 = Employee('Some', 'One', 50000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Arnab Das'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp1.fullname()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "101259.13241600001"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "emp1.apply_raise()\n",
    "emp1.pay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class dataset:\n",
    "    def __init__(self,final,sim,runrate,unknown):\n",
    "        self.final = pickle(final)\n",
    "        self.sim = pickle(sim)\n",
    "        self.runrate = pickle(sim)\n",
    "        self.unknown = pickle(unknown)\n",
    "        \n",
    "    def histograms(i):\n",
    "        final1.iloc[i].plot 9a\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "quarter1 = dataset(final1,sim1,runrate1,simq1fy19)\n",
    "quarter2 = dataset(final2,sim2,runrate2,simq2fy19)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.5.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
