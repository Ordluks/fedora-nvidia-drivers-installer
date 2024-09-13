import logger
from system_utils import install_packages_list, run_shell
from grub_file_parser import GrubFile, GRUB_FILE_PATH

KERNEL_OPTS_PROPERTY_NAME = 'GRUB_CMDLINE_LINUX'

def install_nvidia_driver():
  logger.info('Installing NVidia driver...')

  # grub_file = GrubFile()
  # kernel_options = grub_file[KERNEL_OPTS_PROPERTY_NAME]

  install_packages_list(['akmod-nvidia', 'xorg-x11-drv-nvidia-cuda', 'libva', 'libva-nvidia-driver'])

  # new_kernel_options = grub_file[KERNEL_OPTS_PROPERTY_NAME] = 'nvidia-drm.modeset=1 ' + kernel_options
  # grub_file.write()

  # logger.info(f'In your {GRUB_FILE_PATH}:\n' +
  #             f'{KERNEL_OPTS_PROPERTY_NAME}="{kernel_options}" -> ' +
  #             f'{KERNEL_OPTS_PROPERTY_NAME}="{new_kernel_options}"')
  
  logger.info('Update GRUB config')

  run_shell(
    'grub2-mkconfig -o /boot/grub2/grub.cfg',
    on_success=lambda: logger.success('NVidia driver was installed\n')
  )
