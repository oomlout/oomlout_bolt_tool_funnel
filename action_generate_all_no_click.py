import copy
import os
import sys
import subprocess

def main(**kwargs):
    #run working    
    if True:
        import working
        working.main(**kwargs)
    
    #run scad
    if True:
        import scad
        kwargs2 = copy.deepcopy(kwargs)
        kwargs2["typ"] = "all"
        scad.main(**kwargs2)
    

    #run build oomp
    if True:
        import action_build_oomp
        kwargs2 = copy.deepcopy(kwargs)
        action_build_oomp.main(**kwargs2)

    #run oolc process
    if True:        
        if not os.path.exists("temporary"):
            os.makedirs("temporary")   
        
        directory_repo = "temporary\\oomlout_oolc_oopen_laser_cutting_production_format"
        #git stuff
        if True:
            #clone into temporary directory
            
            #try clone
            os.system(f"git clone https://github.com/oomlout/oomlout_oolc_oopen_laser_cutting_production_format {directory_repo}")
            #try git pull
            os.system(f"cd {directory_repo} && git pull")

        sys.path.append(os.path.join(os.getcwd(), directory_repo))
        import oolc_process
        kwargs2 = copy.deepcopy(kwargs)
        kwargs2["no_click"] = True
        oolc_process.main(**kwargs)

    #run action_generate_all_no_click
    if True:        
        import action_generate_resolutions_overwrite
        action_generate_resolutions_overwrite.main(**kwargs)
        import action_generate_readme_outputs_overwrite
        action_generate_readme_outputs_overwrite.main(**kwargs)



    #push to git
    if True:
        directory_current = os.getcwd()
        git_command = f'cd {directory_current}&git add *&git commit -m "auto commit"&git push'
        print(f"git_command: {git_command}")
        os.system(git_command) #


        

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)