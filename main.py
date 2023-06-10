import pygame 



class Players:
    def __init__(self) -> None:
        self.score1 = 0
        self.score1 = 0
        
    def move(self, player, i):            
        return player | (1 << i)
    
    def getBit(self, player, bitPosition):
        if bitPosition == None: return
        return False if (player & (1 << bitPosition)) == 0 else True
    
    def isPlaced(self, i):
        return (self.getBit(self.player1, i) == 1 or self.getBit(self.player2, i) == 1)
             
    def checkWinner(self):
        WIN = [448, 56, 7, 292, 146, 73, 84, 273]
        player = self.player1;
        for i in range(2):
            for element in WIN:
                if ((player & element) == element):
                    return (True, "X") if (i == 0) else (True, "O")
            player = self.player2;
        return (False, None);
    

class Field():
    def __init__(self):
        self.pos = [(30, 30),(95, 30),(160, 30),(30, 95),(95, 95),(160, 95),(30, 160),(95, 160),(160, 160)]
    
    def draw_field(self):
        for y in range(3):
            for x in range(3):
                box = pygame.Rect(pygame.Rect(30, 30, 60, 60))
                box.move_ip(y*65, x*65)
                pygame.draw.rect(self.screen, (0, 0, 0), box, 1)

    def inField(self, pos):
        for (i, element) in enumerate(self.pos):
            if (pos[0] > element[0] and pos[0] < element[0]+60) and (pos[1] > element[1] and pos[1] < element[1]+60):
                return i

    def drawMoves(self):
        for i in range(9):
            if self.getBit(self.player1, i) == 1: self.draw_x(i)
            elif self.getBit(self.player2, i) == 1: self.draw_o(i)
    
    def draw_x(self, square):
        if square == None: return
        x, y = self.pos[square]
        for i in range(5):
            pygame.draw.aaline(self.screen,"black",(x+i,y),(x+60,y+60-i))  
            pygame.draw.aaline(self.screen,"black",(x+60,y+i),(x+i,y+60))  
            
    def draw_o(self, square):
        if square == None: return
        x, y = self.pos[square]
        for i in range(5):
            pygame.draw.circle(self.screen, "black", [x+30,y+30] , 30)
            
        
class App(Players, Field):
    def __init__(self) -> None:
        super(Players, self).__init__()
        super(Field, self).__init__()
        self.player1 = 0
        self.player2 = 0
        self.counter = 0
        pygame.init()
        self.screen = pygame.display.set_mode([160+60+35, 160+60+35])
        pygame.display.set_caption('TicTacToe')
        self.screen.fill((255, 255, 255))
        self.draw_field()
        pygame.display.flip()
        
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            self.draw_field()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    f = self.inField(pos)
                    # make move 
                    if (f != None and self.isPlaced(f) == False):
                        if self.counter % 2 == 0: 
                            self.player1 = self.move(self.player1, f) 
                        else:
                            self.player2 = self.move(self.player2, f)
                        self.counter+=1 
                    self.drawMoves()
                    
                    win = self.checkWinner()
                    if win[0] == True:
                        self.clear()
                        font = pygame.font.SysFont("freesansbold.ttf", 32)
                        text = font.render(f"won: {win[1]}", True, "black", "white")
                        textRect = text.get_rect()
                        textRect.center = (130, 235)
                        self.screen.blit(text, textRect)
                    pygame.display.flip()
        pygame.quit()
        
    def clear(self):
        self.player1 = 0
        self.player2 = 0
        self.counter = 0

if __name__ == "__main__":
    App()