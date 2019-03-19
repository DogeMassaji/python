extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func analyze_conditions():
	var input = state_machine.input
	var just_pressed_input = input.just_pressed_input

	if input.state == Enums.INPUT_STATES.BUSY \
		&& owner.action_state == Enums.ACTION_STATES.AFTER_ACTION:
		if just_pressed_input != null:
			match just_pressed_input:
				Constants.INPUT_EVENT_NAMES.LEFT:
					set_next_state(Constants.STATE_NAMES.RUN, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.RIGHT:
					set_next_state(Constants.STATE_NAMES.RUN, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.LIGHT_ATK:
					set_next_state(Constants.STATE_NAMES.COMBO_2, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.HEAVY_ATK:
					set_next_state(Constants.STATE_NAMES.COMBO_3, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.ROLL:
					set_next_state(Constants.STATE_NAMES.ROLL, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.JUMP:
					set_next_state(Constants.STATE_NAMES.BEFORE_JUMPING, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.SKILL:
					set_next_state(Constants.STATE_NAMES.SKILL, Enums.SWITCH_FLAG.OFF)