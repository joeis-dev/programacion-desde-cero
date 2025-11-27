age = 16
has_id = False
voucher_was_paid = True
car_documentation = False 
address_documentation = True 
license_exam_approved = True

# and (&&) 
requirement_1 = age >= 18 and voucher_was_paid == True
print(f"Requisito #1: el solicitante cuenta con credencial y voucher de pago? {requirement_1}")

# or (||) 
requirement_2 = address_documentation or has_id 
print(f"Requisito #2: el solicitante cuenta con comprobante de domicilio o su credencial? {requirement_2}")

# not (!) 
requirement_3 = not car_documentation
print(f"Requisito #3: el solicitante cuenta con la documentacion del vehiculo? {requirement_3}")

final_resolution = requirement_1 or requirement_2 and requirement_3 
print(f"El solicitante podra tener acceso a realizar su examen de manejo? {final_resolution}")

