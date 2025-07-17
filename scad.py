import copy
import opsc
import oobb
import oobb_base
import yaml
import os
import scad_help

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    typ = kwargs.get("typ", "")

    if typ == "":
        #setup    
        #typ = "all"
        typ = "fast"
        #typ = "manual"

    oomp_mode = "project"
    #oomp_mode = "oobb"

    test = False
    #test = True

    if typ == "all":
        filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
        #default
        #filter = ""; save_type = "all"; navigation = True; overwrite = True; modes = ["3dpr"]; oomp_run = True; test = False
    elif typ == "fast":
        filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
        #default
        #filter = ""; save_type = "none"; navigation = False; overwrite = True; modes = ["3dpr"]; oomp_run = False
    elif typ == "manual":
    #filter
        filter = ""
        #filter = "test"

    #save_type
        save_type = "none"
        #save_type = "all"
        
    #navigation        
        #navigation = False
        navigation = True    

    #overwrite
        overwrite = True
                
    #modes
        #modes = ["3dpr", "laser", "true"]
        modes = ["3dpr"]
        #modes = ["laser"]    

    #oomp_run
        oomp_run = True
        #oomp_run = False    

    #adding to kwargs
    kwargs["filter"] = filter
    kwargs["save_type"] = save_type
    kwargs["navigation"] = navigation
    kwargs["overwrite"] = overwrite
    kwargs["modes"] = modes
    kwargs["oomp_mode"] = oomp_mode
    kwargs["oomp_run"] = oomp_run
    
       
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        directory_name = os.path.dirname(__file__) 
        directory_name = directory_name.replace("/", "\\")
        project_name = directory_name.split("\\")[-1]
        #max 60 characters
        length_max = 40
        if len(project_name) > length_max:
            project_name = project_name[:length_max]
            #if ends with a _ remove it 
            if project_name[-1] == "_":
                project_name = project_name[:-1]
                
        #defaults
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        #oomp_bits
        if oomp_mode == "project":
            kwargs["oomp_classification"] = "project"
            kwargs["oomp_type"] = "github"
            kwargs["oomp_size"] = "oomlout"
            kwargs["oomp_color"] = project_name
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""
        elif oomp_mode == "oobb":
            kwargs["oomp_classification"] = "oobb"
            kwargs["oomp_type"] = "part"
            kwargs["oomp_size"] = ""
            kwargs["oomp_color"] = ""
            kwargs["oomp_description_main"] = ""
            kwargs["oomp_description_extra"] = ""
            kwargs["oomp_manufacturer"] = ""
            kwargs["oomp_part_number"] = ""

        part_default = {} 
       
        part_default["project_name"] = project_name
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        

        funnels = get_funnels_verbose()

        for funnel in funnels:

            part = copy.deepcopy(part_default)
            p3 = copy.deepcopy(kwargs)
            p3["width"] = 0
            p3["height"] = 0
            p3.update(funnel)
            #p3["thickness"] = 6
            ex = ""
            if "funnel_extra" in funnel:
                ex = f"{funnel["funnel_extra"]}_funnel_extra"
            if "funnel_flare" in funnel:
                ex = f"{ex}{funnel['funnel_flare']}_flare"
            if "funnel_bottom_radius" in funnel:
                ex = f"{ex}_{funnel['funnel_bottom_radius']}_b_rad"
            if "funnel_height" in funnel:
                ex = f"{ex}_{funnel['funnel_height']}_h"
            if "funnel_wall_thickness" in funnel:
                ex = f"{ex}_{funnel['funnel_wall_thickness']}_wt"
            if "funnel_height_bottom_tube" in funnel:
                ex = f"{ex}_{funnel['funnel_height_bottom_tube']}_hbt"
            p3["extra"] = ex
            part["kwargs"] = p3
            nam = p3.get("funnel_type","funnel_circle")
            part["name"] = nam
            
            if oomp_mode == "oobb":
                p3["oomp_size"] = nam
            if not test:
                pass
                parts.append(part)


    kwargs["parts"] = parts

    scad_help.make_parts(**kwargs)

    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("name")
        sort.append("funnel_bottom_radius")
        sort.append("funnel_flare")
        sort.append("funnel_height")
        sort.append("funnel_height_bottom_tube")
        
        scad_help.generate_navigation(sort = sort)


