from .inspector import AbstractInspector
import logging
import os
import psutil

class CPUInspector(AbstractInspector):

    def __init__(self):
        super().__init__("CPUInspector")

    def inspect(self) -> dict:
        """ Extract informations about CPU and running processes"""
        logging.info("Looking for CPU Stats")
        _retval = dict()
        _retval['CpuCount'] = os.cpu_count()
        _retval['Tasks'] = self.__processes()
        return _retval

    def __get_task_info(self, _pid: int, _ppids_map: dict, _tracked_list: list) -> dict:
        _task_info = dict()
        _task = psutil.Process(_pid)
        _task_info['Name'] = _task.name()
        _task_info['PID'] = _pid
        _task_info['PPID'] = _ppids_map[_pid]
        _task_info['Status'] = _task.status()
        _task_info['MemoryPercent'] = round(_task.memory_percent(), 2)
        _task_info['Tasks'] = list()
        for _p in _ppids_map.items():
            if _p[1] == _pid:  # If I am parent of someone else append to me somene else informations
                _task_info['Tasks'].append(self.__get_task_info(_p[0], _ppids_map, _tracked_list))
                _tracked_list.append(_p[0])

        return _task_info

    def __processes(self) -> list:
        _tasks = list()
        _tracked_list = list()
        _pids_list = psutil.pids()
        _ppids_map = psutil._ppid_map()
        for _pid in _pids_list:
            if _pid not in _tracked_list:
                _tasks.append(self.__get_task_info(_pid, _ppids_map, _tracked_list))
        return _tasks
