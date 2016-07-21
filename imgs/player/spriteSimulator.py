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
width= 192
height = 192
rows = 4
columns = 4
imagename = "bow_Power.png"
img2 = "Archer.png"

pygame.display.init()
screen = pygame.display.set_mode((int(width),int(height*rows)))
clock = pygame.time.Clock()
done = False

img = pygame.image.load(imagename)
playerImg = pygame.image.load(img2)
timeroriginal = .15
timer = timeroriginal
increment = 0

while not done:
	screen.fill((255, 255, 255))

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

	screen.blit(playerImg, (68, 38), (0, 768, 64, 64))
	screen.blit(playerImg, (68, 230), (0, 832, 64, 64))
	screen.blit(playerImg, (68, 614), (0, 960, 64, 64))
	screen.blit(img, (0 - ((width)*increment),0))
	screen.blit(playerImg, (68, 422), (0, 896, 64, 64))


	pygame.display.flip()
pygame.display.quit()