def get_funnels_verbose():
    # funnel sizes
    funnels = []


     #coffee
    funnel = {}
    funnel["funnel_bottom_radius"] = 70/2
    funnel["funnel_flare"] = 60/2
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 15
    funnel["funnel_wall_thickness"] = 3
    funnel["funnel_extra"] = "food_coffee_ground_funnel"
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one

     #toner cartridge to smaller bottle
    funnel = {}
    funnel["funnel_bottom_radius"] = 90/2
    funnel["funnel_flare"] = 80/2
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 20
    funnel["funnel_wall_thickness"] = 3
    funnel["funnel_extra"] = "packaging_takeaway_container_circle_670_ml_105_mm_diameter_135_mm_depth_tamper_evident_systempak_254"
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one

    funnel = {}
    funnel["funnel_bottom_radius"] = 30/2
    funnel["funnel_flare"] = 40
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 10
    funnel["funnel_wall_thickness"] = 1
      
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one
    
    funnel = {}
    funnel["funnel_bottom_radius"] = 30/2
    funnel["funnel_flare"] = 40
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 10
    funnel["funnel_wall_thickness"] = 1       
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one

    
    #for emptying toner catridges
    funnel = {}
    funnel["funnel_bottom_radius"] = 50/2
    funnel["funnel_flare"] = 175/2
    funnel["funnel_height"] = 75
    funnel["funnel_height_bottom_tube"] = 20
    funnel["funnel_wall_thickness"] = 2
    funnel["funnel_extra"] = "toner_cartridge_funnel"
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one

    
    funnel = {}
    funnel["funnel_bottom_radius"] = 75/2
    funnel["funnel_flare"] = 145/2
    funnel["funnel_height"] = 75
    funnel["funnel_height_bottom_tube"] = 20
    funnel["funnel_wall_thickness"] = 2
    funnel["funnel_extra"] = "toner_cartridge_jar_fill_funnel"
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one

    #toner cartridge to smaller bottle
    funnel = {}
    funnel["funnel_bottom_radius"] = 15/2
    funnel["funnel_flare"] = 40/2
    funnel["funnel_height"] = 20
    funnel["funnel_height_bottom_tube"] = 15
    funnel["funnel_wall_thickness"] = 2
    funnel["funnel_extra"] = "toner_cartridge_funnel_small_bottle"
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one
    
    #printer_inkjet_nozzle_unclog_fluid
    funnel = {}
    funnel["funnel_bottom_radius"] = 11/2
    funnel["funnel_flare"] = 30/2
    funnel["funnel_height"] = 20
    funnel["funnel_height_bottom_tube"] = 20
    funnel["funnel_wall_thickness"] = 2
    funnel["funnel_extra"] = "printer_inkjet_nozzle_unclog_fluid"
    funnels.append(copy.deepcopy(funnel))  # add a copy for the next one

    funnel = {}
    funnel["funnel_bottom_radius"] = 30/2
    funnel["funnel_flare"] = 70
    funnel["funnel_height"] = 50
    funnel["funnel_height_bottom_tube"] = 20
    funnel["funnel_wall_thickness"] = 1
    funnels.append(funnel)
    #load those values 

    funnel = {}
    funnel["funnel_bottom_radius"] = 45/2
    funnel["funnel_flare"] = 55
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 45
    funnel["funnel_wall_thickness"] = 1
    funnels.append(funnel)
    #load those values 

    #rounded rectangle ones

    funnel = {}
    funnel["funnel_bottom_width"] = 125   
    funnel["funnel_bottom_length"] = 75 
    funnel["funnel_flare"] = 100
    funnel["funnel_height"] = 50
    funnel["funnel_height_bottom_tube"] = 70
    funnel["funnel_wall_thickness"] = 0.3
    funnel["funnel_type"] = "funnel_rounded_rectangle"  
    funnels.append(funnel)
    #load those values 

    #for emptying toner catridges
    funnel = {}
    funnel["funnel_bottom_width"] = 125   
    funnel["funnel_bottom_length"] = 75 
    funnel["funnel_flare"] = 100
    funnel["funnel_height"] = 50
    funnel["funnel_height_bottom_tube"] = 70
    funnel["funnel_wall_thickness"] = 1.5
    funnel["funnel_type"] = "funnel_rounded_rectangle"  
    funnels.append(funnel)

    #cereal
    funnel = {}
    funnel["funnel_bottom_width"] = 100   
    funnel["funnel_bottom_length"] = 55 
    funnel["funnel_flare"] = 130
    funnel["funnel_height"] = 50
    funnel["funnel_height_bottom_tube"] = 30
    funnel["funnel_wall_thickness"] = 0.3
    funnel["funnel_type"] = "funnel_rounded_rectangle"
    funnel["funnel_extra"] = "cereal_funnel"
    funnels.append(funnel)
    #load those values 

    #oobb sized ones
    funnels_oobb = []
    funnels_oobb.append([3,3])
    funnels_oobb.append([2,2.5])
    funnels_oobb.append([4,2.5])
    funnels_oobb.append([3,2.5])
    funnels_oobb.append([5,2.5])



    for funnel_oobb in funnels_oobb:
        funnel = {}
        funnel["funnel_bottom_width"] = funnel_oobb[0] * 15 - 5   
        funnel["funnel_bottom_length"] = funnel_oobb[1] * 15 - 5
        funnel["funnel_flare"] = 60
        funnel["funnel_height"] = 25
        funnel["funnel_height_bottom_tube"] = 25
        funnel["funnel_wall_thickness"] = 1
        funnel["funnel_type"] = "funnel_rounded_rectangle"    
        funnel["funnel_extra"] = f"oobb_funnel_{funnel_oobb[0]}_width_{funnel_oobb[1]}_height"
        funnels.append(funnel)
    
    return funnels

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    
    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "positive"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -500/2
        pos1[1] += 0
        pos1[2] += -500/2        
        p3["pos"] = pos1
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_funnel_circle(thing, **kwargs):
    # default sets
        funnel = kwargs
        width = kwargs.get("width", 3)
        height = kwargs.get("height", 5)
        thickness = kwargs.get("thickness", 3)
        size = kwargs.get("size", "oobb")
        pos = kwargs.get("pos", [0, 0, 0])
        extra = funnel.get("funnel_extra", "")
        # extra sets
        holes = kwargs.get("holes", True)
        both_holes = kwargs.get("both_holes", True)    
        kwargs["pos"] = pos
        
        
            

        funnel_bottom_radius = funnel["funnel_bottom_radius"]        
        funnel_flare = funnel["funnel_flare"]
        funnel_top_radius = funnel_bottom_radius + funnel_flare
        funnel_height = funnel["funnel_height"]
        funnel_height_bottom_tube = funnel["funnel_height_bottom_tube"]
        funnel_wall_thickness = funnel["funnel_wall_thickness"]
        funnel_extra = f"circle_{funnel_top_radius}_mm_top_{funnel['funnel_bottom_radius']*2}_mm_bottom_{funnel['funnel_height']}_mm_height_{funnel['funnel_height_bottom_tube']}_mm_bottom_tube_{funnel['funnel_wall_thickness']}_mm_wall"  
        if extra == "":
            funnel_extra = f"rounded_rectangle_{funnel_top_radius * 2}_mm_top_{funnel_bottom_radius*2}_mm_bottom_{funnel_height}_mm_length_{funnel['funnel_height']}_mm_height_{funnel['funnel_height_bottom_tube']}_mm_bottom_tube_{funnel['funnel_wall_thickness']}_mm_wall"
        else:
            funnel_extra = extra

        extra = funnel_extra
        kwargs["extra"] = funnel_extra

        # get the default thing
        #thing = oobb_base.get_default_thing(**kwargs)
        th = thing["components"]
        #kwargs.pop("size","")

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"   
        p3["shape"] = f"oobb_cylinder_hollow"
        p3["r1"] = funnel_top_radius
        p3["r2"] = funnel_bottom_radius
        p3["wall_thickness"] = funnel_wall_thickness
        p3["h"] = funnel_height
        p3["pos"] = pos
        #p3["m"] = ""  
        p3.pop("size","")
        oobb_base.append_full(thing,**p3)      
        #th.append(oobb_base.oobb_easy(**p3))
        
        # add bottom tube
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder_hollow"
        p3["r"] = funnel_bottom_radius
        p3["wall_thickness"] = funnel_wall_thickness
        p3["h"] = funnel_height_bottom_tube
        pos1 = copy.deepcopy(pos)
        pos1[2] = pos1[2] + funnel_height
        p3["pos"] = pos1 
        #p3["m"] = ""
        p3.pop("size","")
        oobb_base.append_full(thing,**p3)



        
