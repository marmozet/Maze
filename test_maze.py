import maze
import pytest


@pytest.mark.parametrize('file, meta',[('maze1.txt',(0,5)),('maze2.txt',(8,13)),('maze3.txt',(2,1)),('maze4.txt',(14, 10)),('maze5.txt',(1, 7))])
def test_maze(file, meta):
    m = maze.Maze(file)
    m.solve()
    assert m.solution[1][-1] == meta