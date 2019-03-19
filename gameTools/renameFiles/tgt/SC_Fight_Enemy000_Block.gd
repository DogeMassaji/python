extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func analyze_conditions():
	var input = state_machine.input
	var just_pressed_input = input.just_pressed_input

	if input.state == Enums.INPUT_STATES.BUSY:
		if just_pressed_input != null:
			match just_pressed_input:
				Constants.INPUT_EVENT_NAMES.LIGHT_ATK:
					set_next_state(Constants.STATE_NAMES.COUNTER_ATK_PT_1, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.HEAVY_ATK:
					set_next_state(Constants.STATE_NAMES.COUNTER_ATK_PT_1, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.ROLL:
					set_next_state(Constants.STATE_NAMES.ROLL, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.JUMP:
					set_next_state(Constants.STATE_NAMES.BEFORE_JUMPING, Enums.SWITCH_FLAG.OFF)
				_:
					analyze_default_conditions(input)
		else:
			analyze_default_conditions(input)

	else:
		set_next_state(Constants.STATE_NAMES.IDLE)

func do_action():
	move_in_action(Properties.PLAYER_SPEED.X_SPEED_IN_BLOCK, false)