def get_funnel_rounded_rectangle(thing, **kwargs):
    # default sets
        funnel = kwargs
        width = kwargs.get("width", 3)
        height = kwargs.get("height", 5)
        thickness = kwargs.get("thickness", 3)
        size = kwargs.get("size", "oobb")
        pos = kwargs.get("pos", [0, 0, 0])
        extra = funnel.get("funnel_extra", "")
        # extra sets
        holes = kwargs.get("holes", True)
        both_holes = kwargs.get("both_holes", True)    
        kwargs["pos"] = pos
        funnel = kwargs
        
            


        funnel_bottom_width = funnel["funnel_bottom_width"]
        funnel_bottom_length = funnel["funnel_bottom_length"]
        funnel_flare = funnel["funnel_flare"]
        funnel_top_width = funnel_bottom_width + funnel_flare
        funnel_top_length = funnel_bottom_length + funnel_flare


        funnel_height = funnel["funnel_height"]
        funnel_height_bottom_tube = funnel["funnel_height_bottom_tube"]
        funnel_wall_thickness = funnel["funnel_wall_thickness"]
        if extra == "":
            funnel_extra = f"rounded_rectangle_{funnel_top_width}_mm_top_{funnel_bottom_width}_mm_bottom_{funnel_top_length}_mm_length_{funnel['funnel_height']}_mm_height_{funnel['funnel_height_bottom_tube']}_mm_bottom_tube_{funnel['funnel_wall_thickness']}_mm_wall"
        else:
            funnel_extra = extra
        kwargs["extra"] = funnel_extra

        # get the default thing
        #thing = oobb_base.get_default_thing(**kwargs)
        th = thing["components"]
        #kwargs.pop("size","")

        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"   
        p3["shape"] = f"oobb_rounded_rectangle_hollow"
        difference = funnel_top_width - funnel_bottom_width
        w = funnel_top_width - difference
        h = funnel_top_length- difference
        d = funnel_height
        size = [w,h,d]
        p3["size"] = size
        p3["r2"] = 5
        p3["r1"] = difference/2
        p3["wall_thickness"] = funnel_wall_thickness
        p3["pos"] = pos
        oobb_base.append_full(thing,**p3)      
        #th.append(oobb_base.oobb_easy(**p3))
        
        # add bottom tube
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_rounded_rectangle_hollow"
        w = funnel_bottom_width
        h = funnel_bottom_length
        d = funnel_height_bottom_tube
        size = [w,h,d]
        p3["size"] = size
        p3["wall_thickness"] = funnel_wall_thickness
        
        pos1 = copy.deepcopy(pos)
        pos1[2] = pos1[2] + funnel_height
        p3["pos"] = pos1 
        oobb_base.append_full(thing,**p3)




if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)