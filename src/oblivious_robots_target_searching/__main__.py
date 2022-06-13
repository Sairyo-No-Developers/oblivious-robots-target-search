from . import Algorithm, Graph, Robot, __version__


def run():
    print(f"Oblivious Robots Target Search Version : {__version__}")
    P = Graph.Playground(False)
    P.setup()
    P.run()


if __name__ == '__main__':
    run()
