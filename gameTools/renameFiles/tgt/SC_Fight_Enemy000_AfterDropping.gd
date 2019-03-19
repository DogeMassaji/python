extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func enter():
	.enter()
	owner.position.y = Properties.PLAYER_INIT_POSITION.Y

func analyze_conditions():
	var input = state_machine.input
	var just_pressed_input = input.just_pressed_input

	if input.state == Enums.INPUT_STATES.BUSY:
		if just_pressed_input != null:
			match just_pressed_input:
				Constants.INPUT_EVENT_NAMES.JUMP:
					set_next_state(Constants.STATE_NAMES.BEFORE_JUMPING, Enums.SWITCH_FLAG.OFF)
