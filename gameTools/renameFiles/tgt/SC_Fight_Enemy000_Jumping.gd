extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func enter():
	.enter()
	owner.current_y_speed = Properties.PLAYER_SPEED.Y_SPEED

func analyze_conditions():
	var input = state_machine.input
	var just_pressed_input = input.just_pressed_input

	if input.state == Enums.INPUT_STATES.BUSY \
		&& just_pressed_input != null:
		match just_pressed_input:
			Constants.INPUT_EVENT_NAMES.LIGHT_ATK:
				set_next_state(Constants.STATE_NAMES.LIGHT_ATK_IN_AIR, Enums.SWITCH_FLAG.OFF)
				return
			Constants.INPUT_EVENT_NAMES.HEAVY_ATK:
				set_next_state(Constants.STATE_NAMES.HEAVY_ATK_IN_AIR_PT_1, Enums.SWITCH_FLAG.OFF)
				return

	if owner.current_y_speed + 2 *  Properties.PLAYER_SPEED.Y_ACC <= 0:
		set_next_state(Constants.STATE_NAMES.DROPPING, Enums.SWITCH_FLAG.OFF)

func do_action():
	owner.ver_move(Properties.PLAYER_SPEED.Y_ACC)
	move_in_action(Properties.PLAYER_SPEED.X_SPEED_IN_AIR, true)