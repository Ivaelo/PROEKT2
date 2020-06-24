import pygame
import random
import sys

pygame.init()
#v = pygame.Vector2()
#v.xy = 400, 300
#v[:] = 400, 300

radius=50
Green = (0,255,0)
RED=(255,0,0)
w=800
h =600
p_s=50;
p_p=(w/2,h-2*p_s)
vi_size=50
vi_ovre=[random.randint(0,w-vi_size),0]
v_l=[vi_ovre]
sp=10
s = pygame.display.set_mode((w,h))
game_over = False
Clock = pygame.time.Clock()
def dv(v_l):
	delay = random.random()
	if len(v_l) < 10 and delay < 0.1:
		x_pos = random.randint(0,w-vi_size)
		y_pos = 0
		v_l.append([x_pos, y_pos])

def d_v(v_l):
	for vi_ovre in v_l:	
		pygame.draw.rect(s,RED,(vi_size[0],vi_size[1],vi_ovre,vi_ovre),)
def d_c(p_p,p_s):

	px = p_p[0]
	py = p_p[1]
	vx = vi_ovre[0]
	vy = vi_ovre[1]
	if (vx >= px and vx < (px + p_s)) or (px >= vx and px < (vx+vi_size)):
		if (vy >= py and vy < (py + p_s)) or (py >= vy and py < (vy+vi_size)):
			return True
	return False
def uvp(v_l, score):
	for idx, vi_ovre in enumerate(v_l):
		if vi_ovre[1] >= 0 and vi_ovre[1] < HEIGHT:
			vi_ovre[1] += SPEED
		else:
			v_l.pop(idx)
			score += 1
	return score
while not game_over:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.K_LEFT:
			x-=radius
		elif event.type==pygame.K_RIGHT:
			x+=radius
		
			
	#screen.fill((0,0,0))
	#if vi_ovre[1]>0 and vi_ovre[1]<h:
		#vi_ovre[1]+=sp
	#else:
		#vi_ovre[0]= random.ramdint(0,w-vi_ovre)
		#vi_ovre[1]=1
	if d_c(p_p,p_s):
		game_over=True
	#s.fill(0,0,255)
	dv(v_l)
	d_v(v_l)
	score= uvp(v_l,score)
	
	#pygame.draw.rect(screen,RED,(vi_size[0],vi_size[1],vi_ovre,vi_ovre),)
	pygame.draw.rect(s,green,(p_p[0],p_p[1],p_p,p_p))
	clock.tick(30)
	pygame.display.update()
