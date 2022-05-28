from Graph import Playground

def main():
    P = Playground(True)
    P.setup({
        "type": "ring-with-chords",
        "val": 100,
        "noOfRobots": 20,
        "noOfChords": 15
    })
    # P.setup({
    #     "type": "binomial_tree",
    #     "r": 8,
    #     "noOfRobots": 100
    # })
    # P.setup({
    #     "type": "complete_graph",
    #     "r": 60,
    #     "noOfRobots": 10
    # })
    # P.setup({
    #     "type": "complete_multipartite_graph",
    #     "r": 60,
    #     "h": 60,
    #     "noOfRobots": 50
    # })
    # P.setup({
    #     "type": "circular_ladder_graph",
    #     "r": 60,
    #     "noOfRobots": 80
    # })
    # P.setup({
    #     "type": "circulant_graph",
    #     "r": 60,
    #     "h": 60,
    #     "noOfRobots": 50
    # })
    # P.setup({
    #     "type": "chordal_cycle_graph",
    #     "r": 90,
    #     "noOfRobots": 50
    # })
    # P.setup({
    #     "type": "dorogovtsev_goltsev_mendes_graph",
    #     "r": 5,
    #     "noOfRobots": 90
    # })
    # P.setup({
    #     "type": "full_rary_tree",
    #     "r": 5,
    #     "h": 225,
    #     "noOfRobots": 90    
    # })
    # P.setup({
    #     "type": "ladder_graph",
    #     "r": 35,
    #     "noOfRobots": 60    
    # })
    # P.setup({
    #     "type": "duplication_divergence_graph",
    #     "r": 150,
    #     "noOfRobots": 60    
    # })
    #P.setup()
    print(P.run())

if __name__ == "__main__":
    main()