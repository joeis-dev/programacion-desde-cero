clean_room = False
water_plants = True 
do_dishes = False
essay_social_networks = True
binary_tree_balancing_homework = False 
bash_script_homework = True

can_use_social_networks = (clean_room and (water_plants or do_dishes)) and (essay_social_networks and binary_tree_balancing_homework and bash_script_homework)
print(f"Puede Pablo usar un rato las redes sociales? {can_use_social_networks}")