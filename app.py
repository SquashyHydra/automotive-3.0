def main(mov_name, destination):
    from utils.automotive import movieDownloader
    mov = movieDownloader(mov_name, destination)
    mov.start_Proxy()
    mov.build_concat_file()
    mov.cleanup()
    #mov.exe_cleanup() # ONLY FOR EXE COMPALATION DO NOT ENABLE


if __name__ == "__main__":
    from utils.argumentparser import argsparser
    from utils.peaceoflife import gui_supported, get_destination_folder_gui, sanatize_input
    from utils.configuring import load_destination
    from utils.fileandfolder import validate_folder_path

    argsparser()

    mov_name = sanatize_input(input("Movie_Name:"))

    destination = load_destination()

    if destination == None or destination == "" and not validate_folder_path(destination):
        if gui_supported():
            destination = get_destination_folder_gui()
        else:
            destination = load_destination()

    while True:        
        main(mov_name, destination)
        user_input = input("Would you like to rip another movie? (Yes|No) ")
        if user_input.lower() == "no" or user_input.lower() == "n":
            break
        elif user_input.lower() != "yes" or user_input.lower() != "y":
            break
