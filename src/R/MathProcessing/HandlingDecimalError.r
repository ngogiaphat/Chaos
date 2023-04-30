#Calculating world population density in 2022
#World population in 2022
pop <- 7852354000  
#Land area in the world          
area <- 510072000      
#Calculate population density    
density <- pop / area      
#Round to 3 decimal places
density <- round(density, 3)
#Print population density in a number format with thousands separators
cat("Mật độ dân số thế giới năm 2022 là:", format(density, big.mark = ",", scientific = FALSE), "người/km²")