class DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        def __init__(self, element, prev, next):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        """Create an empty list."""
        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header.next = self.trailer  # trailer is after header
        self.trailer.prev = self.header  # header is before trailer
        self.size = 0  # number of elements

    def __len__(self):
        """Return the number of elements in the list."""
        return self.size

    def is_empty(self):
        """Return True if list is empty."""
        return self.size == 0

    def insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self.Node(e, predecessor, successor)  # linked to neighbors
        predecessor.next = newest
        successor.prev = newest
        self.size += 1
        return newest

    def delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self.size -= 1
        element = node.element  # record deleted element
        node.prev = node.next = node.element = None  # deprecate node
        return element  # return deleted element


class PositionalList(DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self.container = container
            self.node = node

        def element(self):
            """Return the element stored at this Position."""
            return self.node.element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other.node is self.node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of eq

    def header_position(self):
        """Return the header sentinel as a Position (unconventional)."""
        return self.make_position(self.header)

    def trailer_position(self):
        """Return the trailer sentinal as a Position"""
        return self.make_position(self.trailer)

    def validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.next is None:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p.node

    def make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self.header or node is self.trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)  # legitimate position

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self.make_position(self.header.next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self.make_position(self.trailer.prev)

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self.validate(p)
        return self.make_position(node.prev)

    def after(self, p):
        """Return the Position just after Position p (or None if p is last)."""
        node = self.validate(p)
        return self.make_position(node.next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super().insert_between(e, predecessor, successor)
        return self.make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self.insert_between(e, self.header, self.header.next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self.insert_between(e, self.trailer.prev, self.trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self.validate(p)
        return self.insert_between(e, original.prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self.validate(p)
        return self.insert_between(e, original, original.next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self.validate(p)
        return self.delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.
        """
        original = self.validate(p)
        old_value = original.element  # temporarily store old element
        original.element = e  # replace with new element
        return old_value  # return the old element value