<<<<<<< HEAD
# resivi de luz


khw = int(input("cuantos kww cunsumio: "))

if khw <= 150 :
    khw_basico = khw * 0.987 
    print("monto a pagar:")
    print(khw_basico)
    khw_IVA = khw_basico * 1.16
    print("monto a pagar con IVA:")
    print(khw_IVA)
    khw_DAP = khw_IVA + 12.5
    print("monto a pagar con DAP (FINAL):")
    print(khw_DAP)
    
if khw >= 151 :
    khw_bas = 150 * 0.987
    khw_int = (khw - 150) * 1.203 
    khw_basico = khw_bas + khw_int
    print("monto a pagar:")
    print(khw_basico)
    khw_IVA = khw_basico * 1.16
    print("monto a pagar con IVA:")
    print(khw_IVA)
    khw_DAP = khw_IVA + 12.5
    print("monto a pagar con DAP (FINAL):")
    print(khw_DAP)
    
=======
# resivi de luz


khw = int(input("cuantos kww cunsumio: "))

if khw <= 150 :
    khw_basico = khw * 0.987 
    print("monto a pagar:")
    print(khw_basico)
    khw_IVA = khw_basico * 1.16
    print("monto a pagar con IVA:")
    print(khw_IVA)
    khw_DAP = khw_IVA + 12.5
    print("monto a pagar con DAP (FINAL):")
    print(khw_DAP)
    
if khw >= 151 :
    khw_bas = 150 * 0.987
    khw_int = (khw - 150) * 1.203 
    khw_basico = khw_bas + khw_int
    print("monto a pagar:")
    print(khw_basico)
    khw_IVA = khw_basico * 1.16
    print("monto a pagar con IVA:")
    print(khw_IVA)
    khw_DAP = khw_IVA + 12.5
    print("monto a pagar con DAP (FINAL):")
    print(khw_DAP)
    
>>>>>>> ddb1045bbb29ea5fca236c962e8dd2c8efc2216f
