from setuptools import setup

package_name = 'yurs_network'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='donutu',
    maintainer_email='p.radhey06@gmail.com',
    description='YURS network standardized task',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publisher = yurs_network.my_first_node:main",
            "subscriber1 = yurs_network.my_second_node:main",
            "subscriber2 = yurs_network.my_third_node:main",
        ],
    },
)
