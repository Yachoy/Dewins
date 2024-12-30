import os
import pathlib
import typing
from abc import *
from typing import *
from pathlib import Path

class File:
    path: pathlib.Path
    _local_save_content: Any
    _ctx: Optional[ContextManager]

    def __init__(self, path: typing.Union[str, pathlib.Path], ctx: Optional["ContManager"] = None, default_context: str = ""):
        if isinstance(path, str):
            self.path = Path(path)
        else:
            self.path = path
        self._local_save_content = default_context
        self._ctx = ctx

    @property
    def extension(self) -> str:
        tmp = self.path.suffix
        tmp = tmp.replace(tmp[0], "", 1)
        return tmp

    def getname(self):
        return self.path

    @property
    def name(self) -> str:
        return self.path.stem

    @property
    def is_created(self) -> bool:
        return self.path.exists()

    def write(self, data: str, mode: str = 'w+') -> None:
        with open(self.path, mode) as file:
            file.write(data)

    def read(self) -> Optional[str]:
        if self.extension not in ['txt', 'html', 'json', 'csv', "xlsx", "xlsm", "xls", "xltx", "xltm"]:
            return None
        answer: str = str()
        with open(self.path, "r") as file:
            tmp_answer = file.readlines()
            for i in tmp_answer:
                answer += i
        return answer

    @abstractmethod
    def load_content(self) -> None: pass
    @abstractmethod
    def get_content(self) -> typing.Any: pass

    def make_like_me(self, _obj: "File"):
        print(self.extension)
        if self.extension not in ['txt', 'html', 'json', 'csv', "xlsx", "xlsm", "xls", "xltx", "xltm"]:
            return None
        answer: str = str()
        with open(str(_obj.getname()), "r+") as f:
            tmp_answer = f.readline()
            for i in tmp_answer:
                answer += i
        with open(self.path, "w") as file:
            file.write(answer)
        return answer


class ImageFile(File):

    def __init__(self):
        var = None


class TextFile(File):

    def __init__(self):
        var = None


class Folder:
    path: pathlib.Path
    _files: List[File]

    def __init__(self, pth: pathlib.Path, files: List[File] = None):
        self.path = pth
        self._files = files if files is not None else []

    @property
    def name(self) -> str:
        return self.path.stem

    @property
    def is_created(self) -> bool:
        return self.path.exists()

    def add_file_by_class(self, file: File):
        self._files.append(file)

    def add_file_by_path(self, path_file: str):
        self._files.append(File(path_file))

    def remove_file_by_class(self, file: File):
        self._files.remove(file)

    def remove_file_by_path(self, path_file: str):
        self._files.remove(File(path_file))

    def realise(self):
        if not self.is_created:
            os.mkdir(pathlib.Path(self.path))
        for i in self._files:
            if not i.path.exists():
                i.path.mkdir()

    def get_files(self) -> List[File]:
        return self._files

    def find_file_by_path(self, path_file: str) -> Optional[File]:
        for i in self._files:
            if path_file == i.path:
                return i
        return None

    def find_file_by_class(self, file: File) -> Optional[File]:
        for i in self._files:
            if file == i:
                return i
        return None


class ContManager:
    _paths: Dict[Folder, Union[Dict[Folder, ...], File]]

    def __init__(self, paths: Dict[Folder, Union[Dict[Folder, ...], File]]):
        self._paths = paths

    def get_files(self) -> List[File]:
        fin_list: List[File] = list()
        for i in self._paths:
            if isinstance(i, File):
                fin_list.append(i)
        return fin_list

    @staticmethod
    def create(f: Union[File, Folder]):
        if not f.path.exists():
            folders: list[str] = str(f.path).split('\\')
            path: str = folders[0]
            try:
                for i in folders:
                    if i != path:
                        path += '/' + i
                    if not pathlib.Path(path).exists():
                        os.mkdir(path)
            except:
                print('Это не работает, я не знаю почему, иди исправляй!')

    def realise(self):
        for i in self._paths:
            if not i.is_created:
                self.create(i)

    def find_by_name(self, name: str) -> Any:
        answer = list()
        for i in self._paths:
            if str(i) == name:
                answer.append(i)
        return answer

    def find_by_path(self, path_file: str) -> Optional[Union[File, Folder]]:
        for i in self._paths:
            if str(i) == path_file:
                return i
        return None

if __name__ == "__main__":
    ### Testing ###

    ### Generation ###
    file_manager = ContManager({
        Folder(Path("TestingFileManager")): {
            File("Example1.txt"):"Default content of file1",
            File("Example2.txt"):"Default content of file2",
            Folder(Path("UnderFolder")):{
                File("under_file.json"):"{}",
                File("Example1.txt"): "Hello world from under example 1"
            }
        }
    })
    file_manager.realise()
    ### Search ###
    assert len(file_manager.find_by_name("Example1.txt")) == 2
    assert (tmp:=file_manager.find_by_path("TestingFileManager/")) is not None and isinstance(tmp, Folder)
    assert (tmp := file_manager.find_by_path("under_file.json")) is not None and isinstance(tmp, File)
    ###

    assert len(file_manager.get_files()) == 4
    f = File("./log.txt")
    assert f.is_created == False
    # f.realise() ???
