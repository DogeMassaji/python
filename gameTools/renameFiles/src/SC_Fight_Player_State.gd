extends "res://scripts/common/stateMachine/State.gd"

onready var state_machine = self.get_parent().get_parent()

signal change_next_state_signal

func _ready():
	self.connect("change_next_state_signal", state_machine, "_change_next_state")
	
func set_next_state(state_name, is_working):
	change_working_state(is_working)
	self.emit_signal("change_next_state_signal", state_name)

func change_working_state(flag):
	is_working = flag

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

func move_in_action(speed, is_flip):
	var input_pool = state_machine.input.input_pool
	var l_r = input_pool[Constants.INPUT_EVENT_NAMES.LEFT].state - \
		input_pool[Constants.INPUT_EVENT_NAMES.RIGHT].state

	if l_r == 1:
		self.owner.hor_move(Enums.ORIENTATION.LEFT, speed, is_flip)
	elif l_r == -1:
		self.owner.hor_move(Enums.ORIENTATION.RIGHT, speed, is_flip)
