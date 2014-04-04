import os

SD = os.path.dirname(__file__)
PP = os.path.join(SD, os.pardir)
PP = os.path.abspath(PP)
TP = os.path.join(PP, 'templates')

print TP