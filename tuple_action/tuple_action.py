class Tuple_action():
    def __init__(self,numeric_tuple,string_tuple,tuple_len,tuple1,tuple2) -> None:
        self.numeric_tuple = numeric_tuple
        self.string_tuple = string_tuple
        self.tuple_len = tuple_len
        self.tuple1 = tuple1
        self.tuple2 = tuple2

    def reverse_tuple(self):
        element = self.numeric_tuple
        len = self.tuple_len
        rev_element = ()
        while len>=0:
            flag = element[len]
            len -= 1
            rev_element = rev_element + (flag , )
        return(rev_element)

    def swap_tuple(self):
        tuple1 = self.tuple1
        tuple2 = self.tuple2
        tuple1 , tuple2 = tuple2 , tuple1
        return tuple1,tuple2
