"""Dev-time generator for data/startup.blend (needs a GUI session: run under tools/kwin-rig.sh style headless Wayland).

    BLENDER_USER_RESOURCES=<tmp> blender --python startup/amerika_startup.py --python tools/make_startup.py

Saves the home file (startup.blend) with the 'Vigil Render' workspace active, an empty-ish scene (camera + sun) and metric units.
Copy <tmp>/config/startup.blend to data/startup.blend.
"""
import os
import bpy


def go():
    from amerika_render import ui
    cube = bpy.data.objects.get('Cube')
    if cube:
        bpy.data.objects.remove(cube)
    sc = bpy.context.scene
    sc.unit_settings.system = 'METRIC'
    sc.unit_settings.scale_length = 1.0
    ui.ensure_workspace()
    bpy.app.timers.register(save, first_interval=2.5)
    return None


def save():
    # drop the transient review text so the template starts clean
    for t in list(bpy.data.texts):
        if t.name == 'Render Review':
            t.clear()
    assert bpy.data.workspaces.get('Vigil Render'), 'Vigil Render workspace was not created'
    screenshot=os.environ.get('VIGIL_RENDER_SCREENSHOT')
    if screenshot:
        with bpy.context.temp_override(window=bpy.context.window_manager.windows[0]):
            bpy.ops.screen.screenshot(filepath=screenshot)
    bpy.ops.wm.save_homefile()
    print('Vigil Render startup template saved')
    bpy.ops.wm.quit_blender()
    return None


bpy.app.timers.register(go, first_interval=1.5)
