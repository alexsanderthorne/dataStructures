from gpg.constants import data


class Node:

    def __init__(self, data=None):

        self.prev = None

        self.data = data

        self.next = None

    def __repr__(self):

        return '|' + str(self.data) + '|'

        class LinkedList:

            def __init__(self):

                self.head = None

                self.length = 0

    def search(self, data):

        if self.head == None:

            return False

        else:

            node = self.head

            while node != None:

                if node.data == data:

                    return True

                node = node.next

            return False

    def __iter__(self):

        node = self.head

        while node != None:

            yield node.data

            node = node.next

    def __len__(self):

        return self.length

    def __repr__(self):

        string = ''

        node = self.head

        while node != None:

            string += str(node) + '-->'

            node = node.next

        return string


class LinkedList:

    def __init__(self):

        self.head = None

        self.length = 0

    def search(self, data):

        if self.head == None:

            return False

        else:

            node = self.head

            while node != None:

                if node.data == data:

                    return True

                node = node.next

            return False

    def __iter__(self):

        node = self.head

        while node != None:

            yield node.data

            node = node.next

    def __len__(self):

        return self.length

    def __repr__(self):

        string = ''

        node = self.head

        while node != None:

            string += str(node) + '-->'

            node = node.next

        return string


class LLSE(LinkedList):

    def add(self, data):

        self.length += 1

    node = Node(data)

    if self.head == None:

        self.head = node

    else:

        node.next = self.head

        self.head = node


def remove(self):

    if self.head != None:

        self.length -= 1

        node = self.head

        self.head = self.head.next

        node.next = None

        return node

    else:

        return None


linked_list = LLSE()
linked_list.add(3)


linked_list.add(2)
linked_list.add(1)

en(linked_list)


print(linked_list)

node = linked_list.remove()
print('nó removido:', node)
print('linked_list:', linked_list)

node = linked_list.remove()
print('nó removido:', node)
print('linked_list:', linked_list)

node = linked_list.remove()
print('nó removido:', node)
print('linked_list:', linked_list)
