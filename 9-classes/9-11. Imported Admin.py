from admin_privileges_module import Admin

admin = Admin('saul', 'luk')
saul_privileges = ['r','w','d']
admin.privileges.privileges = saul_privileges
admin.privileges.show_privileges()


