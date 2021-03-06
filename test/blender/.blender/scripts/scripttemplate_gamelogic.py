#!BPY
"""
Name: 'GameLogic Example'
Blender: 249
Group: 'ScriptTemplate'
Tooltip: 'Script template with examples of how to use game logic'
"""

from Blender import Window
import bpy

script_data = \
'''
# This script must be assigned to a python controller
# where it can access the object that owns it and the sensors/actuators that it connects to.

# GameLogic has been added to the global namespace no need to import

# for keyboard event comparison
# import GameKeys 

# support for Vector(), Matrix() types and advanced functions like AngleBetweenVecs(v1,v2) and RotationMatrix(...)
# import Mathutils 

# for functions like getWindowWidth(), getWindowHeight()
# import Rasterizer

def main():
	cont = GameLogic.getCurrentController()
	
	# The KX_GameObject that owns this controller.
	own = cont.owner
	
	# for scripts that deal with spacial logic
	own_pos = own.worldPosition
	
	
	# Some example functions, remove to write your own script.
	# check for a positive sensor, will run on any object without errors.
	print 'Logic info for KX_GameObject', own.name
	input = False
	
	for sens in cont.sensors:
		# The sensor can be on another object, we may want to use it
		own_sens = sens.owner
		print '    sensor:', sens.name,
		if sens.positive:
			print '(true)'
			input = True
		else:
			print '(false)'
	
	for actu in cont.actuators:
		# The actuator can be on another object, we may want to use it
		own_actu = actu.owner
		print '    actuator:', actu.name
		
		# This runs the actuator or turns it off
		# note that actuators will continue to run unless explicitly turned off.
		if input:
			cont.activate(actu)
		else:
			cont.deactivate(actu)
	
	# Its also good practice to get sensors and actuators by name
	# rather then index so any changes to their order wont break the script.
	
	# sens_key = cont.sensors['key_sensor']
	# actu_motion = cont.actuators['motion']
	
	
	# Loop through all other objects in the scene
	sce = GameLogic.getCurrentScene()
	print 'Scene Objects:', sce.name
	for ob in sce.objects:
		print '   ', ob.name, ob.worldPosition
	
	
	# Example where collision objects are checked for their properties
	# adding to our objects "life" property
	"""
	actu_collide = cont.sensors['collision_sens']
	for ob in actu_collide.objectHitList:
		# Check to see the object has this property
		if ob.has_key('life'):
			own['life'] += ob['life']
			ob['life'] = 0
	print own['life']
	"""

main()
'''

new_text = bpy.data.texts.new('gamelogic_example.py')
new_text.write(script_data)
bpy.data.texts.active = new_text
Window.RedrawAll()
