import bpy

depthText = 0.3
depthStand = (depthText/5)+0.0000000001
heightStand = depthText/13
resizeX = 1
resizeY = 1
resizeZ = 1


#f = open('C:/Example/testNames', "r") // Read in from file
f = ("PAUL","JO","TOM")

ypos = 1

#fnt = bpy.data.fonts.load('C:\\WeddingPrints\\HelveticaNeueBold.ttf') // Use a custom font if required

for line in f:
    nameTag = line.rstrip()
    if nameTag == "":
        continue
    print ("PROCESSING: "+line)
    ypos = ypos - 1
    bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    textName = bpy.context.active_object.name 
    
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
    for i in nameTag:
        bpy.ops.font.text_insert(text=i, accent=False)
    bpy.ops.object.editmode_toggle()
    #bpy.data.objects[textName].data.font = fnt

		
    bpy.ops.object.convert(target='MESH', keep_original=False)
    coPlanRand = 0.0000001
    for i in bpy.data.objects[textName].data.vertices:
        if (i.co[1] < 0):
            i.co[1] = 0
    lowestX = 100
    highestX = -1
    for i in bpy.data.objects[textName].data.vertices:
        if (i.co[1] == 0):
            if i.co[0] < lowestX:
                lowestX = i.co[0]
    for i in bpy.data.objects[textName].data.vertices:
        if (i.co[1] == 0):
            if i.co[0] > highestX:
                highestX = i.co[0]                
    for i in bpy.data.objects[textName].data.vertices:
        if (i.co[1] == 0):
            i.co[1] = 0+coPlanRand
            coPlanRand += 0.0000001
    print("Lowest is "+str(lowestX))
    print("Highest is "+str(highestX))
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, depthText), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "texture_space":False, "release_confirm":False})
    bpy.ops.object.editmode_toggle()
    
    # Add the cube
    bpy.ops.mesh.primitive_cube_add(view_align=False, enter_editmode=False, location=(0, 0, 0), rotation=(0, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    cubeName = bpy.context.active_object.name
    # Centre the cube
    bpy.ops.object.editmode_toggle()
    bpy.ops.transform.translate(value=(1, 1, 1), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)    
    bpy.ops.object.editmode_toggle()

    # Resize to be depth of the text
    
    
    # Line up with start
    bpy.ops.transform.translate(value=(lowestX, 0, -0.0000001), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)    
    
    # Resize to target size
    bpy.ops.transform.resize(value=((highestX-lowestX)/2, heightStand, depthStand), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    
    bpy.context.scene.objects.active = bpy.data.objects[textName]
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'UNION'
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects['Cube']
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
    bpy.context.scene.objects.active = bpy.data.objects[cubeName]
    bpy.ops.object.delete(use_global=False) 
    
    bpy.data.objects[textName].location.y = -ypos
    bpy.context.scene.objects.active = bpy.data.objects[textName]
    bpy.data.objects[textName].select = True
    
    # Final mesh resize for print    
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.mesh.select_all(action='TOGGLE')
    bpy.ops.transform.resize(value=(0.7*1.4375,0.7*1.4375,0.7*1.4375*1.108214), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), texture_space=False, release_confirm=False)
    bpy.ops.object.editmode_toggle()    
    
    # The below line will export an stl to the file path directory
    #bpy.ops.export_mesh.stl(check_existing=False, filepath=("%s.stl" % nameTag), filter_glob="*.stl", ascii=False, apply_modifiers=True)
