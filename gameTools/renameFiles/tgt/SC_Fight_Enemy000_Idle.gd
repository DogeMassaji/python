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
				Constants.INPUT_EVENT_NAMES.LEFT:
					set_next_state(Constants.STATE_NAMES.RUN, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.RIGHT:
					set_next_state(Constants.STATE_NAMES.RUN, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.LIGHT_ATK:
					set_next_state(Constants.STATE_NAMES.LIGHT_ATK, Enums.SWITCH_FLAG.OFF)
				Constants.INPUT_EVENT_NAMES.HEAVY_ATK:
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

func analyze_default_conditions(input):
	var input_pool = input.input_pool
	#Block
	if input_pool[Constants.INPUT_EVENT_NAMES.BLOCK].state == Enums.INPUT_EVENT_STATES.PRESSED:
		set_next_state(Constants.STATE_NAMES.BLOCK, Enums.SWITCH_FLAG.OFF)
		return

	# idle action has a check of run action
	# cause run action could switch idle state while the player press LEFT and RIGHT at the same time.
	# Run
	if (input_pool[Constants.INPUT_EVENT_NAMES.LEFT].state != \
		input_pool[Constants.INPUT_EVENT_NAMES.RIGHT].state):
		set_next_state(Constants.STATE_NAMES.RUN, Enums.SWITCH_FLAG.OFF)
		return

	set_next_state(Constants.STATE_NAMES.IDLE, Enums.SWITCH_FLAG.OFF)