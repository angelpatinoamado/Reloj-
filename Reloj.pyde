coordinate_Ya = -40
coordinate_Yb = -40
coordinate_Yc = -40

def setup():
{
    size(600, 600)
}
    
def draw():
{
    background(0)
    
    global coordinate_Ya
    global coordinate_Yb
    global coordinate_Yc
    
            
    strokeWeight(3)
 
    line (200, 0, 200, 600)
    stroke (255)

    line (400, 0, 400, 600)
    stroke (255)


    circle (100, coordinate_Ya, 80)
    fill (255)
    
    if coordinate_Ya > height: 
       coordinate_Ya = -40 
       
    else: 
       coordinate_Ya = map(second(), 0, 59, -40, height)
       
    strokeWeight(3)

    line (0, 300, 200, 300)
    stroke (255)
       
       
    circle (width / 2, coordinate_Yb, 80)
    fill (254, 255, 10)
    
    if coordinate_Yb > height:
       coordinate_Yb = -40
     
    else:  
       coordinate_Yb = map(minute(), 0, 59, -40, height)
       
       
    strokeWeight(3)
    
    line (200, 100, 400, 100)
    stroke (255)

    line (200, 200, 400, 200)
    stroke (255)

    line (200, 300, 400, 300)
    stroke (255)

    line (200, 400, 400, 400)
    stroke (255)
    
    line (200, 500, 400, 500)
    stroke (247, 140, 7)

    circle (500, coordinate_Yc, 80)
    fill (255)
    
    if coordinate_Yc > height:
       coordinate_Yc = -40
     
    else:  
       coordinate_Yc = map(hour(), 0, 23, -40, height)
         
    strokeWeight(3)
    
    line (400, 150, 600, 150)
    stroke (96, 224, 245)

    line (400, 300, 600, 300)
    stroke (8, 2, 205)
    
    line (400, 450, 600, 450)
    stroke (255)
}
   






    
    
   
       
    

        

   
    
    


    
       
