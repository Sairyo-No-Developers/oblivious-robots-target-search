from . import Algorithm, Graph, Robot


def run():
    P = Graph.Playground(False)
    P.setup()
    P.run()


if __name__ == '__main__':
    run()
