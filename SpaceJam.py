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
        tex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(self.tex, 1)


app = SpaceJam()
app.run()