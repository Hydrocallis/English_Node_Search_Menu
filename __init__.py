bl_info = {
    "name": "English Node Search Menu",
    "author": "KSYN",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "Node Editor > Add Menu",
    "description": "Adds English search functionality to the node editor add menu",
    "warning": "",
    "category": "Node"
}

import bpy

class NODE_OT_search_en_add_menu(bpy.types.Operator):
    bl_idname = "node.search_en_add_menu"
    bl_label = "Search Add Menu (English)"
    bl_description = "Open the add menu search in English"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # 現在の言語設定を保存
        current_lang = context.preferences.view.language
        # UI言語を英語に設定
        context.preferences.view.language = 'en_US'

        # メニューを直接呼び出す
        bpy.ops.wm.search_single_menu("INVOKE_DEFAULT", menu_idname="NODE_MT_add")
        # 言語を元に戻す
        context.preferences.view.language = current_lang
        return {'FINISHED'}

def add_search_operator(self, context):
    self.layout.separator()
    self.layout.operator(NODE_OT_search_en_add_menu.bl_idname)

def register():
    bpy.utils.register_class(NODE_OT_search_en_add_menu)
    bpy.types.NODE_MT_add.append(add_search_operator)

def unregister():
    bpy.types.NODE_MT_add.remove(add_search_operator)
    bpy.utils.unregister_class(NODE_OT_search_en_add_menu)

if __name__ == "__main__":
    register()