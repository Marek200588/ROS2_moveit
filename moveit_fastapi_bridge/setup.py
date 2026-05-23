from setuptools import setup
import os
from glob import glob

package_name = "moveit_fastapi_bridge"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Najpierw podajemy gdzie kopiujemy, potem z użyciem glob co kopiujemy
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py')))
    ],
    
    install_requires=['setuptools'],
    zip_safe=True,
    author="Marek Kulma",
    author_email="marek@todo.todo",
    maintainer="Marek Kulma",
    description="demo fastAPI bo mi zależy na tej pracy :)",
    license="TODO: License declaration",
    
    entry_points={
        'console_scripts': [
            # Komenda api_server odpali plik main.py i znajdującą się w nim funkcję main()
            "api_server = moveit_fastapi_bridge.main:main"
        ],
    }
)