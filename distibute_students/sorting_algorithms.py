from ds import LinkedList, convert_to_linked_list


def bubble_sort(theSeq):
    
    if isinstance(theSeq, list):
        n = len(theSeq)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if theSeq[j] > theSeq[j + 1]:
                    theSeq[j], theSeq[j + 1] = theSeq[j + 1], theSeq[j]
        return theSeq

  
    elif isinstance(theSeq, LinkedList):
        n = len(theSeq)
        for i in range(n - 1):
            cur = theSeq.head
            for _ in range(n - i - 1):
                nxt = cur.next
                if cur.data > nxt.data:
                    cur.data, nxt.data = nxt.data, cur.data
                cur = nxt
        return theSeq

    else:
        raise TypeError(f"Unsupported type: {type(theSeq)}")