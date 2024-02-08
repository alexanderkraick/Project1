from direct.showbase.ShowBase import ShowBase
class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetScene()

    def SetScene(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        
        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        
        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(1150, 5000, 67)
        self.Planet2.setScale(350)
        
        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(2150, 5000, 67)
        self.Planet3.setScale(350)
        
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(3150, 5000, 67)
        self.Planet4.setScale(350)
        
        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(4150, 5000, 67)
        self.Planet5.setScale(350)
        
        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(5150, 5000, 67)
        self.Planet6.setScale(350)
        
        self.Spaceship = self.loader.loadModel("./Assets/Spaceship/theBorg.x")
        self.Spaceship.reparentTo(self.render)
        self.Spaceship.setPos(2000, 2000, 500)
        self.Spaceship.setScale(10)
        
        self.SpaceStation = self.loader.loadModel("./Assets/Space_Station/spaceStation.x")
        self.SpaceStation.reparentTo(self.render)
        self.SpaceStation.setPos(2000, 3000, 1000)
        self.SpaceStation.setScale(30)
        
        self.tex = self.loader.loadTexture("./Assets/Universe/space-galaxy.jpg")
        self.Universe.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Planets/Moon.jpg")
        self.Planet1.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Planets/Venus.jpg")
        self.Planet2.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Planets/Earth.jpg")
        self.Planet3.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Planets/Jupiter.jpg")
        self.Planet4.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Planets/Mars.jpg")
        self.Planet5.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Planets/Pluto.jpg")
        self.Planet6.setTexture(self.tex, 1)
        
        self.tex = self.loader.loadTexture("./Assets/Spaceship/theBorg.jpg")
        self.Spaceship.setTexture(self.tex, 1)
    
    
    
app = SpaceJam()
app.run()