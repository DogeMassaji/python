extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func enter():
	.enter()
	owner.position.y = Properties.PLAYER_INIT_POSITION.Y
