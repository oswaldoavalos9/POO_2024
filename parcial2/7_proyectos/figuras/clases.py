# crear clase

class figura:
 
 def _init_(self,calcular_area):
         self.calcular_area = calcular_area

 def getcalcular_area(self):
      return self.calcular_area

 def setcalcular_area(self,calcular_area):
      self.calcular_area = calcular_area 

 def getInfo(self):
      print(f"calcular_areal: "{set.getcalcular_area})
    



# definir sub clase/clase secundaria

class rectangulo:
        
 def _init_(self,ancho,largo):
        self.ancho = ancho
        self.largo = largo
              
 def getancho(self):
      return self.ancho
              
 def setancho(self,ancho):
      self.ancho = ancho             

 def getlargo(self):
      return self.largo
              
 def setlargo(self,largo):
      self.largo = largo
              
 def getInfo(self):
      print(f"calcular_areal: "{set.getcalcular_area})
              


class circulo:
 
 def _init_(self,radio):
        self.radio = radio
              
 def getradio(self):
      return self.radio
              
 def setradio(self,radio):
      self.radio = radio 
              
 def getInfo(self):  
      print(f"radio: "{set.getradio}) 
    


class triangulo:
 
 def _init_(self,ancho,altura):
        self.ancho = ancho
        self.altura = altura

 def getancho(self):
      return self.ancho
              
 def setaltura(self,altura):
      self.altura = altura
              
 def getInfo(self):
    print(f"calcular_areal: "{set.getcalcular_area})
              