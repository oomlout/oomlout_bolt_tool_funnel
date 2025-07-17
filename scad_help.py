import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad
###### utilities

def make_parts(**kwargs):
    parts = kwargs.get("parts", [])
    filter = kwargs.get("filter", "")
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")            
            extra = part["kwargs"].get("extra", "")
            if filter in name or filter in extra:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                
            else:
                print(f"skipping {part['name']}")

    #run oomp
    oomp_run = kwargs.get("oomp_run", False)
    if kwargs.get("oomp_run", False):
        import action_build_oomp
        action_build_oomp.main()

def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    try:
        func = getattr(scad, f"get_{name}")
    except AttributeError:
        func = None
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        scad.get_base(thing, **kwargs)   

    oomp_mode = kwargs.get("oomp_mode", "project")
    
    if oomp_mode == "project":
        descmain = ""
        current_description_main = thing.get("description_main", "default")
        current_size = thing.get("size", "default")
        new_size = current_size.replace(f"{project_name}_", "")
        descmain = f"{new_size}_{current_description_main}"
        kwargs["oomp_description_main"] = f"{descmain}"
        descextra = ""
        current_description_extra = thing.get("description_extra", "")
        descextra = f"{current_description_extra}"
        kwargs["oomp_description_extra"] = f"{descextra}"
    elif oomp_mode == "oobb":
        current_description_main = thing.get("description_main", "default")   
        descmain = f"{current_description_main}" 

        descextra = thing.get("extra", "")    
        if descextra != "":
            descextra = f"{descextra}_extra"
        kwargs["oomp_description_main"] = f"{current_description_main}"
        kwargs["oomp_description_extra"] = f"{descextra}"
        kwargs["oomp_size"] = f"{part["name"]}"

    #move oomp bits from kwargs to part
    oomp_keys = ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]
    for key in ["classification", "type", "size", "color", "description_main", "description_extra", "manufacturer", "part_number"]:
        part[key] = kwargs.get(f"oomp_{key}", f"")




    #id = thing.get("oobb_id", "default")    
    

    #kwargs["description_main"] = id

    oomp_id = ""
    for key in oomp_keys:
        deet = part.get(key, "")
        deet = deet.replace(".","_")
        if deet != "":
            oomp_id += f"{deet}_"
    oomp_id = oomp_id[:-1]
    part["id"] = oomp_id
    folder = f"parts/{oomp_id}"
    folder_scad_ouput = f"scad_output/{descmain}"
    if descextra != "":
        folder_scad_ouput += f"_{descextra}"

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        

        opsc.opsc_make_object(f'{folder}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)  

        #copy folder to scad_output_folder
        if True:
            print(f"copying {folder} to {folder_scad_ouput}")
            import os
            if not os.path.exists(folder_scad_ouput):
                os.makedirs(folder_scad_ouput)
            if os.name == 'nt':
                #copy a full directory auto overwrite
                command = f'xcopy "{folder}" "{folder_scad_ouput}" /E /I /Y'
                            #print(command)
                os.system(command)
        


    yaml_file = f"{folder}/working.yaml"
    #partial dump
    with open(yaml_file, 'w') as file:
        part_new = copy.deepcopy(part)
        kwargs_new = part_new.get("kwargs", {})
        kwargs_new.pop("save_type","")
        part_new["kwargs"] = kwargs_new
        import os
        cwd = os.getcwd()
        part_new["project_name"] = cwd
        part_new["id_oobb"] = thing["id"]
        #part_new["thing"] = thing
        part_new.pop("thing", "")
        yaml.dump(part_new, file)
    
    #full dump
    yaml_file = f"{folder}/thing.yaml"
    with open(yaml_file, 'w') as file:
        part_new = copy.deepcopy(part)
        kwargs_new = part_new.get("kwargs", {})
        kwargs_new.pop("save_type","")
        part_new["kwargs"] = kwargs_new
        import os
        cwd = os.getcwd()
        part_new["project_name"] = cwd
        part_new["id_oobb"] = thing["id"]
        part_new["thing"] = thing
        yaml.dump(part_new, file)


    print(f"done {oomp_id}")

def generate_navigation(folder="parts", sort=["width", "height", "thickness"]):
    #crawl though all directories in scad_output and load all the working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if 'working.yaml' in files:
            yaml_file = os.path.join(root, 'working.yaml')
            #if working.yaml isn't in the root directory, then do it
            if root != folder:
                with open(yaml_file, 'r') as file:
                    part = yaml.safe_load(file)
                    # Process the loaded YAML content as needed
                    part["folder"] = root
                    part_name = root.replace(f"{folder}","")
                    
                    #remove all slashes
                    part_name = part_name.replace("/","").replace("\\","")
                    parts[part_name] = part

                    print(f"Loaded {yaml_file}")

    pass
    
    for part_id in parts:
        if part_id != "":
            part = parts[part_id]

            if "kwargs" in part:
                kwarg_copy = copy.deepcopy(part["kwargs"])
                folder_navigation = "navigation_oobb"
                folder_source = part["folder"]
                folder_extra = ""
                for s in sort:
                    if s == "name":
                        ex = part.get("name", "default")
                    else:                        
                        ex = kwarg_copy.get(s, "default")
                        #if ex is a list
                        if isinstance(ex, list):
                            ex_string = ""
                            for e in ex:
                                ex_string += f"{e}_"
                            ex = ex_string[:-1]
                            ex = ex.replace(".","d")                            
                    folder_extra += f"{s}_{ex}/"

                #replace "." with d
                folder_extra = folder_extra.replace(".","d")            
                folder_destination = f"{folder_navigation}/{folder_extra}".lower()
                if not os.path.exists(folder_destination):
                    os.makedirs(folder_destination)
                if os.name == 'nt':
                    #copy a full directory auto overwrite
                    command = f'xcopy "{folder_source}" "{folder_destination}" /E /I /Y'
                    print(command)
                    os.system(command)
                else:
                    os.system(f"cp {folder_source} {folder_destination}")

