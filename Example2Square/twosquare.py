bl_info = {
    "name": "Two Squares Example",
    "author": "Example",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Two Squares",
    "description": "Creates two square planes",
    "category": "Add Mesh",
}

import bpy


class OBJECT_OT_add_two_squares(bpy.types.Operator):
    bl_idname = "object.add_two_squares"
    bl_label = "Add Two Squares"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # First square
        bpy.ops.mesh.primitive_plane_add(
            size=1,
            location=(0, 0, 0)
        )

        # Second square
        bpy.ops.mesh.primitive_plane_add(
            size=1,
            location=(2, 0, 0)
        )

        return {'FINISHED'}


class VIEW3D_PT_two_squares_panel(bpy.types.Panel):
    bl_label = "Two Squares"
    bl_idname = "VIEW3D_PT_two_squares_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Two Squares"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.add_two_squares")


def register():
    bpy.utils.register_class(OBJECT_OT_add_two_squares)
    bpy.utils.register_class(VIEW3D_PT_two_squares_panel)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_two_squares)
    bpy.utils.unregister_class(VIEW3D_PT_two_squares_panel)


if __name__ == "__main__":
    register()
