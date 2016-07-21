import pygame

#Reaper
##width = 64
##height = 64
##rows = 9
##columns = 5 #(number of frames)
##imagename = "Reaper.png"

#Bat
##width = 1047 / 4
##height = 1059 /4
##rows = 4
##columns = 3
##imagename = "bat.png"

#Boulder
##width = 96
##height = 96
##rows = 4
##columns = 3
##imagename = "boulder.png"

#bomb
width= 64
height = 64
rows = 4
columns = 4
imagename = "ghost 3.png"

pygame.display.init()
screen = pygame.display.set_mode((int(width),int(height*rows)))
clock = pygame.time.Clock()
done = False

img = pygame.image.load(imagename)
timeroriginal = .15
timer = timeroriginal
increment = 0

while not done:
	screen.fill((0,0,0))

	dT = clock.tick() / 1000.0
	timer -= dT
	if timer <= 0:
		increment += 1
		if increment == columns:
			increment = 0
		timer = timeroriginal

	pygame.event.pump()
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		done = True

	screen.blit(img, (0 - ((width)*increment),0))

	pygame.display.flip()
pygame.display.quit()