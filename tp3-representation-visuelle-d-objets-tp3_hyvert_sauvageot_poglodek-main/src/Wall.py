# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:47:50 2017

@author: lfoul
"""
import OpenGL.GL as gl
from Section import Section

class Wall:
    # Constructor
    def __init__(self, parameters = {}) :  
        # Parameters
        # position: position of the wall 
        # width: width of the wall - mandatory
        # height: height of the wall - mandatory
        # thickness: thickness of the wall
        # color: color of the wall        

        # Sets the parameters
        self.parameters = parameters
        
        # Sets the default parameters
        if 'position' not in self.parameters:
            self.parameters['position'] = [0, 0, 0]        
        if 'width' not in self.parameters:
            raise Exception('Parameter "width" required.')   
        if 'height' not in self.parameters:
            raise Exception('Parameter "height" required.')   
        if 'orientation' not in self.parameters:
            self.parameters['orientation'] = 0              
        if 'thickness' not in self.parameters:
            self.parameters['thickness'] = 0.2    
        if 'color' not in self.parameters:
            self.parameters['color'] = [0.5, 0.5, 0.5] 
        if 'edges' not in self.parameters:
            self.parameters['edges'] = False  
            
        # Objects list
        self.objects = []

        # Adds a Section for this object
        self.parentSection = Section({'width': self.parameters['width'], \
                                      'height': self.parameters['height'], \
                                      'thickness': self.parameters['thickness'], \
                                      'color': self.parameters['color'], \
                                      'position': self.parameters['position'], \
                                      'edges' : self.parameters['edges']
                                      })
        self.objects.append(self.parentSection) 
        
    # Getter
    def getParameter(self, parameterKey):
        return self.parameters[parameterKey]
    
    # Setter
    def setParameter(self, parameterKey, parameterValue):
        self.parameters[parameterKey] = parameterValue
        return self                 

    # Finds the section where the object x can be inserted
    def findSection(self, x):
        for item in enumerate(self.objects):
            if isinstance(item[1], Section) and item[1].canCreateOpening(x):
                return item
        return None
    
    # Adds an object    
    def add(self, x):       
        # A compl??ter en rempla??ant pass par votre code
        pass        
                    
    # Draws the faces
    def draw(self):
        gl.glPushMatrix()
        if self.parameters['edges']:
            gl.glTranslatef(self.parameters['position'][0],self.parameters['position'][1],self.parameters['position'][2])   
            gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE) # on trace les faces : GL_FILL
            gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
            gl.glColor3fv([self.parameters['color'][0]*0.8, self.parameters['color'][1]*0.8, self.parameters['color'][2]*0.8])
       
        gl.glRotate(self.parameters['orientation'],0,0,1)   
        gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL) # on trace les faces : GL_FILL
        gl.glBegin(gl.GL_QUADS) # Trac?? d???un quadrilat??re
        gl.glColor3fv([0.5, 0.5, 0.5]) # Couleur gris moyen
            
            
        gl.glEnd()
        gl.glPopMatrix()
        
        for x in self.objects:
            x.draw()
  