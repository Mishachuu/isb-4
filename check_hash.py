import hashlib


def check_hash(x):
    return x if hashlib.sha256(f'446674{x}1378'.encode()).hexdigest() == '70ba6e37c3be80134c2fd8563043c0cb9278a43116b3bc2dfad03e2e455ed473' else False
