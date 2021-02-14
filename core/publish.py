
#existing
def publish(module_options, asset_name, asset_type):
    if module_options:
        print ('publish with module_options')
    else:
        print ('publish without module options')

#but this has to be changed as
#def publish(asset_name, asset_type):
#i dont know how to get module optipns