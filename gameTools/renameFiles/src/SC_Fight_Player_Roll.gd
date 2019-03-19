extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func do_action():
	owner.hor_move(owner.orientation, Properties.PLAYER_SPEED.X_SPEED, false)