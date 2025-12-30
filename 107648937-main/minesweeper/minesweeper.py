import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """
        count = 0
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                if (i, j) == cell:
                    continue
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1
        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        if len(self.cells) == self.count and self.count != 0:
            return set(self.cells)
        return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        if self.count == 0:
            return set(self.cells)
        return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        self.height = height
        self.width = width

        self.moves_made = set()
        self.mines = set()
        self.safes = set()
        self.knowledge = []

    def mark_mine(self, cell):
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the AI player learns that the given
        safe cell has a given number of neighboring mines.
        """

        # 1. Mark the cell as a move made and safe
        self.moves_made.add(cell)
        self.mark_safe(cell)

        # 2. Find all undetermined neighbors
        neighbors = set()
        i, j = cell
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if (di == 0 and dj == 0):
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < self.height and 0 <= nj < self.width:
                    neighbor = (ni, nj)
                    if neighbor in self.mines:
                        count -= 1
                    elif neighbor not in self.safes and neighbor not in self.moves_made:
                        neighbors.add(neighbor)

        # 3. Add the new sentence
        if neighbors:
            new_sentence = Sentence(neighbors, count)
            self.knowledge.append(new_sentence)

        # 4. Loop until no new inferences can be made
        while True:
            known_safes = set()
            known_mines = set()

            for sentence in self.knowledge:
                known_safes.update(sentence.known_safes())
                known_mines.update(sentence.known_mines())

            if not known_safes and not known_mines:
                break

            for safe in known_safes:
                self.mark_safe(safe)
            for mine in known_mines:
                self.mark_mine(mine)

        # 5. Infer new sentences from subset relations
        new_inferred = []
        for s1 in self.knowledge:
            for s2 in self.knowledge:
                if s1 == s2 or not s1.cells or not s2.cells:
                    continue
                if s1.cells.issubset(s2.cells):
                    diff = s2.cells - s1.cells
                    count_diff = s2.count - s1.count
                    inferred = Sentence(diff, count_diff)
                    if inferred not in self.knowledge and inferred not in new_inferred:
                        new_inferred.append(inferred)
        self.knowledge.extend(new_inferred)

        # Remove empty sentences
        self.knowledge = [s for s in self.knowledge if s.cells]

    def make_safe_move(self):
        for cell in self.safes:
            if cell not in self.moves_made:
                return cell
        return None

    def make_random_move(self):
        all_cells = set((i, j) for i in range(self.height) for j in range(self.width))
        candidates = list(all_cells - self.moves_made - self.mines)
        return random.choice(candidates) if candidates else None
