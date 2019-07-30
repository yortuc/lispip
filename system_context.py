import subprocess

def shell(*commands):
    result = subprocess.run(commands, stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8').split('\n')

ctx = {
    'input': input,
    'shell': shell
}
