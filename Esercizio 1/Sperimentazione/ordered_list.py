# Implemento le statistiche d'ordine dinamiche utilizzando una lista doppiamente collegata
class OrderedListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None


class OrderedList():
    def __init__(self):
        self.head = None

    def insert(self, key):
        x = OrderedListNode(key)

        if self.head is None:
            self.head = x
            return

        if key < self.head.key:
            x.next = self.head
            self.head.prev = x
            self.head = x
            return

        z = self.head
        while z.next is not None and z.next.key < key:
            z = z.next

        x.next = z.next
        x.prev = z
        z.next = x
        if x.next is not None:
            x.next.prev = x

    def delete(self, key):
        z = self.head

        while z is not None and z.key != key:
            z = z.next

        if z is None:
            return

        if z.prev is not None:
            z.prev.next = z.next
        else:
            self.head = z.next

        if z.next is not None:
            z.next.prev = z.prev

    def print(self):
        z = self.head
        while z is not None:
            print(z.key, end=" ")
            z = z.next

    # Aggiungo le funzioni per implementare le statistiche d'ordine dinamiche
    def select(self, i):
        z = self.head
        count = 1
        while z is not None:
            if count == i:
                return z.key
            count += 1
            z = z.next
        return None

    def rank(self, key):
        z = self.head
        count = 0
        while z is not None and z.key <= key:
            count += 1
            z = z.next
        return count
