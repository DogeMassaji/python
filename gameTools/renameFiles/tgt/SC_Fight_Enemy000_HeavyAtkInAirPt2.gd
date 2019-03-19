extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func analyze_conditions():
	if owner.position.y - (2 * owner.current_y_speed + 3 * Properties.PLAYER_SPEED.Y_ACC) >= \
		Properties.PLAYER_INIT_POSITION.Y:
		set_next_state(Constants.STATE_NAMES.HEAVY_ATK_IN_AIR_PT_3, Enums.SWITCH_FLAG.OFF)

func do_action():
	owner.ver_move(Properties.PLAYER_SPEED.Y_FAST_ACC)
