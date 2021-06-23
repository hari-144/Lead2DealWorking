import os, shutil
from pdf2image import convert_from_path

class FileOperations:
    
    def __init__(self):
        pass
    
    def __file_status__(self, location: str=None):
        if location!=None:
            return os.path.exists(location)
        else:
            return False
        

    def __delete_all__(self,dir_path: str=None):
        status = False
        if self.__file_status__(dir_path):
            cur_dir = os.getcwd()
            os.chdir(dir_path)
            for folder, sub_folder, files in os.walk("."):
                for file in files:
                    try:
                        os.remove(file)
                        # shutil.rmtree(file)
                        # path = os.path.normpath(path)
                        status = True
                    except Exception as ex:
                        print(ex)
        os.chdir(cur_dir)
        return status

    def __get_files__(self, dir_path: str=None, extension: str=None):
        result = {
            "files":[]
        }
        filteration_ = False
        
        if extension==None or extension=="*.*":
            filteration_ = False
        else:
            filteration_ = True

        if dir_path!=None:
            if self.__file_status__(dir_path):
                cur_dir = os.getcwd()
                os.chdir(dir_path)
                for folder, sub_folder, files in os.walk("."):
                    if filteration_ == False:
                        for file in files:
                            result["files"].append({"file_name": file})
                    else:
                        for file in files:
                            if str(file).endswith(extension):
                                result["files"].append({"file_name": file})
                os.chdir(cur_dir)
        return result

class SplitPages(FileOperations):

    def __init__(self):
        pass

    def __convert_page_to_image__(self, file_name: str=None, popplerPath: str=None):
        response = False
        
        file_info = {
            "data": [],
            "page_num": 0
        }

        if self.__file_status__(file_name):
            pdfObj = convert_from_path(file_name,poppler_path=popplerPath)
            pageCounter = 1
            for i in range(len(pdfObj)):
                location = f"static\processed_images\page{str(pageCounter)}.jpg"
                save_location = f"..\\processed_images\\page{str(pageCounter)}.jpg"
                save_location = os.path.normpath(save_location)
                file_info["data"].append({"file_path": save_location, "file_name": "page" + str(pageCounter)})
                pdfObj[i].save(location, 'JPEG')
                pageCounter+=1
        file_info["page_num"] = pageCounter-1
        return response, pageCounter, file_info



