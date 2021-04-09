#  #!/usr/bin/env python
#  encoding: utf-8

# --------------------------------------------------------------------------------------------------------------------
#
# Name: uname.py
# Version: 0.0.1
#
# Summary: Identifying and fetching all system and hardware information.
#
# Author: Alexsander Lopes Camargos
# Author-email: alcamargos@vivaldi.net
#
# License: MIT
#
# --------------------------------------------------------------------------------------------------------------------

"""Identifying and fetching all system and hardware information such as os details, CPU and GPU information,
disk and network usage in Python using platform, psutil and gputil libraries."""


import platform
from datetime import datetime

# Cross-platform library for process and system monitoring.
import psutil


def size_readable_human(size, suffix='B'):
    """Size the bytes into the appropriate format for reading by humans.

    Ex:
        342.246.182 bytes => 326 MB
        37.675.796.098 bytes => 35,0 GB"""

    factor = 1024

    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if size < factor:
            return f'{size: .2f}{unit} {suffix}'

        size /= factor


def python_information():
    """The current version of python language identifying."""

    # The Python version.
    print(f'Python Version: {platform.python_version()}')
    # The Python implementation
    print(f'Python Implementation: {platform.python_implementation()}')
    # The compiler used for compiling Python.
    print(f'Python Compiler: {platform.python_compiler()}')
    # The Python build number and date as strings.
    print(f'Python Build Number: {platform.python_build()}')
    # The libc version that the file executable.
    print(f'Python Lib C Version: {platform.libc_ver()}')
    print(f'Python Architecture: {platform.architecture()}')
    print(f'Python Platform: {platform.platform()}')


def boot_time():
    """Identifying the current system boot time."""

    system_boot_time_timestamp = psutil.boot_time()

    # Construct the system boot date and time
    system_boot_time = datetime.fromtimestamp(system_boot_time_timestamp)

    print(f"Boot Time: {system_boot_time.day}/{system_boot_time.month}/{system_boot_time.year} "
          f"{system_boot_time.hour}:{system_boot_time.minute}:{system_boot_time.second}")


def cpu_information(frequency=True, usage=True, enumerate_cores=True):
    """Identifying the CPU information.

    psutil.cpu_count() - returns number of cores.
    psutil.cpu_freq() - returns CPU frequency expressed in Mhz (current, min and max frequency).
    psutil.cpu_percent() - returns a float representing the current CPU utilization as a percentage."""

    # Number of cores:
    # The number of physical cores only.
    print(f'Physical cores: {psutil.cpu_count(logical=False)}')
    # The number of physical and logical cores.
    print(f'Total cores: {psutil.cpu_count(logical=True)}')

    # CPU frequency:
    if frequency:
        cpu_frequency = psutil.cpu_freq()
        print(f'Maximum Frequency: {cpu_frequency.max :.2f}Mhz')
        print(f'Minimum Frequency: {cpu_frequency.min :.2f}Mhz')
        print(f'Current Frequency: {cpu_frequency.current :.2f}Mhz')

    # CPU usage:
    if usage:
        # Fetching the use of each core.
        if enumerate_cores:
            for core, usage_percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
                print(f'Core {core}: {usage_percentage}%')

        print(f'Total CPU Usage: {psutil.cpu_percent()}%')


def memory_information(system_memory_information=True, swap_memory_information=True):
    """System and swap memory information.

    psutil.virtual_memory() - returns stats about system memory usage.
    psutil.swap_memory() - returns stats about swap memory usage."""

    # Get the memory details:
    if system_memory_information:
        system_memory_information = psutil.virtual_memory()
        print(f'Total Memory: {size_readable_human(system_memory_information.total)}')
        print(f'Available Memory: {size_readable_human(system_memory_information.available)}')
        print(f'Used Memory: {size_readable_human(system_memory_information.used)}')
        print(f'Percentage Memory: {system_memory_information.percent}%')

    # Get the swap memory details (if exists):
    if swap_memory_information:
        swap_memory_information = psutil.swap_memory()
        if swap_memory_information:
            print(f'Total Swap Memory: {size_readable_human(swap_memory_information.total)}')
            print(f'Free Swap Memory: {size_readable_human(swap_memory_information.free)}')
            print(f'Used Swap Memory: {size_readable_human(swap_memory_information.used)}')
            print(f'Percentage Swap Memory: {swap_memory_information.percent}%')


def disk_usage_information():
    """Disk usage statistics information."""

    # Get all disk partitions:
    partitions = psutil.disk_partitions()

    for partition in partitions:
        print(f'Device: {partition.device}')
        print(f'\tMount Point: {partition.mountpoint}')
        print(f'\tFile System Type: {partition.fstype}')

        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f'\tTotal Size: {size_readable_human(partition_usage.total)}')
            print(f'\tUsed: {size_readable_human(partition_usage.used)}')
            print(f'\tFree: {size_readable_human(partition_usage.free)}')
            print(f'\tPercentage: {partition_usage.percent :.2f}%')
        except PermissionError:
            # This can be catched due to the disk that isn't ready.
            continue

    # Get I/O statistics since boot:
    disk_io_stats = psutil.disk_io_counters()
    print(f'Total read: {size_readable_human(disk_io_stats.read_bytes)}')
    print(f'Total write: {size_readable_human(disk_io_stats.write_bytes)}')


def network_information():
    """Network interfaces information."""

    # Get all network information (virtual and physical):
    network_interface = psutil.net_if_addrs()

    for interface_name, interface_address in network_interface.items():
        for address in interface_address:
            print(f'Interface: {interface_name}')
            print(f"\tAddress Family: {str(address.family).split('.')[1]}")
            print(f'\tAddress: {address.address}')
            print(f'\tNetmask: {address.netmask}')
            print(f'\tBroadcast IP: {address.broadcast}')

    # Get I/O statistics since bot:
    net_io_stats = psutil.net_io_counters()
    print(f'Total Bytes Sent: {size_readable_human(net_io_stats.bytes_sent)}')
    print(f'Total Bytes Received: {size_readable_human(net_io_stats.bytes_recv)}')


def operating_system_information():
    """The current operating system identifying.

    platform.uname() Returns a tuple of strings (system, node, release, version, machine, processor)
        sysname - operating system name
        nodename - name of machine on network (implementation-defined)
        release - operating system release
        version - operating system version
        machine - hardware identifier"""

    uname_information = platform.uname()

    print(f"Operating system: {uname_information.system}")
    print(f"Hostname: {uname_information.node}")
    print(f"Release: {uname_information.release}")
    print(f"Version: {uname_information.version}")
    print(f"Machine: {uname_information.machine}")
    print(f"Processor: {uname_information.processor}")


def uname(all_information=True, op=False, bt=False, py=False, cpu=False, men=False, disk=False, net=False):
    """Display system information."""

    if all_information:
        op = True
        bt = True
        py = True
        cpu = True
        men = True
        disk = True
        net = True

    if op:
        print('System Information')
        operating_system_information()

    if bt:
        print('Boot Time')
        boot_time()

    if py:
        print('Python Information')
        python_information()

    if cpu:
        print("CPU Information")
        cpu_information()

    if men:
        print("Memory Information")
        memory_information()

    if disk:
        print("Disk Information")
        disk_usage_information()

    if net:
        print("Network Information")
        network_information()


if __name__ == "__main__":
    uname(all_information=True)
