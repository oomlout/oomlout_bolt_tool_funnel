import oom_kicad
import oom_markdown
import os
import copy

import opsc
import oobb 
import oobb_base
#process
#  locations set in working_parts.ods 
#  export to working_parts.csv
#  put components on the right side of the board
#  run this script

def main(**kwargs):
    #place_parts(**kwargs)
    #make_readme(**kwargs)
    make_scad(**kwargs)
    
    

def make_readme(**kwargs):
    os.system("generate_resolution.bat")
    oom_markdown.generate_readme_project(**kwargs)
    #oom_markdown.generate_readme_teardown(**kwargs)
    
def make_scad(**kwargs):

    #kwargs["save_type"] = "none"    
    kwargs["save_type"] = "all"

    #kwargs["save_type"] = "3dpr"
    
    #kwargs["modes"] = ["3dpr","laser","true"]
    kwargs["modes"] = ["3dpr"]
    
    kwargs["size"] = "oobb"
    kwargs["type"] = "oomlout_bolt_tool_funnel"
    kwargs["width"] = 1
    kwargs["height"] = 1
    kwargs["thickness"] = 1

   
    # funnel sizes
    funnels = []

    funnel = {}
    funnel["funnel_bottom_radius"] = 30/2
    funnel["funnel_flare"] = 40
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 10
    funnel["funnel_wall_thickness"] = 1
      
    funnels.append(funnel)
    
    funnel = {}
    funnel["funnel_bottom_radius"] = 30/2
    funnel["funnel_flare"] = 40
    funnel["funnel_height"] = 30
    funnel["funnel_height_bottom_tube"] = 10
    funnel["funnel_wall_thickness"] = 1       
    funnels.append(funnel)

    
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
    funnel["funnel_type"] = "rounded_rectangle"  
    funnels.append(funnel)
    #load those values 

    #cereal
    funnel = {}
    funnel["funnel_bottom_width"] = 100   
    funnel["funnel_bottom_length"] = 55 
    funnel["funnel_flare"] = 150
    funnel["funnel_height"] = 50
    funnel["funnel_height_bottom_tube"] = 70
    funnel["funnel_wall_thickness"] = 0.3
    funnel["funnel_type"] = "rounded_rectangle"
    funnel["funnel_extra"] = "cereal_funnel"
    funnels.append(funnel)
    #load those values 

    #oobb sized ones
    funnels_oobb = []
    funnels_oobb.append([3,3])
    funnels_oobb.append([2,2.5])
    funnels_oobb.append([4,2.5])



    for funnel_oobb in funnels_oobb:
        funnel = {}
        funnel["funnel_bottom_width"] = funnel_oobb[0] * 15 - 5   
        funnel["funnel_bottom_length"] = funnel_oobb[1] * 15 - 5
        funnel["funnel_flare"] = 60
        funnel["funnel_height"] = 25
        funnel["funnel_height_bottom_tube"] = 25
        funnel["funnel_wall_thickness"] = 1
        funnel["funnel_type"] = "rounded_rectangle"    
        funnel["funnel_extra"] = f"oobb_funnel_{funnel_oobb[0]}_width_{funnel_oobb[1]}_height"
        funnels.append(funnel)


    for funnel in funnels:
        funnel_type = funnel.get("funnel_type", "circle")

        if funnel_type == "circle":
            get_funnel_circle(funnel, **kwargs)

        if funnel_type == "rounded_rectangle":
            pass
            get_funnel_rounded_rectangle(funnel, **kwargs)

def get_funnel_circle(funnel, **kwargs):
    # default sets
        width = kwargs.get("width", 3)
        height = kwargs.get("height", 5)
        thickness = kwargs.get("thickness", 3)
        size = kwargs.get("size", "oobb")
        pos = kwargs.get("pos", [0, 0, 0])
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
        kwargs["extra"] = funnel_extra

        # get the default thing
        thing = oobb_base.get_default_thing(**kwargs)
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



        ######  save stuff    
            
        save_type = kwargs.get("save_type", "all")
        overwrite = True
        modes = kwargs.get("modes", ["3dpr","laser","true"])
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
            opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)
        
def get_funnel_rounded_rectangle(funnel, **kwargs):
    # default sets
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
        thing = oobb_base.get_default_thing(**kwargs)
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



        ######  save stuff    
            
        save_type = kwargs.get("save_type", "all")
        overwrite = True
        modes = kwargs.get("modes", ["3dpr","laser","true"])
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
            opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)
        
 


#take component positions from working_parts.csv and place them in working.kicad_pcb
def place_parts(**kwargs):
    board_file = "kicad/current_version/working/working.kicad_pcb"
    parts_file = "working_parts.csv"
    #load csv file
    import csv
    with open(parts_file, 'r') as f:
        reader = csv.DictReader(f)
        parts = [row for row in reader]


    
    oom_kicad.kicad_set_components(board_file=board_file, parts=parts, corel_pos=True, **kwargs)






if __name__ == '__main__':
    main()