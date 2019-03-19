extends "res://scripts/main/SC_Fight/characters/player/states/SC_Fight_Player_State.gd"

func analyze_conditions():
	var input = state_machine.input
	var just_pressed_input = input.just_pressed_input
	var input_pool = input.input_pool
	var states_stack = state_machine.states_stack

	if input.state == Enums.INPUT_STATES.BUSY:
		if just_pressed_input != null:
			match just_pressed_input:
				Constants.INPUT_EVENT_NAMES.LEFT:
					if input_pool[Constants.INPUT_EVENT_NAMES.LEFT].state - \
						input_pool[Constants.INPUT_EVENT_NAMES.RIGHT].state == 0:
						set_next_state(Constants.STATE_NAMES.IDLE, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.RIGHT:
					if input_pool[Constants.INPUT_EVENT_NAMES.LEFT].state - \
						input_pool[Constants.INPUT_EVENT_NAMES.RIGHT].state == 0:
						set_next_state(Constants.STATE_NAMES.IDLE, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.LIGHT_ATK:
					if (states_stack.size() > 0 \
						&& states_stack[-1] == Constants.STATE_NAMES.LIGHT_ATK) \
						|| (states_stack.size() > 1 \
						&& states_stack[-2] == Constants.STATE_NAMES.LIGHT_ATK):
						set_next_state(Constants.STATE_NAMES.COMBO_1, Enums.SWITCH_FLAG.OFF)
					elif (states_stack.size() > 0 \
						&& states_stack[-1] == Constants.STATE_NAMES.COMBO_1) \
						|| (states_stack.size() > 1 \
						&& states_stack[-2] == Constants.STATE_NAMES.COMBO_1):
						set_next_state(Constants.STATE_NAMES.COMBO_2, Enums.SWITCH_FLAG.OFF)
					else:
						set_next_state(Constants.STATE_NAMES.LIGHT_ATK, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.HEAVY_ATK:
					if (states_stack.size() > 0 \
						&& states_stack[-1] == Constants.STATE_NAMES.COMBO_1) \
						|| (states_stack.size() > 1 \
						&& states_stack[-2] == Constants.STATE_NAMES.COMBO_1):
						set_next_state(Constants.STATE_NAMES.COMBO_3, Enums.SWITCH_FLAG.OFF)
					else:
						set_next_state(Constants.STATE_NAMES.HEAVY_ATK, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.BLOCK:
					set_next_state(Constants.STATE_NAMES.BLOCK, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.ROLL:
					set_next_state(Constants.STATE_NAMES.ROLL, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.JUMP:
					set_next_state(Constants.STATE_NAMES.BEFORE_JUMPING, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.SKILL:
					set_next_state(Constants.STATE_NAMES.SKILL, Enums.SWITCH_FLAG.OFF)
				_:
					analyze_default_conditions(input)
		else:
			analyze_default_conditions(input)
	else:
		set_next_state(Constants.STATE_NAMES.IDLE, Enums.SWITCH_FLAG.OFF)

func do_action():
	move_in_action(Properties.PLAYER_SPEED.X_SPEED, true)