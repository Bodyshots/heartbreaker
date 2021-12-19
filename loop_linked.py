from typing import Any, List, Union


class EmptyLinkedListError(Exception):
    pass


class Node:
    def __init__(self, item: Any) -> None:
        """
        >>> test1 = Node('test')
        >>> test1.item
        'test'
        >>> test1.next
        """
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self, items: Union[Any, List[Any]]) -> None:
        """
        
        >>> lst = LinkedList([1, 2, 3, 4, 5])
        >>> 2 in lst
        True
        >>> str(lst)
        '[1 -> 2 -> 3 -> 4 -> 5]'
        >>> isinstance(lst.get_first(), Node)
        True
        >>> isinstance(lst.get_last(), Node)
        True
        >>> lst.get_first().item == 1
        True
        >>> lst.get_last().item == 5
        True
        >>> lst.get_last().next.item == 1
        True
        >>> lst = LinkedList([])
        >>> lst._first
        >>> lst._last
        >>> lst = LinkedList([1])
        >>> lst.get_first().item == 1
        True
        >>> lst.get_last().item == 1
        True
        >>> lst1 = LinkedList(None)
        >>> lst1.get_first().item
        >>> lst1.get_last().item
        >>> len(lst1)
        1
        >>> lst2 = LinkedList(2)
        >>> lst2.get_first().item
        2
        >>> lst2.get_last().item
        2
        >>> len(lst2)
        1
        """
        if isinstance(items, list):
            if items:
                self._first = Node(items[0])
                curr = self._first
                for item in items[1:]:
                    curr.next = Node(item)
                    curr = curr.next
                self._last = curr
                self._last.next = self._first
                self._len = len(items)

            else: 
                self._first = None
                self._last = None
                self._len = 0

        else:
            self._first = Node(items)
            self._last = self._first
            self._len = 1
    
    def __len__(self) -> int:
        """
        
        >>> lst = LinkedList([1, 2, 3, 4, 5])
        >>> len(lst)
        5
        >>> lst2 = LinkedList([])
        >>> len(lst2)
        0
        >>> lst3 = LinkedList([1])
        >>> len(lst3)
        1
        """
        return self._len
    
    def get_first(self) -> Node:
        """
        Getter for the first node of a LinkedList
        """
        return self._first

    def get_last(self) -> Node:
        """
        Getter for the last node of a LinkedList
        """
        return self._last
    
    def __setitem__(self, index: int, item: Any) -> None:
        """
        
        >>> lst = LinkedList([1, 2, 3, 4, 5])
        >>> lst[2] = 'poopy'
        >>> lst[3] = 'butthole'
        >>> str(lst)
        '[1 -> 2 -> poopy -> butthole -> 5]'
        >>> lst2 = LinkedList([])
        >>> lst2[0] = 'test'
        Traceback (most recent call last):
        ...
        ValueError
        >>> lst3 = LinkedList([1])
        >>> lst3[0] = '7 haha'
        >>> str(lst3)
        '[7 haha]'
        >>> lst3[1] = 'testing'
        Traceback (most recent call last):
        ...
        ValueError
        >>> lst4 = LinkedList([1, 2, 3])
        >>> lst4[2] = 'johnny test'
        >>> str(lst4)
        '[1 -> 2 -> johnny test]'
        >>> lst4[0] = 177013
        >>> str(lst4)
        '[177013 -> 2 -> johnny test]'
        """
        if index >= len(self):
            raise ValueError

        curr = self._first

        while curr != self._last and index != 0:
            curr = curr.next
            index -= 1
        curr.item = item
    
    def __str__(self) -> str:
        """
        
        >>> lst1 = LinkedList([1, 2, 3])
        >>> str(lst1)
        '[1 -> 2 -> 3]'
        >>> lst2 = LinkedList(['test', 231, True])
        >>> str(lst2)
        '[test -> 231 -> True]'
        >>> lst3 = LinkedList([])
        >>> str(lst3)
        '[]'
        >>> lst4 = LinkedList([1])
        >>> str(lst4)
        '[1]'
        """

        items = []
        curr = self._first
        while curr != self._last:
            items.append(str(curr.item))
            curr = curr.next
        if self._last:
            items.append(str(self._last.item))
            return '[' + ' -> '.join(items) + ']'
        return '[]'
    
    def _item_match_check(self, item1, item2) -> bool:
        """
        
        >>> lst = LinkedList([])
        >>> lst._item_match_check(1, 1)
        True
        >>> lst._item_match_check(True, 1)
        False
        """
        return (isinstance(item1, type(item2)) 
                and isinstance(item2, type(item1))
                and item1 == item2)

    def append(self, item: Any) -> None:
        """

        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst1.append(4)
        >>> str(lst1)
        '[1 -> 2 -> 3 -> 4]'
        >>> lst1._first.item
        1
        >>> lst1._last.item
        4
        >>> lst1._last.next.item
        1
        >>> lst2 = LinkedList([])
        >>> lst2.append(7)
        >>> str(lst2)
        '[7]'
        >>> lst2._first.item
        7
        >>> lst2._last.item
        7
        >>> lst2.append(8)
        >>> lst2._first.item
        7
        >>> lst2._last.item
        8
        """
        if not self._first:
            temp = LinkedList([item])
            self._first = temp._first
            self._last = temp._last

        else:
            curr = self._last
            curr.next = Node(item)
            curr = curr.next
            
            curr.next, self._last = self._first, curr
        
        self._len += 1
    
    def pop(self) -> Any:
        """
        
        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst1.pop()
        3
        >>> str(lst1)
        '[1 -> 2]'
        >>> lst1._first.item
        1
        >>> lst1._last.item
        2
        >>> lst1.pop()
        2
        >>> str(lst1)
        '[1]'
        >>> lst1._first.item
        1
        >>> lst1._last.item
        1
        >>> lst1.pop()
        1
        >>> lst1._first
        >>> lst1._last
        >>> str(lst1)
        '[]'
        >>> lst1.pop()
        Traceback (most recent call last):
        ...
        EmptyLinkedListError: No items to pop
        """
        if self._first and self._first == self._last:
            return_item = self._first.item
            self._first, self._last = None, None
            self._len -= 1
            return return_item

        if self._first:
            curr = self._first

            while curr.next.next != self._first:
                curr = curr.next

            return_item = curr.next.item
            curr.next, self._last = None, curr
            self._last.next = self._first
            self._len -= 1
            return return_item
        
        raise EmptyLinkedListError('No items to pop')
    
    def count(self, item: Any) -> int:
        """
        
        >>> lst1 = LinkedList([1])
        >>> lst1.count(1)
        1
        >>> lst1.count(5)
        0
        >>> lst2 = LinkedList([2, 2, 3])
        >>> lst2.count(2)
        2
        >>> lst2.count(3)
        1
        >>> lst3 = LinkedList([1, 1, 1, 0, 0, 0, 0, False, True, False])
        >>> lst3.count(0)
        4
        >>> lst3.count(1)
        3
        >>> lst3.count(False)
        2
        >>> lst3.count(True)
        1
        >>> lst3.count('1')
        0
        """
        if not self._first:
            return 0

        count = 0
        if self._item_match_check(self._first.item, item):
            count += 1
        if self._first == self._last:
            return count

        curr = self._first.next
        while curr != self._first:
            if self._item_match_check(curr.item, item):
                count += 1
            curr = curr.next

        return count

    def insert(self, index: int, item: Any) -> None:
        """
        
        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst1.insert(0, 0)
        >>> str(lst1)
        '[0 -> 1 -> 2 -> 3]'
        >>> lst1.insert(2, 'test')
        >>> str(lst1)
        '[0 -> 1 -> test -> 2 -> 3]'
        >>> lst1.insert(4, 'testing')
        >>> str(lst1)
        '[0 -> 1 -> test -> 2 -> testing -> 3]'
        >>> lst1.insert(6, 7)
        >>> str(lst1)
        '[0 -> 1 -> test -> 2 -> testing -> 3 -> 7]'
        >>> lst1.insert(17, 10)
        Traceback (most recent call last):
        ...
        ValueError
        """
        if index > len(self):
            raise ValueError

        new_node = Node(item)

        if index == len(self):
            self.append(item)
        elif index == 0:
            rest = self._first
            self._first = new_node
            new_node.next = rest
        else:
            index -= 1
            curr = self._first
            while curr.next != self._last and index != 0:
                curr = curr.next
                index -= 1

            rest = curr.next
            curr.next = new_node
            new_node.next = rest
        self._len += 1
    
    def find(self, item: Any) -> int:
        """
        find index of <item>.

        return -1 if not in LinkedList
        """
        if not self._first:
            return -1
        if self._item_match_check(self._last.item, item):
            return len(self) - 1
        
        curr, index = self._first, 0
        while curr != self._last:
            if self._item_match_check(curr.item, item):
                return index
            curr = curr.next
            index += 1

        return -1

    def __contains__(self, item: Any) -> bool:
        """
        
        >>> lst1 = LinkedList([1])
        >>> 1 in lst1
        True
        >>> 2 in lst1
        False
        >>> True in lst1
        False
        """
        if self.find(item) == -1:
            return False
        return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
