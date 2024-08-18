import logger, os
from nvidia import install_nvidia_driver

def main():
  try:
    install_nvidia_driver()
  except OSError:
    logger.echo('\nIt seams something went wrong during installation. You can found logs in ./logs')
    input()
    exit(1)
  else:
    input('Reboot required. Press enter to reboot.')
    os.system('systemctl reboot')

main()
