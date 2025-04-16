from scenes.scene import main_scene, name_scene, race_scene
from data import globals

scene_map = {
    "main_scene": main_scene,
    "name_scene": name_scene,
    "race_scene": race_scene,
}

def push_scene(scene_name):
    """Push a new scene into the stack and switch to it.

    Args:
        scene_name (str): The name of the scene to switch to.
    """
    if scene_name in scene_map:
        globals.scene_stack.append(scene_name)
        scene_map[scene_name]()

def pop_scene():
    """Pop the current scene from the stack and switch to the previous scene."""
    if len(globals.scene_stack) > 1:
        globals.scene_stack.pop()
        current_scene = globals.scene_stack[-1]
        scene_map[current_scene]()
