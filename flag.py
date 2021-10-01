from cryptography.fernet import Fernet

key = b'SVtmKLWWrfZ52PJekIVo92EmRXc76XT4fiemiTpwVKg='

flag = b'gAAAAABhVyPrVWg1bEYswViq0A6P-weuQ0KZqoEVMJU1yE4Thl6-DT3Hu5v6zzCkTfsY_6h5UWaHBudb7gSotdErBv0ZKM9dRlNikwZ8GcpMYDM--W8xOsTf9C1Euy5I-72FC-G8NCEk'

fernet = Fernet(key)

decMessage = ''

print("decrypted string: ", decMessage)
