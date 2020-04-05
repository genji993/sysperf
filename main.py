from modules.inspectors.cpu_inspector import CPUInspector

__author__ = 'Carmelo Riolo (Genji)'
__version__ = '0.1'

if __name__ == '__main__':
    _cpu_inspector = CPUInspector()
    print(_cpu_inspector.inspect())