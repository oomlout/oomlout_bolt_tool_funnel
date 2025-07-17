import os

def main(**kwargs):
    pass
    files_to_delete = []
    #configuration
    #files_to_delete.append('configuration\\filter.yaml')
    files_to_delete.append('configuration\\filter_default.yaml')    
    files_to_delete.append('configuration\\generate_release.yaml')
    files_to_delete.append('configuration\\oomlout_oomp_utility_label_generation_configuration.yaml')
    files_to_delete.append('configuration\\oomlout_oomp_utility_oomlout_generate_report_configuration.yaml')
    #files_to_delete.append('configuration\\repos_source.yaml')
    files_to_delete.append('configuration\\repos_source_default.yaml')
    #files_to_delete.append('configuration\\utility_source.yaml')
    files_to_delete.append('configuration\\utility_source_default.yaml')

    files_to_delete.append('a_clean_for_base_oomp.py')
    #files_to_delete.append('action_build_oomp.py')
    files_to_delete.append('action_build_release.py')
    #files_to_delete.append('action_clean_up_generation.py')
    #files_to_delete.append('action_generate_all_no_click.py')
    files_to_delete.append('Backup_of_working.cdr')
    files_to_delete.append('generate_all.bat')
    files_to_delete.append('generate_all_missing.bat')
    files_to_delete.append('generate_docs.bat')
    files_to_delete.append('generate_oolc.bat')
    files_to_delete.append('generate_resolution.bat')
    #files_to_delete.append('scad.py')
    #files_to_delete.append('scad_help.py')
    #files_to_delete.append('working.cdr')
    #'files_to_delete.append('working.py')
    files_to_delete.append('working.scad')
    files_to_delete.append('working_xlsx.xlsx')
    files_to_delete.append('a_oomp_open_hardware_source_clean.py')
    files_to_delete.append('a_oomp_open_hardware_source_create.py')

    
    print('Deleting files')
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
        else:
            print('File does not exist: ' + file)

    folders_to_delete = []
    folders_to_delete.append('kicad')
    folders_to_delete.append('oolc_production')
    folders_to_delete.append('source_files')
    folders_to_delete.append('three_d_printing')
    folders_to_delete.append('navigation_oobb')
    folders_to_delete.append('navigation_oomp')
    folders_to_delete.append('parts')
    folders_to_delete.append('scad_output')
    folders_to_delete.append('data')
    folders_to_delete.append('temporary')
    

    #remove all files then remove directory recursively use a system call
    print('Deleting folders')
    for folder in folders_to_delete:
        if os.path.exists(folder):
            os.system('rmdir /S /Q ' + folder)
        else:
            print('Folder does not exist: ' + folder)


    print('Done')


if __name__ == '__main__':
    main()