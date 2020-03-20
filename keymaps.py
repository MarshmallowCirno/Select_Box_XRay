import bpy


addon_keymaps = []


def register_keymaps():    
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Mesh", space_type='EMPTY')

        kmi = km.keymap_items.new("mesh.select_box_xray", 'EVT_TWEAK_R', 'ANY')
        kmi.properties.mode = 'SET'
        kmi.properties.select_through = True
        kmi.properties.select_all_faces = False
        kmi.properties.select_all_edges = False
        kmi.properties.show_xray = False
        kmi.properties.wait_for_input = False
        kmi.properties.hide_modifiers = True
        kmi.active = False
        addon_keymaps.append((km, kmi))
                
        kmi = km.keymap_items.new("mesh.select_box_xray", 'EVT_TWEAK_R', 'ANY', shift=True)
        kmi.properties.mode = 'ADD'
        kmi.properties.select_through = True
        kmi.properties.select_all_faces = False
        kmi.properties.select_all_edges = False
        kmi.properties.show_xray = True
        kmi.properties.wait_for_input = False
        kmi.properties.hide_modifiers = True
        kmi.active = False
        addon_keymaps.append((km, kmi))
        
        kmi = km.keymap_items.new("mesh.select_box_xray", 'EVT_TWEAK_R', 'ANY', ctrl=True)
        kmi.properties.mode = 'SUB'
        kmi.properties.select_through = True
        kmi.properties.select_all_faces = False
        kmi.properties.select_all_edges = False
        kmi.properties.wait_for_input = False
        kmi.properties.show_xray = True
        kmi.properties.hide_modifiers = True
        kmi.active = False
        addon_keymaps.append((km, kmi))
        
        km = kc.keymaps.new(name="Object Mode", space_type='EMPTY')

        kmi = km.keymap_items.new("object.select_box_xray", 'EVT_TWEAK_R', 'ANY')
        kmi.properties.mode = 'SET'
        kmi.properties.wait_for_input = False
        kmi.active = False
        addon_keymaps.append((km, kmi))
        
        kmi = km.keymap_items.new("object.select_box_xray", 'EVT_TWEAK_R', 'ANY', shift=True)
        kmi.properties.mode = 'ADD'
        kmi.properties.wait_for_input = False
        kmi.active = False
        addon_keymaps.append((km, kmi))
        
        kmi = km.keymap_items.new("object.select_box_xray", 'EVT_TWEAK_R', 'ANY', ctrl=True)
        kmi.properties.mode = 'SUB'
        kmi.properties.wait_for_input = False
        kmi.active = False
        addon_keymaps.append((km, kmi))


def unregister_keymaps():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    

def register():
    register_keymaps()


def unregister():
    unregister_keymaps()