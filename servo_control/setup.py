from setuptools import find_packages, setup

package_name = 'servo_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cengsiang',
    maintainer_email='cengsiang@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "kaki1_node = servo_control.kaki1_node:main",
            "kaki2_node = servo_control.kaki2_node:main",
            "kaki3_node = servo_control.kaki3_node:main",
            "kaki4_node = servo_control.kaki4_node:main",
            "walk_node = servo_control.walk_node:main",
            "berdiri_node = servo_control.berdiri_node:main",
            "us_node = servo_control.us_node:main"            
        ],
    },
)
